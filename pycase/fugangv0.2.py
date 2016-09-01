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
#    http://blog.csdn.net/pleasecallmewhy/article/details/9305229
#---------------------------------------  
  
import urllib    
import urllib2  
import cookielib  
import re  
  
class SDU_Spider:    
    # 申明相关的属性    
    def __init__(self):      
        self.loginUrl = 'http://test.fugangzs.com.cn/Admin_ChkLogin.asp'   # 登录的url  
        self.resultUrl = 'http://test.fugangzs.com.cn/Yaohuo_List4.asp' # 显示成绩的url  
        self.cookieJar = cookielib.CookieJar()                                      # 初始化一个CookieJar来处理Cookie的信息  
        self.postdata=urllib.urlencode({'UserID':'zhangcheng', 'Password':'beijlg486'})     # POST的数据  
##        self.weights = []   #存储权重，也就是学分  
##        self.points = []    #存储分数，也就是成绩
        self.weights = []   #专卖店  
        self.points = []    #总金额  
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))  
  
    def sdu_init(self):  
        # 初始化链接并且获取cookie  
        myRequest = urllib2.Request(url = self.loginUrl,data = self.postdata)   # 自定义一个请求  
        result = self.opener.open(myRequest)            # 访问登录页面，获取到必须的cookie的值  
        result = self.opener.open(self.resultUrl)       # 访问成绩页面，获得成绩的数据  
        # 打印返回的内容  
        #print result.read()  
        self.deal_data(result.read().decode('gbk'))  
        self.print_data(self.weights);  
        self.print_data(self.points);
        #获取内容
        #print self.print_data(self.weights) 
  
    # 将内容从页面代码中抠出来    
    def deal_data(self,myPage):    
        #myItems = re.findall('<TR>.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?</TR>',myPage,re.S)     #获取到学分
        myItems = re.findall('<td  align="left">￥(.*?)</td>',myPage,re.S) 

        for item in myItems:  
            self.weights.append(item[0].encode('gbk'))  
            self.points.append(item[1].encode('gbk'))  
  
              
    # 将内容从页面代码中抠出来  
    def print_data(self,items):    
        for item in items:    
            print item  
              
#调用    
mySpider = SDU_Spider()    
mySpider.sdu_init()    
