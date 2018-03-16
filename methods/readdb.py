# coding:utf-8

from methods.db import *


def select_table(table, column, condition, value):
    sql = "select " + column + " from ec." + table + " where " + condition + "=" + value
    cur.execute(sql)
    return cur.fetchall()


def select_table(table, column):
    sql = "select " + column + "  from  ec." + table
    cur.execute()
    return cur.fetchall()
