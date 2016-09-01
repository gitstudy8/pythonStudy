# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：YouTube：正则表达式学习--3、正则表达式的应用举例--抓网页
#   网址：https://www.youtube.com/watch?v=FOKmFqOQ9SQ
#   日期：2016-08-26
#   语言：Python 2.7
#---------------------------------------
# 标题：只有一个要找的内容，就用search（找到就不找了），而findall要遍历整个文档

import re
import sys
type = sys.getfilesystemencoding()

old_url='http://www.jikexueyuan.com/zhiye/course/1.html?type=3'
total_page=5
f=open('tet_Regular2.txt','r')
html=f.read()
f.close()
#
# #爬取标题
# title=re.search('<title>(.*?)</title>',html,re.S).group(1)
# 只有一个要找的内容，就用search（找到就不找了），而findall要遍历整个文档
# # print title
# # #显示乱码
# print title.decode('gbk')

#提取网址
links=re.findall('<a.*?href="(.*?)">',html,re.S)
for each in links:
    print each

#提取部分文字信息，先抓大后抓小
text_fied=re.findall('<ul>(.*?)</ul>',html,re.S)[0]
the_text=re.findall('html".*?>(.*?)</a>', text_fied, re.S)
for every_text in the_text:
    print every_text.decode('gbk')
# print  text_fied

#翻页功能
for i in range(2,total_page+1):
    new_link=re.sub('course/\d+.html?','course/%d.html?'%i,old_url,re.S)
    print new_link
