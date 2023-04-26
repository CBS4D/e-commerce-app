from models import db, BaseActions
from datetime import datetime


class OrderModel(db.Model, BaseActions):

    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    is_open = db.Column(db.Boolean, default=True)
    is_canceled = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    items = db.relationship('OrderItemModel', backref='order_item')


class OrderItemModel(db.Model, BaseActions):

    __tablename__ = 'orderitem'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Numeric)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
