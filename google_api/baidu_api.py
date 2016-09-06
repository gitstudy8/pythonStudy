# coding:utf-8

import xlrd
import xlwt
import requests
import urllib
import math
import re
import chardet

pattern_x = re.compile(r'"x":(".+?")')
pattern_y = re.compile(r'"y":(".+?")')


# 墨卡托转经纬度
# http://www.cnblogs.com/liongis/archive/2012/06/13/2548061.html
def mercator2wgs84(mercator):
    # key1=mercator.keys()[0]
    # key2=mercator.keys()[1]
    point_x = mercator[0]
    point_y = mercator[1]
    print 'point_x',point_x,point_y
    x = point_x / 20037508.3427892 * 180
    y = point_y / 20037508.3427892 * 180
    y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180)) - math.pi / 2)
    print 'x:', x, 'y:', y
    return (x, y)


def get_mercator(addr):
    # print '------' + addr
    quote_addr = urllib.quote(addr.encode('utf8'))
    city = urllib.quote(u'齐齐哈尔市龙'.encode('utf8'))
    province = urllib.quote(u'黑龙江省'.encode('utf8'))
    if quote_addr.startswith(city) or quote_addr.startswith(province):
        pass
    else:
        # print 'quote_addr1',quote_addr
        # print 'type:', type(quote_addr)
        # print 'type1:',chardet.detect(quote_addr)
        # # quote_addr:<type 'str'>---ascii
        # aaa=unicode(quote_addr, 'gbk')
        # # print 'type2:',chardet.detect(aaa)
        # print 'aaaa:'+urllib.unquote(quote_addr)
        # ## 成功还原回去
        # quote_addr = city + quote_addr
        print 'quote_addr2', urllib.unquote(quote_addr)
    s = urllib.quote(u'北京市'.encode('utf8'))
    api_addr = "http://api.map.baidu.com/?qt=gc&wd=%s&cn=%s&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk62300" % (quote_addr , s)
    req = requests.get(api_addr)
    print 'api_addr',api_addr
    content = req.content.encode('utf8')
    print '--1111-----------------'
    print content
    print '--2222---------------------'
    x = re.findall(pattern_x, content)
    y = re.findall(pattern_y, content)
    if x:
        x = x[0]
        y = y[0]
        x = x[1:-1]
        y = y[1:-1]
        x = float(x)
        y = float(y)
        location = (x, y)
    else:
        location = ()
    return location


def run():
    data = xlrd.open_workbook('Book2.xlsx')
    rtable = data.sheets()[0]
    nrows = rtable.nrows
    values = rtable.col_values(0)

    workbook = xlwt.Workbook()
    wtable = workbook.add_sheet('data', cell_overwrite_ok=True)
    row = 0
    for value in values:
        mercator = get_mercator(value)
        if mercator:
            wgs = mercator2wgs84(mercator)
        else:
            wgs = ('NotFound', 'NotFound')
        print "%s,%s,%s" % (value, wgs[0], wgs[1])
        wtable.write(row, 0, value)
        wtable.write(row, 1, wgs[0])
        wtable.write(row, 2, wgs[1])
        row = row + 1

    workbook.save('data.xls')


if __name__ == '__main__':
    run()