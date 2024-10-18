# 요청 데이터를 정의하는 pydantic모델 파일

from pydantic import BaseModel, Field
from typing import Literal

class CalculatorRequest(BaseModel):
    number1: float = Field(..., description="첫 번째 숫자")
    number2: float = Field(..., description="두 번째 숫자")
    operator: Literal["+", "-", "*", "%"] = Field(..., description="연산자 (예: +, -, *, %)")