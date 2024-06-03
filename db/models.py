from tortoise import fields
from tortoise.models import Model
from enum import IntEnum


class Channels(IntEnum):
    JD = 1
    TAOBAO = 2
    ALIPAY = 3   # 支付宝小程序
    WECHAT = 4   # 小程序
    DOUYIN = 5
    PDD = 6


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
    buy_channel = fields.IntEnumField(Channels, description="购买渠道")
    location = fields.ForeignKeyField("models.Location", related_name="goods")
    description = fields.CharField(description="备注信息", max_length=32)
    guarantee_period = fields.IntField(description="保修期限", default=1)
    guarantee_end_date = fields.DateField(description="保修截止时间")

    class Meta:
        table = "goods"


class GoodMoveLog(Model):

    id = fields.IntField(pk=True)
    move_date = fields.DateField(description="移动日期")
    source_loc = fields.ForeignKeyField("models.Location", related_name="move_source")
    dest_loc = fields.ForeignKeyField("models.Location", related_name="move_dest")
    desc = fields.CharField(max_length=32, description="备注")

    class Meta:
        table = "move_log"
