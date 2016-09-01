# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：山东大学爬虫
#  -- 改成：test.fugangzs.com.cn
#   版本：0.1  
#   作者：why  
#   日期：2013-07-12  
#   语言：Python 2.7  
#   操作：输入学号和密码  
#   功能：输出成绩的加权平均值也就是绩点  
#---------------------------------------  
  
import urllib    
import urllib2  
import cookielib  
  
cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
  
#需要POST的数据#  
postdata=urllib.urlencode({    
    'UserID':'zhangcheng',    
    'Password':'beijlg486'    
})  
  
#自定义一个请求#  
req = urllib2.Request(    
    url = 'http://test.fugangzs.com.cn/Admin_ChkLogin.asp',    
    data = postdata  
)  
  
#访问该链接#  
result = opener.open(req)  
  
#打印返回的内容#  
print result.read()  
  
#打印cookie的值
#print '-------------'+str(cookie)
for item in cookie:    
    print 'Cookie：Name = '+item.name    
    print 'Cookie：Value = '+item.value  
  
      
#访问该链接#  
result = opener.open('http://test.fugangzs.com.cn/Yaohuo_List4.asp')  
  
#打印返回的内容#  
print result.read()  
