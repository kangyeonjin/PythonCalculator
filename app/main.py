##fastapi 앱을 시작하는 파일

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

#app.include_router(calculator.router)

# @app.get("/")
# async def read_root():
#     return {"message":"welcome to the calculator API"}

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

#엔드포인트
@app.get("/calculator", response_class=HTMLResponse) 
async def calculator(request: Request):
    try:
        return templates.TemplateResponse("calculator.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, number1: int, number2: int, operator: str):
    try:
        
        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "%":
            result = number1 % number2
        else:
            raise HTTPException(status_code=400, detail="Invalid operator")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # 템플릿 렌더링
    return templates.TemplateResponse("result.html", {
        "request": request,
        "number1": number1,
        "number2": number2,
        "operator": operator,
        "result": result
    })