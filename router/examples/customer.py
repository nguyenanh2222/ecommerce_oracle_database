import string
import random
def username(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

customer_op1 = {"opt_1": {"value": {"created_at": "2022-08-01 15:43:39.000",
                                    "created_by": "customer",
                                    "updated_at": "2022-08-01 15:43:39.000",
                                    "updated_by": "customer",
                                    "phone": "033578982",
                                    "address": "quan 8",
                                    "province_code": " 78",
                                    "district_code": "468",
                                    "ward_code": "234",
                                    "username": username(),
                                    "password": "123456",
                                    "firstname": "anh",
                                    "lastname": "viet",
}}}
