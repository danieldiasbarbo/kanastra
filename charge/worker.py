from .dtos import DebtDTO


class Worker:
    def __init__(self) -> None:
        self.processed_debts_db = set()

    def _generate_boleto(self, debt: DebtDTO):
        boleto = f"Favor {debt.name}, pague o montante R${debt.debt_amount}"
        print(f"Boleto para {debt.debt_id} gerado")
        return boleto

    # Should be declared in a separated module with the SMTP connection and error handlings
    def _send_email(self, email, content):
        print(f"Mail sent to {email}, content: {content}")

    def _check_if_debt_is_already_processed(self, debt: DebtDTO):
        if debt.debt_id in self.processed_debts_db:
            return True

    def async_debt_processing(self, debts_dtos: list[DebtDTO]):
        debt_dtos_that_email_was_sent = []
        for debt in debts_dtos:
            if not self._check_if_debt_is_already_processed(debt):
                boleto = self._generate_boleto(debt)
                self._send_email(debt.email, boleto)
                self.processed_debts_db.add(debt.debt_id)
                debt_dtos_that_email_was_sent.append(debt)
            else:
                print(f"Débito {debt.debt_id} já processado")
        return debt_dtos_that_email_was_sent
