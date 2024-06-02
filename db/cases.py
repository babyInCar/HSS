
from fastapi import APIRouter
from pydantic import BaseModel
app_case = APIRouter()


class Case(BaseModel):
    case_id: int
    info_patient_name: str
    info_patient_age: int
    pay_status: bool


@app_case.post("/case/{case_id}")
def case_insert(case_id: int, case: Case):
    pass
