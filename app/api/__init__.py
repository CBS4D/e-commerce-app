from flask_restful import Api

from resources import product, order, order_item


app_api = Api()

# product resource binding
app_api.add_resource(product.ProductResource, "/api/v1/product/<id>", methods=['GET'], endpoint="get_product")
app_api.add_resource(product.ProductResource, "/api/v1/product/", methods=['POST'], endpoint="create_product")
app_api.add_resource(product.ProductResource, "/api/v1/product/", methods=['PUT'], endpoint="update_product")
app_api.add_resource(product.ProductResource, "/api/v1/product/<id>", methods=['DELETE'], endpoint="delete_product")

app_api.add_resource(product.ProductListResource, "/api/v1/products/", methods=['GET'], endpoint="get_products")

# order resource binding
app_api.add_resource(order.OrderResource, "/api/v1/order/<id>", methods=['GET'], endpoint="get_order")
app_api.add_resource(order.OrderResource, "/api/v1/order/", methods=['POST'], endpoint="create_order")
app_api.add_resource(order.OrderResource, "/api/v1/order/", methods=['PUT'], endpoint="cancel_order")

app_api.add_resource(order.OrderListResource, "/api/v1/orders/", methods=['GET'], endpoint="get_orders")

# order item resource binding
app_api.add_resource(order_item.OrderItemResource, "/api/v1/order/item/<id>", methods=['GET'], endpoint="get_order_item")
app_api.add_resource(order_item.OrderItemResource, "/api/v1/order/item/<user_id>", methods=['POST'], endpoint="create_order_item")
