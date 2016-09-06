# coding=utf-8
## ## 数据抓取的艺术（一）：Selenium+Phantomjs数据抓取环境配置
## http://blog.chinaunix.net/uid-22414998-id-3692113.html


from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=find_element_by_id&rsv_pq=9d649aca00042b2c&rsv_t=a181vl3FtiZy7pD8F1jVjokLF7lNNLSOylE%2BtG2QmGjBolkyrWYXYMNkjZk&rqlang=cn&rsv_enter=1&rsv_sug3=2&rsv_n=2')
data = driver.find_element_by_id('su').text
print data