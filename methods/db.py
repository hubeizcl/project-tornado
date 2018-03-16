# coding:utf-8
import pymysql.cursors

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='988728',
    db='python',
    charset='utf8'
)

cur = conn.cursor()
