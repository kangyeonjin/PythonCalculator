#api경로와 기능을 정의하는 파일

from fastapi import APIRouter
from app.models.calculator_request import CalculatorRequest
from app.services.calculator_service import calculate

router = APIRouter()

@router.post("/calculate")
def perform_calculation(request: CalculatorRequest):
    result = calculate(request.number1, request.number2, request.operator)
    return {"result": result}
