from models.product import ProductModel


class ProductDAO(ProductModel):

    def get_by_id(self, id):
        return ProductModel.query.filter_by(id=id, deleted=False).first()

    def get_by_name(self, name):
        return ProductModel.query.filter(ProductModel.name.ilike(name)).first()

    def get_products(self, input_filters):

        filters = []
        order = []

        if input_filters.get("name"):
            filters.append(ProductModel.name.ilike(f"%{input_filters['name']}%"))
        if input_filters.get("price"):
            filters.append(ProductModel.price == input_filters['price'])
        if not input_filters.get("status"):
            filters.append(ProductModel.deleted == False)
        if input_filters.get("status"):
            filters.append(ProductModel.deleted == True)

        if input_filters.get("order_by") == "name":
            if input_filters.get("order") and input_filters.get("order").lower() == "desc":
                order.append(-ProductModel.name)
            else:
                order.append(-ProductModel.name)
        if input_filters.get("order_by") == "price":
            if input_filters.get("order") and input_filters.get("order").lower() == "desc":
                order.append(-ProductModel.price)
            else:
                order.append(ProductModel.price)
        else:
            if input_filters.get("order") and input_filters.get("order").lower() == "desc":
                order.append(-ProductModel.created_date)
            else:
                order.append(ProductModel.created_date)

        products = ProductModel.query.filter(*filters).order_by(*order).all()

        return products
