# -*- coding:utf-8 -*-
import xlrd
# 打开excel
data = xlrd.open_workbook('sample.xls') #注意这里的workbook首字母是小写
# 查看文件中包含sheet的名称
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
print nrows,ncols

# # 获取整行和整列的值（数组）
# for rownum in range(table.nrows):
#     print table.row_values(rownum)
# #单元格
# print table.cell(0,4).value
# #分别使用行列索引
# print  table.row(0)[3].value
# print  table.col(0)[0].value
#简单的写入
row = 0
col = 0
ctype = 1
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
value = 'lixiaoluo'
xf = 0 # 扩展的格式化 (默认是0)
table.put_cell(row,col,ctype, value, xf)
print '-----------'
print table.cell(0,0)
print table.cell(0,0).value