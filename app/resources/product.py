from datetime import datetime
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from daos.product_daos import ProductDAO
from schemas.product import ProductPostSchema, ProductPutSchema, ProductListSchema


class ProductResource(Resource):

    def get(self, id):
        """
        fetch product using product id
        """
        try:
            if not id:
                return {
                    "message": "please provide product id",
                    "status": "failed"
                }, 400
            
            data = ProductDAO().get_by_id(id)
            if not data:
                return {
                    "message": f"product not found for product id {id}",
                    "status": "failed"
                }, 404
            product_schema = ProductPostSchema()
            return product_schema.dump(data), 200
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
    
    def post(self):
        try:
            request_data = request.get_json()
            # validate data
            product_schema = ProductPostSchema()
            product = product_schema.load(request_data)

            # check product duplication
            product_check = ProductDAO().get_by_name(product.name)
            if product_check:
                return {
                    "message": "product already exists with name " + 
                        f"'{product_check.name}' has id - {product_check.id}",
                    "status": "failed"
                }, 400
            else:
                product.save()
                return product_schema.dump(product), 201
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
        
    def put(self):
        try:
            request_data = request.get_json()
            # validate data
            product_schema = ProductPutSchema()
            valid_data = product_schema.load(request_data)
            
            product_data = ProductDAO().get_by_id(id=valid_data["id"])
            if not product_data:
                return {
                    "message": f"product not found for product id {valid_data['id']}",
                    "status": "failed"
                }, 404

            product_data.price = request_data.get("price", product_data.price)
            product_data.name = request_data.get("name", product_data.name)
            product_data.deleted = request_data.get("deleted", product_data.deleted)
            product_data.updated_date = datetime.utcnow()
            product_data.save()

            return product_schema.dump(product_data), 200
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
    
    def delete(self, id):
        try:
            if not id:
                return {
                    "message": "please provide produvt id",
                    "status": "failed"
                }, 400
            
            data = ProductDAO().get_by_id(id=id)
            if not data:
                return {
                    "message": f"product not found for product id {id}",
                    "status": "failed"
                }, 404

            data.deleted = True
            data.updated_date = datetime.utcnow()
            data.save()
            
            return {
                "message": "product has been removed",
                "status": "success"
            }, 200
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500
        

class ProductListResource(Resource):

    def get(self):
        """
        fetch multiple products depending on filter/order
        """
        try:
            filters = request.args.to_dict()
            valid_filters = ProductListSchema().load(filters)
            print(valid_filters)
            data = ProductDAO().get_products(valid_filters)
            if not data:
                return {
                    "message": f"No products found",
                    "status": "failed"
                }, 404
            product_schema = ProductListSchema(many=True)
            return product_schema.dump(data), 200
        except ValidationError as v_err:
            return v_err.messages, 400
        except Exception as e:
            print(e)
            return {
                "message": "Some Internal error",
                "status": "failed"
            }, 500