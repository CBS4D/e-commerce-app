from schemas import ma
from models.order import OrderModel, OrderItemModel

from marshmallow import fields, validate, post_load


class OrderItemPostSchema(ma.Schema):

    __model__ = OrderItemModel

    id = fields.Int()
    order_id = fields.Int()
    product_id = fields.Int()
    quantity = fields.Int()
    price = fields.Float()
    created_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    date_updated = fields.DateTime(format="%Y-%m-%d %H:%M:%S")

    @post_load
    def make_orderitem(self, data, **kwargs):
        return OrderModel(**data)

class OrderPostSchema(ma.Schema):

    __model__ = OrderModel

    id = fields.Int()
    user_id = fields.Int()
    items = fields.List(fields.Nested(OrderItemPostSchema))
    is_open = fields.Boolean()
    is_cancelled = fields.Boolean()
    created_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    updated_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")

    @post_load
    def make_order(self, data, **kwargs):
        print(data)
        return OrderModel(**data)
    

class OrderListSchema(ma.Schema):

    __model__ = OrderModel

    id = fields.Int()
    user_id = fields.Int()
    open = fields.Boolean()
    cancelled = fields.Boolean()
    order_by = fields.Str(validate=validate.OneOf(["created_date",]))
    order = fields.Str(validate=validate.OneOf(["ASC", "DESC", "asc", "desc"]))
    created_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")