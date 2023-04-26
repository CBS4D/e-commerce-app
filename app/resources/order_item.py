from datetime import datetime
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from daos.order_daos import OrderDAO
from daos.order_item_daos import OrderItemDAO
from models.order import OrderItemModel, OrderModel
from schemas.order_item import OrderItemPostSchema


class OrderItemResource(Resource):

    def get(self, id):
        """
        fetch order item using product id
        """
        try:
            if not id:
                return {
                    "message": "please provide product id",
                    "status": "failed"
                }, 400
            
            data = OrderItemDAO().get_by_id(id)
            if not data:
                return {
                    "message": f"product not found for product id {id}",
                    "status": "failed"
                }, 404
            product_schema = OrderItemPostSchema()
            return product_schema.dump(data), 200
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
    
    def post(self, user_id):
        try:
            request_data = request.get_json()
            # validate data
            order_item_schema = OrderItemPostSchema()
            order_item = order_item_schema.load(request_data)

            # check for open order
            open_order = OrderDAO().get_by_user(user_id)
            print(open_order)
            if open_order:
                order = open_order
                for item in order.items:
                    if item.product_id == order_item.product_id:
                        item.quantity += order_item.quantity
                        item.price += order_item.price
                    else:
                        order_items = OrderItemModel()
                        order_items.product_id = order_item.product_id
                        order_items.quantity = order_item.quantity
                        order_items.price = order_item.price
                        order.items.append(order_items)
            else:
                order = OrderModel()
                order.user_id = user_id

                order_items = OrderItemModel()
                order_items.product_id = order_item.product_id
                order_items.quantity = order_item.quantity
                order_items.price = order_item.price
                order.items.append(order_items)

            order.save()
            return order_item_schema.dump(order), 201
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            raise e
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
