# -*- coding: utf-8 -*-
### Python爬虫利器六之PyQuery的用法
### http://cuiqingcai.com/2636.html
# from pyquery import PyQuery as pq
# doc = pq(filename='helloworld.html')
# print doc.html()
# print type(doc)
# li = doc('li')
# print type(li)
# print li.text()


# from pyquery import PyQuery as pq
#
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.addClass('beauty')
# print p.removeClass('hello')
# print p.css('font-size', '16px')
# print p.css({'background-color': 'yellow'})

# DOM操作
# 同样的原汁原味的 jQuery 语法

# from pyquery import PyQuery as pq
#
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')
# print p.prepend('Oh yes!')
# d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
# p.prependTo(d('#test'))
# print p
# print d
# d.empty()
# print d

# # 遍历:遍历用到 items 方法返回对象列表，或者用 lambda
# ## 不过最常用的还是 items 方法
# from pyquery import PyQuery as pq
# doc = pq(filename='helloworld.html')
# lis = doc('li')
# print '************lis************'
# print 'lis:'+lis.text()
# for li in lis.items():
#     print 'li-html--------:'+li.html()
#     print 'li-str----------:'+str(li)
#     print 'li-text--------:' + li.text()
# print '************lis.each(lambda e: e)************'
# # print lis.each(lambda e: e)

#
# ## PyQuery 本身还有网页请求功能，而且会把请求下来的网页代码转为 PyQuery 对象
# ## 感受一下，GET，POST，样样通。
# from pyquery import PyQuery as pq
# print '************get************'
# # print pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'})
# print '************post************'
# print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True)


# Ajax：
# PyQuery 同样支持 Ajax 操作，带有 get 和 post 方法，不过不常用，
# 一般我们不会用 PyQuery 来做网络请求，仅仅是用来解析。


