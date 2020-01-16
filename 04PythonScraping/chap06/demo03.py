#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import MySQLdb

conn= MySQLdb.connect(host='localhost' , user='root', passwd='123456', db ='scraping')
cur = conn.cursor()

# cur.execute("INSERT INTO urls (url, content) VALUES ('www.baidu.com', 'This is content.')")
# cur.close()
# conn.commit()
# conn.close()

cur.execute("INSERT INTO urls (url, content) VALUES ('test.com', 'test20200116')")
cur.close()
conn.commit()
conn.close()