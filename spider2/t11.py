#coding=utf-8
# 链接：https://www.zhihu.com/question/40547676/answer/87214437
import urllib2
import urllib
import json

def getLl(address):
	addressAPI = "http://api.map.baidu.com/geocoder/v2/?address="+ address+"&output=json&ak=B9DG2Fxl5KjlUymnS1aapUWL&callback=showLocation"
	dirtyJson = urllib2.urlopen(addressAPI).read()
	dirtyJson = dirtyJson[27:-1] #注[1]
	jsonOfAddress = json.loads(dirtyJson)
    # print dirtyJson
    # print dirtyJson
    # print  str(jsonOfAddress)
	return (str)('%.6f' %(jsonOfAddress["result"]["location"]["lng"]))[:]+","+(str)('%.6f' %(jsonOfAddress["result"]["location"]["lat"]))

def get_google(address):
    addressAPI = "http://maps.google.com/maps/api/geocode/json?address=" + address + "& sensor = false"
    dirtyJson = urllib2.urlopen(addressAPI).read()
    print dirtyJson
    # dirtyJson = dirtyJson[27:-1]  # 注[1]
    # jsonOfAddress = json.loads(dirtyJson)
    return    jsonOfAddress



# address = raw_input("Enter Address:")
# address = urllib.quote_plus((address.decode("gb2312")).encode("utf-8")) #注[2]

# print getLl(address)
print getLl('北京')
# print get_google('北京')