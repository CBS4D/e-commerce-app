from models.order import OrderItemModel


class OrderItemDAO(OrderItemModel):

    def get_by_id(self, id):
        return OrderItemModel.query.filter_by(id=id).first()

    def get_by_orderid(self, order_id):
        return OrderItemModel.query.filter_by(order_id=order_id).all()

    def get_by_user(self, user_id):
        return OrderItemModel.query.filter_by(user_id=user_id).first()
