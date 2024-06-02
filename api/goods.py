
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from db.models import Goods
from fastapi.exceptions import HTTPException
from tortoise.contrib.pydantic import pydantic_model_creator
goods_api = APIRouter()


@goods_api.get("/")
async def getGoodsList():
    goods = await Goods.all()
    return goods


@goods_api.get("/goods/{goods_id}")
async def getGoodsByGoodsId(good_id: int):
    """查询某一个商品"""
    good = await Goods.get(id=good_id)
    return good


@goods_api.get("/{category_id}")
async def getGoodsByCategoryId(category_id: int):
    good = await Goods.get(category_id=category_id)
    return good


class GoodsIn(BaseModel):
    name: str
    category_id_id: int     # 如果是外键的话，必须要在字段后面`_id`才能写进数据表中
    is_deleted: bool = False
    buy_date: date
    location_id: int


GoodRead = pydantic_model_creator(
    cls=Goods,
    name='GoodsRead'
)

GoodCreate = pydantic_model_creator(
    cls=Goods,
    name='GoodCreate',
    # exclude_readonly=True  # Exclude `id` on creating
)


@goods_api.post("/", response_model=GoodRead)
async def createGood(good_in: GoodsIn):
    """创建某一个商品  Ask:是否可以批量创建呢 """
    # await Goods.create(good_in.dict())
    good = await Goods.create(
        # name=good_in.name,
        # category_id=good_in.category_id,
        # buy_date=good_in.buy_date,
        # is_deleted=good_in.is_deleted,
        # location=good_in.location
        **good_in.dict()
    )
    return good


# @goods_api.put("/{good_id}")
# async def updateGoodsInfo():
#     pass

@goods_api.delete("/{good_id}")
async def deleteGoods(good_id: int):
    delete_count = await Goods.filter(id=good_id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail=f"主键为{id}的病理不存在")
    return {"msg": "删除成功"}

