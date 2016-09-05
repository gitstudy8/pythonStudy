# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
# driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
# data = driver.find_element_by_id("jd_comments").text
# print data
# driver.quit()
#


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()