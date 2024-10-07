import csv
import io
from uuid import UUID
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from datetime import datetime
from .dtos import DebtDTO
from .worker import Worker


def _parse_row(row) -> DebtDTO:
    name = row["name"]
    government_id = row["governmentId"]
    email = row["email"]
    debt_amount = float(row["debtAmount"])
    debt_due_date = datetime.strptime(row["debtDueDate"], "%Y-%m-%d").date()
    debt_id = UUID(row["debtId"].strip())

    debt_dto = DebtDTO(
        name=name,
        government_id=government_id,
        email=email,
        debt_amount=debt_amount,
        debt_due_date=debt_due_date,
        debt_id=debt_id,
    )

    return debt_dto


def _check_params_in_request(request):
    if "file" not in request.FILES:
        return JsonResponse({"error": "Arquivo CSV não encontrado."}, status=400)

    file = request.FILES["file"]

    if not file.name.endswith(".csv"):
        return JsonResponse(
            {"error": "Formato de arquivo inválido, esperado .csv"}, status=400
        )


def _check_file_columns(reader):
    expected_columns = [
        "name",
        "governmentId",
        "email",
        "debtAmount",
        "debtDueDate",
        "debtId",
    ]

    if not expected_columns == reader.fieldnames:
        return JsonResponse(
            {
                "error": "Formato de colunas inválido. Colunas esperadas: {}".format(
                    ", ".join(expected_columns)
                )
            },
            status=400,
        )


@csrf_exempt
@require_POST
def upload_csv(request):
    if exception := _check_params_in_request(request):
        return exception

    file = request.FILES["file"]

    try:
        decoded_file = file.read().decode("utf-8")
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        if exception := _check_file_columns(reader):
            return exception

        list_debts_dtos = []
        for row in reader:
            try:
                debt_dto = _parse_row(row)
                list_debts_dtos.append(debt_dto)

            except (ValueError, KeyError, ValidationError) as e:
                return JsonResponse(
                    {"error": f"Dados inválidos na linha: {row}. Erro: {str(e)}"},
                    status=400,
                )

        # Suposed to be assyncronous using celery and return the job_id to be processed by the workers
        Worker().async_debt_processing(list_debts_dtos)

        return JsonResponse(
            {"message": "Arquivo CSV está sendo processado"}, status=200
        )

    except Exception as e:
        return JsonResponse(
            {"error": f"Erro ao processar o arquivo CSV: {str(e)}"}, status=500
        )
