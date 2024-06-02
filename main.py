# This is a sample Python script.
import uvicorn
from typing import Union
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise
from api.goods import goods_api
from api.category import cat_api
from api.location import loc_api
from settings import TORTOISE_ORM
app = FastAPI()

app.include_router(cat_api, prefix="/cat", tags=["类别信息相关接口"])
app.include_router(goods_api, prefix="/good", tags=["物品信息相关接口"])
app.include_router(loc_api, prefix="/loc", tags=["位置信息相关接口"])

register_tortoise(
    app=app,
    config=TORTOISE_ORM,

)

# async def initialize_db():
#     await Tortoise.init(
#         db_url=os.environ.get("TORTOISE_CONNECTION_DEFAULT"),
#         modules={"models": ["db.models", "aerich.models"]}
#     )
#     print("Database initialized successfully")

class Student(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None]


@app.get("/")
async def read_index():
    return {"Hello": "World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q:Union[str, None]=None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Student):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}


class UploadData(BaseModel):
    text_data: str


@app.post("/upload/")
async def upload(upload_data: UploadData, file: UploadFile = File(...)):
    # 读取文件内容
    file_content = await file.read()

    # 处理文本数据
    print(f"Received text data: {upload_data.text_data}")

    # 这里可以根据需要处理文件和其他数据
    # 示例：只是简单打印文件名和长度
    print(f"Uploaded file: {file.filename}, size: {len(file_content)} bytes")

    return {"file_name": file.filename, "text_data": upload_data.text_data}

# @app.on_event("startup")
# async def startup_event():
#     # 在应用启动时运行的异步操作
#     result = await initialize_db()
#     print(result)


if __name__ == '__main__':
    # initialize_db()
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
