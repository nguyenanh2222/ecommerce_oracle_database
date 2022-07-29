from typing import List

import pandas as pd

from model import Order
from repo.order import OrderRepo
from schema import OrderReq


class Check():
    def search_shipping_code(self, data: List, shipping_code: str):
        left = 0
        right = len(data) - 1
        is_found: int
        while (left <= right):
            mid = (left + right) // 2
            if data[mid] == shipping_code:
                return shipping_code
            if data[mid] > shipping_code:
                right = mid - 1
            else:
                left = mid + 1
            is_found = data[mid]
            if is_found != data[mid]:
                return
if __name__=="__main__":

    check = Check()
    data_district = pd.read_excel('district_29_07.xls', dtype=int)['Mã']
    data_province = pd.read_excel('./province_29_07.xls', dtype=int)['Mã']
    data_ward = pd.read_excel('./ward_29_07.xls', dtype=int)['Mã']
    check.search_shipping_code(data_district, '001')

