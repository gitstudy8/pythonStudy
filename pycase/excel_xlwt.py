# -*- coding: utf-8 -*-
import xlwt
#新建一个excel文件
file = xlwt.Workbook() #注意这里的Workbook首字母是大写，无语吧
# 新建一个sheet
table = file.add_sheet('sheet name',cell_overwrite_ok=True)
# 写入数据table.write(行,列,value)
table.write(0,0,'test')
file.save('demo.xls')