from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
data = driver.find_element_by_id("jd_comments").text
print data
driver.quit()



# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
# driver.get('http://www.sogou.com/')
# data = driver.find_element_by_id('sina').text
# print data
# driver.quit()