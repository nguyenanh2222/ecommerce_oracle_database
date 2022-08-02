from enum import Enum


class EOrderStatus(str, Enum):
    PENDING = 'PENDING'
    CANCELLED = 'CANCELLED'
    SHIPPING = 'SHIPPING'
    COMPLETED = 'COMPLETED'


class ESkuStatus(str, Enum):
    ACTIVATED = "ACTIVATE"
    DISABLE = "DISABLE"
