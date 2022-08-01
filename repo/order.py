# - Get list, get by id, change status order
# Thông tin province_code, district_code, ward_code phải là code theo đơn vị hành chính VN
from decimal import Decimal
from dependency_injector.providers import List
from sqlalchemy import DateTime
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session

from database import SessionLocal
from model import Order
from project.schemas import Sort
from status import EOrderStatus


class OrderRepo():
    def get_orders_repo(self,
                        customer_name: str, from_price: Decimal, to_price: Decimal,
                        id: int, payment_method: str, name_shipping: str,
                        phone_shipping: str, address_shipping: str,
                        province_code_shipping: str, ward_code_shipping: str,
                        district_code_shipping: str,
                        customer_username: str,
                        sort_direction: Sort.Direction,
                        page: int, size: int) -> List[Row]:
        session: Session = SessionLocal()
        query = session.query(Order)
        if customer_name:
            query = query.filter(Order.customer_name.like(f"%{customer_name}%"))
        if from_price:
            query = query.filter(Order.price == from_price)
        if to_price:
            query = query.filter(Order.price == to_price)
        if id:
            query = query.filter(Order.id == id)
        if customer_username:
            query = query.filter(Order.customer_username.like(f"%{customer_username}%"))
        if payment_method:
            query = query.filter(Order.payment_method.like(f"%{payment_method}%"))
        if phone_shipping:
            query = query.filter(Order.name_shipping.like(f"%{phone_shipping}%"))
        if name_shipping:
            query = query.filter(Order.name_shipping.like(f"%{name_shipping}%"))
        if address_shipping:
            query = query.filter(Order.address_shipping.like(f"%{address_shipping}%"))
        if province_code_shipping:
            query = query.filter(Order.province_code_shipping.like(f"%{province_code_shipping}%"))
        if district_code_shipping:
            query = query.filter(Order.district_code_shipping.like(f"%{district_code_shipping}%"))
        if ward_code_shipping:
            query = query.filter(Order.ward_code_shipping.like(f"%{ward_code_shipping}%"))
        if sort_direction == 'asc':
            query = query.order_by(Order.created_time)
        if sort_direction == 'desc':
            query = query.order_by(Order.created_time).desc()
        if page and size:
            query = query.limit(size).offset((page - 1) * size)
        rs = session.execute(query).fetchall()
        return rs

    def get_order_by_id_repo(self, order_id: int) -> Row:
        session: Session = SessionLocal()
        query = session.query(Order).filter(Order.id == order_id)
        return session.execute(query).first()

    def insert_order(self, order: Order):
        session: Session = SessionLocal()
        session.add(Order(
            created_at=order.created_at,
            created_by=order.created_by,
            updated_by=order.updated_by,
            updated_at=order.updated_at,
            customer_name=order.customer_name,
            price=order.price,
            payment_method=order.payment_method,
            items_count=order.items_count,
            name_shipping=order.name_shipping,
            phone_shipping=order.phone_shipping,
            address_shipping=order.address_shipping,
            province_code_shipping=order.province_code_shipping,
            ward_code_shipping=order.ward_code_shipping,
            customer_username=order.customer_username,
            status=order.status,
            district_code_shipping=order.district_code_shipping
    ))
        session.commit()
        order = session.get(Order, order.id)
        return order

    def change_order_status_repo(self, order_id: int, next_status: EOrderStatus) -> Row:
        session: Session = SessionLocal()
        session.query(Order).filter(Order.id == order_id).update({Order.status: next_status})
        session.commit()
        rs = session.get(Order, order_id)
        return rs


