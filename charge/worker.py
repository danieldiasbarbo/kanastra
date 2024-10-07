from .dtos import DebtDTO


class Worker:
    processed_debts_db = set()

    # Should be declared in a separated module with the SMTP connection and error handlings
    def send_email(self, email, content):
        print(f"Mail sent to {email}, content: {content}")

    def _check_if_debt_is_already_processed(self, debt: DebtDTO):
        if debt.debt_id in self.processed_debts_db:
            return True

    def async_debt_processing(self, debts_dtos: list[DebtDTO]):
        for debt in debts_dtos:
            if not self._check_if_debt_is_already_processed(debt):
                self.processed_debts_db.add(debt.debt_id)
                self.send_email(
                    debt.email,
                    f"Favor {debt.name}, pague o montante R${debt.debt_amount}",
                )
            else:
                print(f"Débito {debt.debt_id} já processado")
