import re
import  time

from Library.excel_lib import ReadExcel
from Library.configuration import Configuration
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class HotelModule:
    obj_1 = ReadExcel()
    locator_hotel = obj_1.read_locator(Configuration.HOTEL_MODULE_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver
        self.action_obj = ActionChains(driver)

    def click_hotel_btn(self):
        locator = self.locator_hotel["hotel_link"]
        self.driver.find_element(*locator).click()

    def click_india_radio_btn(self):
        locator = self.locator_hotel["india_radio_btn"]
        self.driver.find_element(*locator).click()

    def click_international_radio_btn(self):
        locator = self.locator_hotel["international_radio_btn"]
        self.driver.find_element(*locator).click()

    def enter_where_txt(self,where_text):
        locator = self.locator_hotel["where_txt"]
        self.driver.find_element(*locator).send_keys(where_text)
        time.sleep(2)
        self.action_obj.key_down(Keys.ARROW_DOWN).perform()
        self.action_obj.key_down(Keys.ENTER).perform()

    def select_dates(self):
        locator = self.locator_hotel["check_in_calender"]
        self.driver.find_element(*locator).click()
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["check_in_date"]
        self.driver.find_element(*locator).click()
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["check_out_date"]
        self.driver.find_element(*locator).click()

    def select_guest_and_rooms(self):
        loctor = self.locator_hotel["enter_guest_&_rooms"]
        self.driver.find_element(*loctor).click()
        # time.sleep(1)
        self.driver.implicitly_wait(10)
        loctor = self.locator_hotel["decrease_adults"]
        self.driver.find_element(*loctor).click()
        # time.sleep(1)
        self.driver.implicitly_wait(10)
        loctor = self.locator_hotel["click_on_done"]
        self.driver.find_element(*loctor).click()

    def click_on_search(self):
        locator = self.locator_hotel["search_btn"]
        self.driver.find_element(*locator).click()


    def select_hotel(self,hotel_name):
        time.sleep(3)
        locator = self.locator_hotel["search_property_btn"]
        self.driver.find_element(*locator).send_keys(hotel_name)
        time.sleep(2)
        self.action_obj.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        locator = self.locator_hotel["click_hotel"]
        self.driver.find_element(*locator).click()


    def select_room(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["click_on_room_options"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
        locator = self.locator_hotel["select_room"]
        self.driver.find_element(*locator).click()


    def select_title(self):
        locator = self.locator_hotel["click_title"]
        list_box1 = self.driver.find_element(*locator)
        s_obj = Select(list_box1)
        s_obj.select_by_visible_text("Mr")
        time.sleep(1)

    def enter_first_name(self,first_name):
        locator = self.locator_hotel["enter_first_name"]
        result = re.findall('[a-zA-Z]',first_name)
        assert result, "invalid first_name"
        self.driver.find_element(*locator).send_keys(first_name)

    def enter_last_name(self,last_name):
        locator = self.locator_hotel["enter_last_name"]
        result = re.findall('[a-zA-Z]',last_name)
        assert result, "invalid last_name"
        self.driver.find_element(*locator).send_keys(last_name)

    def enter_email_id(self,email_id):
        locator = self.locator_hotel["enter_email"]
        result = re.findall(r"\w+@gmail\.com",email_id)
        assert result != [] , "invalid email_id"
        self.driver.find_element(*locator).send_keys(email_id)

    def select_countrycode(self):
        locator = self.locator_hotel["enter_country_code"]
        list_box2 = self.driver.find_element(*locator)
        s_obj = Select(list_box2)
        # s_obj.select_by_visible_text("+247 Ascension Island")
        s_obj.select_by_visible_text("+91 India")
        time.sleep(1)

    def enter_mb_num(self,mb_num):
        if isinstance(mb_num,float):
            mb_num = str(int(mb_num))
        assert len(mb_num) == 10 , "invaild mb_num"
        locator = self.locator_hotel["enter_mb_num"]
        self.driver.find_element(*locator).send_keys(mb_num)

    def proceed_to_payment(self):
        locator = self.locator_hotel["proceed_to_payment"]
        self.driver.find_element(*locator).click()
