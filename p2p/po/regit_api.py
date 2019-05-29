import requests
import pymysql
from p2p.libs.tools import connectSql
from p2p.libs.tools import BaseRequest

class Regit(BaseRequest):

    def regit(self,username,phone,cid):

        '发送短信验证码'
        sms_url = 'http://localhost/index.php?ctl=ajax&act=get_register_verify_code'
        sms_data = {
            'user_mobile':phone,
            'smsverify':'aaaa'
        }
        result = self.get_request(url=sms_url,data=sms_data)
        print('短信发送成功:',result.json())
        coo=result.cookies
        print(coo)
        # 获取短信验证码
        sql = 'select verify_code from cyo_mobile_verify_code where mobile="'+phone+'"'
        varify = connectSql(sql)[0]

        # 注册流程1
        url = 'http://localhost/index.php?ctl=user&act=doregister'
        data = {
            'user_type': 0,
            'user_name': username,
            'mobile': phone,
            'smsverify': 'aaaa',
            'sms_code':varify,
            'user_pwd':'sf123456',
            'user_pwd_confirm': 'sf123456',
            'referer': '',
            'agreement': 1,
            'commit': '注册'
        }
        result = self.get_request(url=url,data=data,cookies=coo)
        # print('注册成功之后返回的值是:', result.text)

        # 注册流程2
        verify_url = 'http://localhost/index.php?ctl=user&act=do_re_name_id'
        data = {
            'real_name':username,
            'idno':cid,
            'sex':'-1',
            'byear':'0',
            'bmonth':'0',
            'bday':'0',
            'commit':'%E9%AA%8C%E8%AF%81',
        }
        result = self.get_request(url=verify_url,data=data,cookies=coo)
        # requests.get()
        # print(result.text)
        return result

if __name__ == '__main__':
    r=Regit()
    r.regit('yoyoy2','13890900102','432501199906226227')