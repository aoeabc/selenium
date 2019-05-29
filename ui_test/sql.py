import pymysql

#  连接数据库
def connectSql():
    #  连接数据库
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='edu')
    #   获取游标（实例化）
    c=con.cursor()
    #    执行sql
    c.execute('select * from xsmart_users where username="18625426325"')
    #    查看返回结果
    data=c.fetchone()
    print(data)
    # c.execute('delete from xsmart_users where username="18625426325"')
    # print(data)
    c.execute('select * from xsmart_users where username="18625426325"')
    #    查看返回结果
    data=c.fetchone()
    print(data)

connectSql()