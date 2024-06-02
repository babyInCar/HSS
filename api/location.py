from fastapi import APIRouter, UploadFile, Depends,File
from pydantic import BaseModel, Field
from db.models import Location
import os
from fastapi.exceptions import HTTPException
from tortoise.contrib.pydantic import pydantic_model_creator

loc_api = APIRouter()

LocRead = pydantic_model_creator(
    cls=Location,
    name='LocRead'
)

@loc_api.get('/')
async def getLocInfo():
    loc = await Location.all()
    return loc

LocCreate = pydantic_model_creator(
    cls=Location,
    name='LocCreate',
    exclude_readonly=True  # Exclude `id` on creating
)


class LocationIn(BaseModel):
    name: str = Field(...)
    code: str = Field(...)
    # pic: UploadFile


@loc_api.post('/', response_model=LocRead)
async def insertLocInfo(loc_in: LocationIn = Depends(),
                        pic: UploadFile = File(...),):
    # 把文件放到服务器对应目录里面去
    file_path = os.path.join('oss/images', pic.filename)
    with open(file_path, "wb") as file:
        for line in pic.file:
            file.write(line)
    loc_dict = {
        'name': loc_in.name,
        'code': loc_in.code,
        'pic': file_path
    }
    loc = await Location.create(**loc_dict)
    return loc
