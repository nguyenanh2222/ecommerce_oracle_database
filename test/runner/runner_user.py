from decimal import Decimal
from test.executor.admin import AdminAPIExecutor
from status import EOrderStatus
from test.executor.user import UserAPIExecutor


class TestSimpleCaseCustomer:
    executor_user = UserAPIExecutor()
