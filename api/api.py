import requests
import pymysql
# 建立一个session连接
# ceshi git
def connectSql(sql='',user='root',password='root',host='localhost',port=3306,db='p2p'):

    with pymysql.connect(user=user,
                         password=password,
                         host=host,
                         port=port,
                         db=db) as my:
        my.execute(sql)
        result=my.fetchone()
    return result

# session没有s
s = requests.session()

# 发送短信验证码
sms_url = 'http://localhost/index.php?ctl=ajax&act=get_register_verify_code'
sms_data = {
    'user_mobile':'13920000022',
    'smsverify':'aaaa'
}
result = requests.post(url=sms_url,data=sms_data)
print('短信发送成功:',result.json())
coo=result.cookies
print(coo)
# 获取短信验证码
sql = 'select verify_code from cyo_mobile_verify_code where mobile="13920000022"'
varify = connectSql(sql)[0]
# 注册流程1
url = 'http://localhost/index.php?ctl=user&act=doregister'
data = {
    'user_type': 0,
    'user_name': 'nidaye097',
    'mobile': '13920000022',
    'smsverify': 'aaaa',
    'sms_code':varify,
    'user_pwd':'sf123456',
    'user_pwd_confirm': 'sf123456',
    'referer': '',
    'agreement': 1,
    'commit': '注册'
}
result = requests.post(url=url,data=data,cookies=coo)
print('注册成功之后返回的值是:', result.text)

# 注册流程2
verify_url = 'http://localhost/index.php?ctl=user&act=do_re_name_id'
data = {
    'real_name':'nidaye097',
    'idno':'440301199306225710',
    'sex':'-1',
    'byear':'0',
    'bmonth':'0',
    'bday':'0',
    'commit':'%E9%AA%8C%E8%AF%81',
}
result = requests.post(url=verify_url,data=data,cookies=coo)
requests.get()
print('实名认证注册成功', result.text)