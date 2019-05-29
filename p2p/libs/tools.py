import requests
import os
import pymysql
import unittest

class BaseRequest():
    def get_request(self,method='post',data='',url='',*args,**kwargs):
        '''
        封装request方法
        :param method: 请求方式
        :param data:
        :param url:
        :param args:
        :param kwargs:
        :return:
        '''
        try:
            if os.path.isfile(data):
                res = requests.request(method=method, files=data, url=url,*args,**kwargs)
        except TypeError as e:
            res=requests.request(method=method,data=data,url=url,*args,**kwargs)
        except BaseException as e:
            print(e)

        return res



def connectSql(sql='',user='root',password='root',host='localhost',port=3306,db='p2p'):
    '''
    创建数据库连接，执行sql
    :param sql:
    :param user:
    :param password:
    :param host:
    :param port:
    :param db:
    :return:
    '''

    with pymysql.connect(user=user,
                         password=password,
                         host=host,
                         port=port,
                         db=db) as my:
        my.execute(sql)
        result=my.fetchone()
    return result

class Check(unittest.TestCase):

    def check_status_code(self,status_Code):
        self.assertEqual(status_Code,200)

    def json_value(self,json,key,value):
        re=json.json().get(key)
        self.assertEqual(re,value)

    def value_in_text(self,responce,value):
        self.assertIn(value,responce)


if __name__ == '__main__':
    url = 'http://localhost/index.php?ctl=user&act=dologin'
    data = {'email': 'liuww',
            'user_pwd': 'bkNoY1B0TnFrcGZxQ1hnUVFDSEVFdmJlTm90c0x1T0xGU1hhQWxRYWpoSXd2TVphZ3UlMjV1NjVCOSUyNXU3RUY0MTIzcXdlJTI1dThGNkYlMjV1NEVGNg==',
            'ajax': '1'}
    r=BaseRequest().get_request('post',data,url)
    print(r.json())