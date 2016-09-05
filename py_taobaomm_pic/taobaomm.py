# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：本地视频--Python培训之美眉图片下载爬虫--小甲鱼
#   网址：
#   日期：2016-08-29
#   语言：Python 2.7
#---------------------------------------
import urllib2
import urllib
import re
import requests


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # print path + ' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + ' 目录已存在'
        return False


# # 定义要创建的目录
#mkpath = "d:\\qttc\\web\\"
# # 调用函数
# mkdir(mkpath)



mmurl="https://mm.taobao.com/json/request_top_list.htm?type=0&page="
i=0
ph=-1
temp='''<img src="'''
while i<20:
    url=mmurl+str(i)
    # print url
    up=urllib2.urlopen(url)
    cont=up.read().decode("gbk")
    # print '-------11111------------------'
    #print cont
    head="<img src="
    tail=".jpg"
    ph=cont.find(head)
    pj=cont.find(tail,ph+1)
    # print 'https:'+cont[ph+len(temp):pj+len(tail)]
    # print '--------2222------------'
    # ahref='''<a href="'''
    # target='''target="'''
    # pa=cont.find(ahref)
    # pb=cont.find(target,pa)
    # print pa,pb
    # print  'https:'+cont[pa+len(ahref):pb-2]
#以上是，获取图片上的连接，但是进不去，换成下面获取名字的连接

#######################################################
    ahref2='''model_card.htm?user_id='''
    target2='''" target='''
    pa2=cont.find(ahref2)
    pb2=cont.find(target2,pa2)
    # print pa2,pb2
    # print  cont[pa2+len(ahref2):pb2]
    #获取编号
    #modelurl='https:'+cont[pa2+len(ahref2):pb2]+'&is_coment=false'
    # modelurl='https://mm.taobao.com/self/model_info.htm?user_id='+cont[pa2+len(ahref2):pb2]+'&is_coment=false'
    #modelurl='https://mm.taobao.com/self/model_info.htm?user_id=687471686&is_coment=false'
#查看源代码，再一次转换地址：url:"/self/info/model_info_show.htm?user_id="+687471686
#直接修改添加，结合id（是放到代码里面的，JavaScript调用，框架？）
    user_id=cont[pa2+len(ahref2):pb2]
    modelurl = 'https://mm.taobao.com/self/info/model_info_show.htm?user_id='+user_id
    # print modelurl
    mup=urllib2.urlopen(modelurl)
    mcont=mup.read().decode("gbk")
    # print '-----------3333------------'
    # print modelurl
    # print mcont

#这里获取的只是中间地址，淘宝第二次跳转（截取--域名地址://mm.taobao.com/tyy6160）
#尝试用第二种方法，re.findall()--还是选search()，找一次就结束
    # print '------------444---------'
    #yuming_url = re.findall('<span>(.*?)</span>', mcont, re.S)
    #yuming_url = 'https:'+re.search('mm-p-domain-info.*?<span>(.*?)</span>', mcont, re.S).group(1)
    mod_id1=re.search('mm-p-domain-info.*?<span>(.*?)</span>', mcont, re.S).group(1)
    yuming_url = 'https:'+mod_id1
    ###中文“域名地址:”去搜索，老是找不到     # < label > 域名地址: < / label > < span >
    # nam=re.search('</label><span>(.*?)</span>', mcont, re.S).group(1)
    mup2=urllib2.urlopen(yuming_url)
    mcont2=mup2.read().decode("gbk")
    #yuming_url='https://mm.taobao.com/menyastrong'
    print yuming_url
    # print mcont2
#总算找到淘女郎照片真正网址
#######################################################

#####下面寻找里面的照片################################################
    ################这一段代码，可以了，但是怎么获取批量的？还是改用re.findall()#############
    # # print '-----------555---------'
    # #ahref3 = '''margin: 10.0px;" src="'''
    # #不行，有的格式变了margin: 10.0px;float: none;" src="
    # ahref3 = ''';" src="'''
    # target3 = '''>'''
    # ###如果觉得太长了，也可以做2次查找mcont2[pa4:]后面留空，表示到最后一个字符
    # pa4 = mcont2.find(ahref3)
    # if  pa4==-1 :
    #     print  '该淘女郎没有图片！'
    # else:
    #     pb4 = mcont2.find(target3, pa4-1)
    #     print 'pa4='+str(pa4), 'pb4='+str(pb4)
    #     print  'https:'+mcont2[pa4:pb4-1]
    ################这一段代码，可以了，但是怎么获取批量的？，还是改用re.findall()#############
    #########提取照片信息，先抓大后抓小
    pic_text = re.findall(';" src="(.*?)"/>', mcont2, re.S)
    j=0
    k= str(user_id)
    mkdir(k)
    for each in pic_text:
        print 'now downloading:' + 'https:'+each
        #######方法1--成功###################
        # pic = requests.get('https:'+each)
        # p=k+'\\' +str(user_id)+'-'+str(j+1)  + '.jpg'
        # # print p
        # fp = open(p, 'wb')
        # fp.write(pic.content)
        #######方法1--成功###################
        #######方法2 urllib.urlretrieve(url,路径)--成功###################
        urllib.urlretrieve('https:'+each,k+'\\' +str(user_id)+'-'+str(j+1)+'.jpg')
        ###但是，加不进目录路径？
        #######方法2 urllib.urlretrieve(url,路径)--成功###################

        #######方法2###################
        if j==99:
            break
        j += 1

        #####第2层循环#############################
            # modelurl_pic = 'https:'+mcont2[pa4+len(ahref3):pb4-1]
    # mup4 = urllib2.urlopen(modelurl_pic)
    # mcont4 = mup4.read()
    # print mcont4
#####第一层循环#############################
    i+=1
