import time

import pytest
import datetime
from Library.configuration import Configuration
from Library.excel_lib import ReadExcel
from POM.hotel_module import HotelModule


class TestHotelModule:
    obj = ReadExcel()
    data = obj.read_test_data(Configuration.HOTEL_MODULE_TESTDATA_SHEET)

    @pytest.mark.parametrize("where_text, hotel_name, first_name, last_name, email_id, mb_num", data)
    def test_hotel_module(self,init_driver, where_text, hotel_name,first_name, last_name, email_id, mb_num):
        driver = init_driver
        try:
            hm = HotelModule(driver)
            hm.click_hotel_btn()
            hm.click_india_radio_btn()
            hm.enter_where_txt(where_text)
            hm.select_dates()
            hm.select_guest_and_rooms()
            hm.click_on_search()
            hm.select_hotel(hotel_name)
            hm.select_room()
            hm.select_title()
            hm.enter_first_name(first_name)
            hm.enter_last_name(last_name)
            hm.enter_email_id(email_id)
            hm.select_countrycode()
            hm.enter_mb_num(mb_num)
            hm.proceed_to_payment()


        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOTS_PATH + name)
            raise err_msg













