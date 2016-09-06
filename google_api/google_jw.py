# -*- coding: utf-8 -*-
# ---------------------------------------
# 仿照查天气，做googlemap的api读取
# http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000176&itemidx=1&sign=42881919403184543ad80cb756f279ab
# http://www.weather.com.cn/data/cityinfo/101010100.html
# http://maps.google.com/maps/api/geocode/json?address=地点名称&sensor=false
# ---------------------------------------

import urllib2
import json
# from city import city

cityname='beijing'
# url='http://maps.google.com/maps/api/geocode/json?address='+cityname+'&sensor=false'
# # print url
# web=urllib2.urlopen(url)
# content=web.read()
# print content

# citycode = city.get(cityname)
citycode=str(cityname)
# if citycode:
#    # url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
#    url = 'http://maps.google.com/maps/api/geocode/json?address=' + cityname + '&sensor=false'
#    # print url
#    # content = urllib2.urlopen(url).read()
#    # print content


f = file('country2.py')
# data = f.read()
data = f.readlines()
print data[0]
f.close()


for countryname in data:
    print countryname
    if countryname:
        # url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        #url = 'http://maps.google.com/maps/api/geocode/json?address=' + countryname + '&sensor=false'
        url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + countryname + '&sensor=false&language=zh-CN'
        print url
        # print urllib2.urlopen(url).read()

