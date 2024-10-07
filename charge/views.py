import csv
import io
from uuid import UUID
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from datetime import datetime


@csrf_exempt
@require_POST
def upload_csv(request):
    if "file" not in request.FILES:
        return JsonResponse({"error": "Arquivo CSV não encontrado."}, status=400)

    file = request.FILES["file"]

    if not file.name.endswith(".csv"):
        return JsonResponse(
            {"error": "Formato de arquivo inválido, esperado .csv"}, status=400
        )

    try:
        decoded_file = file.read().decode("utf-8")
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

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

        for row in reader:
            try:
                name = row["name"]
                government_id = row["governmentId"]
                email = row["email"]
                debt_amount = float(row["debtAmount"])
                debt_due_date = datetime.strptime(row["debtDueDate"], "%Y-%m-%d").date()
                debt_id = UUID(row["debtId"].strip())

            except (ValueError, KeyError, ValidationError) as e:
                return JsonResponse(
                    {"error": f"Dados inválidos na linha: {row}. Erro: {str(e)}"},
                    status=400,
                )

        return JsonResponse(
            {"message": "Arquivo CSV processado com sucesso!"}, status=200
        )

    except Exception as e:
        return JsonResponse(
            {"error": f"Erro ao processar o arquivo CSV: {str(e)}"}, status=500
        )
