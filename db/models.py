from tortoise import fields
from tortoise.models import Model


class User(Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    sex = fields.IntField(description="性别，0：女 1：男")
    relationship = fields.ForeignKeyField("models.RelationShip", related_name="user")
    age = fields.IntField(description="年龄")
    degree = fields.CharField(max_length=16, description="学历")

    class Meta:
        table = "res_user"


class RelationShip(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=16, description='关系名称')

    class Meta:
        table = "res_relationship"


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="类别名称")
    parent_id = fields.ForeignKeyField("models.Category", related_name="category", null=True)  # 父类

    class Meta:
        table = "category"


class Location(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="名称")
    code = fields.CharField(max_length=16, description="代码")
    pic = fields.CharField(max_length=128, description="存放路径")

    class Meta:
        table = "location"


class Goods(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="名称")
    category_id = fields.ForeignKeyField("models.Category", related_name="goods")
    buy_date = fields.DateField(description='购买日期')
    is_deleted = fields.BooleanField(description="是否遗失")
    location = fields.ForeignKeyField("models.Location", related_name="goods")

    class Meta:
        table = "goods"
