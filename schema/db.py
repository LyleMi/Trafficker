#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb


class DB(object):

    def __init__(self, opts):
        self.conn = MySQLdb.connect(
            host=opts["host"],
            user=opts["user"],
            passwd=opts["pwd"],
            db=opts["db"],
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def insert(self, pcapName, packetNum, data):
        sql = "INSERT INTO `flow` (`pcapName`, `packetNum`, `data`) VALUES (%s, %s, %s)"
        self.cur.execute(sql, [pcapName, packetNum, data])
        self.conn.commit()

    def insertMul(self, data):
        sql = "INSERT INTO `flow` (`pcapName`, `packetNum`, `data`) VALUES (%s, %s, %s)"
        self.cur.executemany(sql, data)
        self.conn.commit()

    def select(self, data, pcapName=""):
        sql = "SELECT pcapName, packetNum FROM flow WHERE data like '%%%s%%'" % data.replace(
            "'", "\\'")
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()

if __name__ == '__main__':
    opts = {
        "host": "localhost",
        "user": "traffic",
        "pwd": "password",
        "db": "traffic"
    }
    db = DB(opts)
    m = []
    for i in range(10):
        m.append(["1.pcap", i, "data%d" % i])
    db.insertMul(m)
    # db.insert("1.pcap", 1, "data\xff\x22\x00\x66")
    # db.insert("1.pcap", 1, "data'\xff\x22\x00\x66")
    print db.select("data")
    # print db.select("\xff")
