# -*- coding: utf-8 -*-
#---------------------------------
#   Python编码介绍——encode和decode
####   将http://blog.chinaunix.net/uid-27838438-id-4227131.html
#   将其他编码的字符串解码（decode）成 Unicode
#   再从 Unicode编码（encode）成另一种编码
#   对 Unicode 进行编码和对 str 进行编码都是错误的
#   要在同一个文本中进行两种编码的输出等操作就必须进行编码的转换，
#   先用decode将文本原来的编码转换成Unicode，再用encode将编码转换成需要转换成的编码。
#   http://www.jb51.net/article/55759.htm
'''
python中如何避免中文是乱码
这个问题是一个具有很强操作性的问题。我这里有一个经验总结，分享一下，供参考：
首先，提倡使用utf-8编码方案，因为它跨平台不错。
经验一：在开头声明：
# -*- coding: utf-8 -*-
有朋友问我-*-有什么作用，那个就是为了好看，爱美之心人皆有，更何况程序员？当然，也可以写成：
# coding:utf-8
经验二：遇到字符（节）串，立刻转化为unicode，不要用str()，直接使用unicode()
unicode_str = unicode('中文', encoding='utf-8')
print unicode_str.encode('utf-8')
经验三：如果对文件操作，打开文件的时候，最好用codecs.open，替代open(这个后面会讲到，先放在这里)
import codecs
codecs.open('filename', encoding='utf8')
我还收集了网上的一片文章，也挺好的，推荐给看官：Python2.x的中文显示方法
最后告诉给我，如果用python3，坑爹的编码问题就不烦恼了。
'''

#---------------------------------

fp1 = open('test1.txt', 'r')
info1 = fp1.read()
# 已知是 GBK 编码，解码成 Unicode
#   内置函数 open() 打开文件时，read() 读取的是 str，读取后需要使用正确的编码格式进行 decode()
tmp = info1.decode('GBK')
# print 'tmp:',tmp

fp2 = open('test2.txt', 'w')
# 编码成 UTF-8 编码的 str
info2 = tmp.encode('UTF-8')
# print 'info2:',info2
fp2.write(info2)
fp2.close()

# 获取编码的方式：
# 判断是 s 字符串否为Unicode，如果是返回True，不是返回False
print 'tmp is unicode?'+str(isinstance(tmp, unicode))
print 'info2 is unicode?'+str(isinstance(info2, unicode))

#   下面代码可以获取系统默认编码：
import sys
print sys.getdefaultencoding()

#   经验二：遇到字符（节）串，立刻转化为unicode，不要用str()，直接使用unicode()
unicode_str = unicode('中文', encoding='utf-8')
print unicode_str.encode('utf-8')

#   经验三：如果对文件操作，打开文件的时候，最好用codecs.open，替代open(这个后面会讲到，先放在这里)
import codecs
codecs.open('filename', encoding='utf8')


#######非常重要
#####http://dashen2009.blog.51cto.com/714741/199157
# >>> urllib.quote(data)
# '%E4%B8%BD%E6%B1%9F'
# 那我们想转回去呢？
# >>> urllib.unquote('%E4%B8%BD%E6%B1%9F')
# '\xe4\xb8\xbd\xe6\xb1\x9f'