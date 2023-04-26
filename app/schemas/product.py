from schemas import ma
from models.product import ProductModel

from marshmallow import fields, post_load, validate


class ProductPostSchema(ma.Schema):

    __model__ = ProductModel

    id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    created_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")

    @post_load
    def make_product(self, data, **kwargs):
        return ProductModel(**data)


class ProductPutSchema(ma.Schema):

    __model__ = ProductModel

    id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    deleted = fields.Boolean()


class ProductListSchema(ma.Schema):

    __model__ = ProductModel

    id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    status = fields.Boolean()
    order_by = fields.Str(validate=validate.OneOf(["name", "created_date", "price"]))
    order = fields.Str(validate=validate.OneOf(["ASC", "DESC", "asc", "desc"]))
    created_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")