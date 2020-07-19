import unittest
from selenium import webdriver
import time


class NewMeeting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PATH = 'C:\\Users\\tigran\\PycharmProjects\\flasknarusskom\\Testing\\webdriver\\Chrome_83\\chromedriver.exe'

        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_new_valid1(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.find_element_by_name("createmeet").click()
        self.driver.find_element_by_name("mroom").send_keys("Third")
        self.driver.find_element_by_name("employee").send_keys("Klinton")
        self.driver.find_element_by_name("stime").send_keys("08-11-2020")  # problem send time
        self.driver.find_element_by_name("etime").send_keys("08-11-2020")
        self.driver.find_element_by_name("OK").click()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == "__main__":
    unittest.main()
