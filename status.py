from enum import Enum


class EOrderStatus(str, Enum):
    PENDING = 'PENDING'
    CANCELLED = 'CANCELLED'
    SHIPPING = 'SHIPPING'
    COMPLETED = 'COMPLETED'

