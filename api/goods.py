
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from datetime import date
from db.models import Goods
from settings import CHANNEL_MAP
from fastapi.exceptions import HTTPException
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.queryset import Q
goods_api = APIRouter()


@goods_api.get("/")
async def getGoodsList():
    goods = await Goods.all()
    for good in goods:
        good.buy_channel = CHANNEL_MAP.get(good.buy_channel)
    return goods


@goods_api.get("/{good_id}", description="通过商品id获取商品")
async def getGoodsByGoodsId(good_id: int):
    """查询某一个商品"""
    good = await Goods.get(id=good_id)  # 返回的是一个对象
    if good.buy_channel:
        good.buy_channel = CHANNEL_MAP.get(good.buy_channel)
    return good


@goods_api.get("/name/{name}", description="通过名称模糊查询到商品")
async def getGoodsByName(name: str):
    """通过商品名称模糊查询 """
    query = Q(name__contains=name) | Q(name__icontains=name)
    goods = await Goods.filter(query)
    for good in goods:
        good.buy_channel = CHANNEL_MAP.get(good.buy_channel)
    return goods


@goods_api.get("/category/{category_id}", description="通过类别获取商品")
async def getGoodsByCategoryId(category_id: int):
    """通过商品分类查询商品信息"""
    goods = await Goods.filter(category_id_id=category_id)  # 返回的是一个QuerySet
    for good in goods:
        good.buy_channel = CHANNEL_MAP.get(good.buy_channel)
    return goods


class GoodsIn(BaseModel):
    name: str
    category_id_id: int = Field(..., description="物品的类别")    # 如果是外键的话，必须要在字段后面`_id`才能写进数据表中
    is_deleted: bool = Field(default=False, description="是否被删除")
    buy_date: date = Field(..., description="物品的类别")
    location_id: int
    buy_channel: int = Field(default=1, description="购买渠道，默认填入JD")
    guarantee_period: int = Field(default=1, description="保修年限，默认1年")
    guarantee_end_date: date
    description: str


GoodRead = pydantic_model_creator(
    cls=Goods,
    name='GoodsRead'
)

GoodCreate = pydantic_model_creator(
    cls=Goods,
    name='GoodCreate',
    # exclude_readonly=True  # Exclude `id` on creating
)


@goods_api.post("/", response_model=GoodRead, description="添加物品")
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

@goods_api.delete("/{good_id}", description="删除物品")
async def deleteGoods(good_id: int):
    delete_count = await Goods.filter(id=good_id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail=f"主键为{id}的病理不存在")
    return {"msg": "删除成功"}


