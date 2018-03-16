# coding:utf-8
import psycopg2

conn = psycopg2.connect(
    host='192.168.50.130',
    port=5432,
    user='postgres',
    passwd='postgres',
    dbname='hdsc_db',
    charset='utf8'
)

cur = conn.cursor()
