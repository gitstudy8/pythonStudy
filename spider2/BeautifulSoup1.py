# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#### http://cuiqingcai.com/1319.html
#### 熟练掌握了 Beautiful Soup，一定会给你带来太多方便


import re
import lxml

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story Elsie</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">elsie<!-- elsie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">test...</p>
"""
soup = BeautifulSoup(html)
# print soup.prettify()

# print soup.p['class']
# print soup.p['name']
# print soup.p.get('name')
#
# soup.p['class']='newclass--live'
# print soup.p['class']
# print soup.p.get('class')
#
# print soup.p
#
# # （2）NavigableString
# print soup.p.string
# print type(soup.p.string)

# #  （3）BeautifulSoup
# print type(soup.name)
# #<type 'unicode'>
# print soup.name
# # [document]
# print soup.attrs
# #{} 空字典


# #   #（4）Comment
# # print 'soup.a='+str(soup.a)
# print 'soup.a.string='+soup.a.string
# # print 'soup.a.string='+type(soup.a.string)
# print type(soup.p.string)
# print type(soup.a.string)

# # 6. 遍历文档树
# # （1）直接子节点,要点：.contents  .children  属性
# print soup.head.contents
# #[<title>The Dormouse's story</title>]
##输出方式为列表，我们可以用列表索引来获取它的某一个元素
# print soup.head.contents[0]
# #<title>The Dormouse's story</title>

# # .children
# # 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
# # 我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象
# print soup.head.childern
# #<listiterator object at 0x7f71457f5710>
#
# for child in  soup.body.children:
#     print child

# #  （2）所有子孙节点
# # 知识点：.descendants 属性
# #.contents 和 .children 属性仅包含tag的直接子节点，.
# # descendants 属性可以对所有tag的子孙节点进行递归循环，
# # 和 children类似，我们也需要遍历获取其中的内容。
# for child in soup.descendants:
#     print child

# # （3）节点内容
# # 知识点：.string
# #通俗点说就是：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
# # 如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。
# print soup.head.string
# #The Dormouse's story
# print soup.title.string
# # #The Dormouse's story
# # #如果tag包含了多个子节点,tag就无法确定，
# # string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
# print soup.html.string
# # None

# # （4）多个内容
# # 知识点： .strings  .stripped_strings
# for string in soup.strings:
#     print(repr(string))
# ## str()一般是将数值转成字符串。
# ## repr()是将一个对象转成字符串显示，注意只是显示用，有些对象转成字符串没有直接的意思。
# ## 如list,dict使用str()是无效的，但使用repr可以
# ## 函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式
# # u"The Dormouse's story"
# # u'\n'
# # u'\n'
# # u"The Dormouse's story"
# # u'\n'
# # u'Once upon a time there were three little sisters; and their names were\n'
# # u',\n'
# # u'Lacie'
# # u' and\n'
# # u'Tillie'
# # u';\nand they lived at the bottom of a well.'
# # u'\n'
# # u'test...'
# # u'\n'

# ## .stripped_strings
# ## .stripped_strings 可以去除多余空白内容
# for string in soup.stripped_strings:
#     print(repr(string))

# ##（5）父节点   知识点： .parent 属性
# p = soup.p
# print p.parent.name
# #body
#
# content = soup.head.title.string
# print content.parent.name
# #title


# ##（6）全部父节点:通过元素的 .parents 属性可以递归得到元素的所有父辈节点
# content = soup.head.title.string
# # print content
# ## The Dormouse's story
# for parent in  content.parents:
#     print parent.name
# # title
# # head
# # html
# # [document]

# ## （7）兄弟节点:.next_sibling  .previous_sibling 属性
# # 兄弟节点可以理解为和本节点处在统一级的节点，
# # .next_sibling 属性获取了该节点的下一个兄弟节点，
# # .previous_sibling 则与之相反，如果节点不存在，则返回 None
# ## 注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
# ## 因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
# print soup.p.next_sibling
# #       实际该处为空白
# print soup.p.prev_sibling
# #None   没有前一个兄弟节点，返回 None
# print soup.p.next_sibling.next_sibling
# #<p class="story">Once upon a time there were three little sisters; and their names were
# #<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
# #<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# #<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# #and they lived at the bottom of a well.</p>
# #下一个节点的下一个兄弟节点是我们可以看到的节点


# ## （8）全部兄弟节点.next_siblings  .previous_siblings 属性
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))
#     # u',\n'
#     # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
#     # u' and\n'
#     # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
#     # u'; and they lived at the bottom of a well.'
#     # None

### 以下略掉一些，参考：http://cuiqingcai.com/1319.html


# ## 7.搜索文档树
# ## （1）find_all( name , attrs , recursive , text , **kwargs )
# ## find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
## A.传字符串
# # print soup.find_all('b')
# # # [<b>The Dormouse's story</b>]
# print soup.find_all('a')
# #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# ## B.传正则表达式
#
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# # body
# # b


# ##  C.传列表:将与列表中任一元素匹配的内容返回.
# print soup.find_all(["p", "b"])
# # [<b>The Dormouse's story</b>,
# #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# ## D.传 True,True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
# for tag in soup.find_all(True):
#     print(tag.name)
# # html
# # head
# # title
# # body
# # p
# # b
# # p
# # a
# # a


# ##  E.传方法
# ##  如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数
# ##  如果这个方法返回 True 表示当前元素匹配并且被找到
# ##  下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# soup.find_all(has_class_but_no_id)
# # [<p class="title"><b>The Dormouse's story</b></p>,
# #  <p class="story">Once upon a time there were...</p>,
# #  <p class="story">...</p>]

# ##   2）keyword 参数
# print soup.find_all(id='link2')
# # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# soup.find_all(href=re.compile("elsie"))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

# ## 在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以
# soup.find_all("a", class_="sister")
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# ##  有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(data-foo="value")
# # SyntaxError: keyword can't be an expression


# ## 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
# data_soup.find_all(attrs={"data-foo": "value"})
# # [<div data-foo="value">foo!</div>]

#
# ##  3）text 参数
# print soup.find_all(text="Elsie")
# # [u'Elsie']
#
# print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# # [u'Elsie', u'Lacie', u'Tillie']
#
# print soup.find_all(text=re.compile("Dormouse"))
# # [u"The Dormouse's story", u"The Dormouse's story"]


# print soup.select('title')
# #[<title>The Dormouse's story</title>]

# print soup.select('.sister')
# print soup.select('#link1')
# print soup.select('p #link1')

# ## 直接子标签查找
# print soup.select("head > title")
# #[<title>The Dormouse's story</title>]

## （5）属性查找
## 属性需要用中括号括起来，注意属性和标签属于同一节点，
## 所以中间不能加空格，否则会无法匹配到。

# print soup.select('a[class="sister"]')
# # print soup.select('a[id="link1"]')
# #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# print soup.select('a[href="http://example.com/elsie"]')
# #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

## 以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，
## 然后用 get_text() 方法来获取它的内容。


soup = BeautifulSoup(html, 'lxml')
print type(soup.select('p'))
print soup.select('p')[0].get_text()
print '---------------'
for title in soup.select('p'):
    print title.get_text()
