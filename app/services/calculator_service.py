#비즈니스 로직을 처리하는 서비스파일

from fastapi import HTTPException

def calculate(number1: float, number2: float, operator: str) -> float:
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        if number2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return number1 % number2
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")
    
#추가기능(계산내역기록)

import logging

# 로그 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

def calculate(number1: float, number2: float, operator: str) -> float:
    result = 0
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "%":
        if number2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = number1 % number2
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")
    
    # 로그 저장
    logger.info(f"Operation: {operator}, Numbers: {number1}, {number2}, Result: {result}")
    
    return result