from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class DebtDTO:
    name: str
    government_id: str
    email: str
    debt_amount: float
    debt_due_date: date
    debt_id: UUID
