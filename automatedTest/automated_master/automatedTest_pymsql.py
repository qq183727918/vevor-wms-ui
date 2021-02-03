"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/1 14:10
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : automatedtest_test.py
@Software  : PyCharm
"""
import pymysql

def foo2():

    con = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='automatedtest',
        port=3306,
    )

    cur = con.cursor()

    sql = "select * from automatedtest;"

    cur.execute(sql)

    con.commit()

    student = cur.fetchall()

    print(student)

    con.close()


if __name__ == '__main__':
    foo2()
