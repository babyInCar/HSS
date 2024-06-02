
from fastapi import FastAPI,Request
app = FastAPI()


@app.middleware("http")
async def m2(request: Request, call_next):
    print("m2 request")
    response = await call_next(request)
    # 响应代码块
    response.headers['author'] = "gaos"
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    print("m1 request")
    response = await call_next(request)

    # 相应代码块
    print("m1 response")
    return response

