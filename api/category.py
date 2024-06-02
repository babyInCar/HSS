
from fastapi import APIRouter
from db.models import Category
from fastapi.exceptions import HTTPException
from tortoise.contrib.pydantic import pydantic_model_creator
cat_api = APIRouter()


@cat_api.get("/")
async def getCategoryList():
    goods = await Category.all()
    return goods

CategoryRead = pydantic_model_creator(
    cls=Category,
    name='CategoryRead'
)

CategoryCreate = pydantic_model_creator(
    cls=Category,
    name='CategoryCreate',
    exclude_readonly=True  # Exclude `id` on creating
)


@cat_api.post("/", response_model=CategoryRead)
async def addCategory(category_in: CategoryCreate):
    good = await Category.create(
        **category_in.dict(
            exclude_unset=True,
        )
    )
    return good