# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2019/3/18


import pymysql

# 利用PyMySQL查询数据库


# 创建数据库连接
connect = pymysql.connect(host='127.0.0.1', user='root', password='19940415', port=3306, db='codemao_db')
cursor = connect.cursor()
result = cursor.execute('select * from wood_book')
print(cursor.fetchall())
connect.close()