# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：YouTube：正则表达式学习--正则表达式符号与方法
#   常用符号： . * ? ()
#   常用方法： findall,search,sub
#   网址：https://www.youtube.com/watch?v=Tt6JZfrZn0Q
#   日期：2016-08-26
#   语言：Python 2.7
#---------------------------------------
# 密码：ugsdsxxIxx123xxlovexxfdhfhuidxxyouxxhufhudh

#匹配纯数字,用\d+,当然用(.*?)也没问题
import re
a='asbj44sdkfhsf12324kdj99gkj'
b=re.findall('(\d+)',a)
# #['44', '12324', '99']
b2=re.search('(\d+)',a).group(1)
print b2

# ## compile的用法，但是不推荐这么用
# #与这个类似：# f1=findall('xx(.*?)xx',s2,S)
# import re
# s2 = 'ugsdsxxIxx123xxlovexxfdhfhuidxxyouxxhufhudh'
# pattern='xx(.*?)xx'
# new_pattern=re.compile(pattern,re.S)
# output=re.findall(new_pattern,s2)
# ['I', 'love', 'you']
# print output

# import re
# from re import findall,search,S
# #可以省掉re.，但是不推荐这么做，还是保留re.S
# s2='ugsdsxxIxx123xxlovexxfdhfhuidxxyouxxhufhudh'
# f0=search('xx(.*?)xx123xx(.*?)xx',s2).group(0)
# #xxIxx123xxlovexx
# f1=findall('xx(.*?)xx',s2,S)
# #['I', 'love', 'you']
# print f1



# import re
# s2='ugsdsxxIxx123xxlovexxfdhfhuidxxyouxxhufhudh'
#
# s='123abcssfdf123'
# #output=re.sub('123(.*?)123','123789123',s)
# #123789123
# #output=re.sub('123(.*?)123','123%d123'%888,s)
# #123888123
# output=re.sub('123(.*?)123','test',s)
# #test
# print output

# search 要跟group()
# f00=re.search('xx(.*?)xx123xx(.*?)xx',s2)
# # <_sre.SRE_Match object at 0x02586728>
#
# f0=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(0)
# #xxIxx123xxlovexx
#
# f1=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(1)
# #I
#
# f2=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
# #love
#
# #f3=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(3)
# # AttributeError: 'list' object has no attribute 'group'
#
# f4=re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# # [('I', 'love')]
#
# f5=re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# #print f5[0][0]
# # I
# print f5[0][1]
# #love



# secort_code='ugsdsxxIxxsfjhfdkhxxlovexxfdhfhuidxxyouxxhufhudh'
# s='''ugsdsxxIxxsfjhfdkhxxlove
# xxfdhfhuidxxyouxxhufhudh
# '''
# #  (.*?) 需要掌握，需要的内容，就用()包围起来，不需要的就放()外面
# #b=re.findall('xx.*?xx',secort_code)
# #   ['xxIxx', 'xxlovexx', 'xxyouxx']
# # b=re.findall('xx(.*?)xx',secort_code)
# #   ['I', 'love', 'you']
# b=re.findall('xx(.*?)xx',s,re.S)
# #re.S 让匹配内容，包含\n
# print b
# ['I', 'love\n', 'you']