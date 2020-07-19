import unittest
from selenium import webdriver


class MeetingSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PATH = "C:\\Users\\tigran\\PycharmProjects\\flasknarusskom\\Testing\\webdriver\\Chrome_83\\chromedriver.exe"
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_emp1(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element_by_name("search_string").send_keys("A")
        self.driver.find_element_by_name("searchbutton").click()
        assert "Search result" in self.driver.title

    def test_search_emp2(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element_by_name("search_string").send_keys("ba")
        self.driver.find_element_by_name("searchbutton").click()
        assert "Search result" in self.driver.title

    def test_search_emp3(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element_by_name("search_string").send_keys("ko")
        self.driver.find_element_by_name("searchbutton").click()
        assert "Search result" in self.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == "__main__":
    unittest.main()
