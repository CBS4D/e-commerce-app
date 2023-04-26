from models.order import OrderModel


class OrderDAO(OrderModel):

    def get_by_id(self, id):
        return OrderModel.query.filter_by(id=id, deleted=False).first()

    def get_by_user(self, user_id):
        return OrderModel.query.filter_by(user_id=user_id).first()

    def get_orders(self, input_filters):

        filters = []
        order = []
    
        if input_filters.get("user_id"):
            filters.append(OrderModel.user_id == input_filters['user_id'])
        if input_filters.get("open") == True:
            filters.append(OrderModel.is_open == True)
        if input_filters.get("open") == False:
            filters.append(OrderModel.is_open == False)
        if input_filters.get("cancelled"):
            filters.append(OrderModel.is_canceled == True)

        if input_filters.get("order") and input_filters.get("order").lower() == "desc":
            order.append(-OrderModel.created_date)
        else:
            order.append(OrderModel.created_date)

        orders = OrderModel.query.filter(*filters).order_by(*order).all()

        return orders
