from schemas import ma
from models.order import OrderItemModel

from marshmallow import fields, validate, post_load


class OrderItemPostSchema(ma.Schema):

    __model__ = OrderItemModel

    id = fields.Int()
    order_id = fields.Int()
    product_id = fields.Int()
    quantity = fields.Int()
    price = fields.Float()
    created_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")

    @post_load
    def make_orderitem(self, data, **kwargs):
        return OrderItemModel(**data)