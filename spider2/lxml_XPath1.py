# -*- coding: utf-8 -*-
from lxml import etree
html = etree.parse('helloworld.html')
# print type(html)
# result = html.xpath('//li')
# print result
# print len(result)
# print type(result)
# print type(result[0])

# ## （2）获取 <li> 标签的所有 class
# result = html.xpath('//li/@class')
# print result

# result = html.xpath('//li/a[@href="link1.html"]')
# print result
# #[<Element a at 0x10ffaae18>]

result = html.xpath('//*[@class="bold"]')
print result[0].tag