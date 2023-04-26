from datetime import datetime
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from daos.order_daos import OrderDAO
# from daos.order_item_daos import OrderItemDAO
# from models.order import OrderItemModel, OrderModel
from schemas.order import OrderPostSchema, OrderListSchema # OrderItemPostSchema


class OrderResource(Resource):

    def get(self, id):
        """
        fetch order using order id
        """
        try:
            if not id:
                return {
                    "message": "please provide order id",
                    "status": "failed"
                }, 400
            
            data = OrderDAO().get_by_id(id)
            if not data:
                return {
                    "message": f"order not found for order id : {id}",
                    "status": "failed"
                }, 404
            product_schema = OrderPostSchema()
            return product_schema.dump(data), 200
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
    
    def post(self):
        """
        Place an order
        """
        try:
            request_data = request.get_json()
            # validate data
            order_schema = OrderPostSchema()
            order = order_schema.load(request_data)
            order_db = OrderDAO().get_by_user(order.user_id)
            order_db.is_open = False
            order_db.save()
            return order_schema.dump(order), 201
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            raise e
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500

    def put(self):
        """
        Cancel an order
        """
        try:
            request_data = request.get_json()
            # validate data
            order_schema = OrderPostSchema()
            valid_data = order_schema.load(request_data)
            order_data = OrderDAO().get_by_user(valid_data.user_id)
            if not order_data:
                return {
                    "message": f"order not found for order id : {valid_data['id']}",
                    "status": "failed"
                }, 404

            order_data.is_cancelled = True
            order_data.updated_date = datetime.utcnow()
            order_data.save()
            return order_schema.dump(order_data), 200
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500


class OrderListResource(Resource):

    def get(self):
        """
        fetch multiple products depending on filter/order
        """
        try:
            filters = request.args.to_dict()
            valid_filters = OrderListSchema().load(filters)
            print(valid_filters)
            data = OrderDAO().get_orders(valid_filters)
            if not data:
                return {
                    "message": f"No orders found",
                    "status": "failed"
                }, 404
            product_schema = OrderListSchema(many=True)
            return product_schema.dump(data), 200
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500