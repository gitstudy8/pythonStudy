# -*- coding: utf-8 -*-
import requests
import json
# payload={'ie':'utf-8','wd':'python'}
# headers = {'content-type': 'application/json'}
# # r = requests.get("https://www.baidu.com/s", params=payload, headers=headers)
# # r = requests.get("https://www.baidu.com/s", params=payload)
# #https://www.baidu.com/s?ie=utf-8&wd=python
# r=requests.post("http://httpbin.org/post",data=payload)
# print r.text
####有时候我们需要传送的信息不是表单形式的，
# 需要我们传JSON格式的数据过去，
# 所以我们可以用 json.dumps() 方法把表单数据序列化。
# url='http://httpbin.org/post'
# payload={'ie':'utf-8','some':'data'}
# r=requests.post(url,data=json.dumps(payload))
# print r.text
#### json.dumps()   end#############

#  如果想要上传文件，那么直接用 file 参数即可#################
# url='http://httpbin.org/post'
# files={'file':open('a.json','rb')}
# r=requests.post(url,files=files)
# print r.text
##end####################

#   保持一个持久的会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
# #   在这里我们请求了两次，一次是设置 cookies，一次是获得 cookies
# print(r.text)

#   那么既然会话是一个全局的变量，那么我们肯定可以用来全局的配置了。
# s = requests.Session()
# s.headers.update({'x-test': 'true'})
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print r.text
#   通过 s.headers.update 方法设置了 headers 的变量。
#   然后我们又在请求中设置了一个 headers，那么会出现什么结果？
#   很简单，两个变量都传送过去了

# #   Requests可以为HTTPS请求验证SSL证书,你可以使用 verify 参数
# # r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
# # r = requests.get('https://baidu.com', verify=True)
# r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
# # r=requests.get('http://www.fugangzs.com.cn/index.asp')
# print r.text
#
# ### 设置代理服务器
# proxies = {
#   "https": "http://41.118.132.69:4433"
# }
# # r = requests.post("http://httpbin.org/post", proxies=proxies)
# r = requests.post("http://www.fugangzs.com.cn", proxies=proxies)
# print r.text

# ## 也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理
# export HTTP_PROXY="http://10.10.1.10:3128"
# export HTTPS_PROXY="http://10.10.1.10:1080"
# ## 也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理
