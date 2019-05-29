import requests
import pymysql
import time

def post_requrest(url,data):
    res=requests.post(url,data)
    return res

def get_requrest(url):
    res=requests.get(url)
    return res

def connectSql(sql='',user='root',password='root',host='localhost',port=3306,db='p2p'):

    with pymysql.connect(user=user,
                         password=password,
                         host=host,
                         port=port,
                         db=db) as my:
        my.execute(sql)
        result=my.fetchone()
    return result

#  验证用户名
# /index.php?ctl=ajax&act=check_field&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC
#
# field_name=user_name&field_data=nihao

def check_username(username):
    # username='nihao1'
    url_username = 'http://localhost/index.php?ctl=ajax&act=check_field&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC'
    data_username = {'field_name': 'user_name',
                     'field_data': username
                     }
    test=post_requrest(url_username,data_username).text

    if eval(test)['status']==1:
        return username
    else:
        return None


#验证手机号
# /index.php?ctl=ajax&act=check_field&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC
#
# field_name=mobile&field_data=13480691284
def check_phone(phone):
    # phone='13786861235'
    url_phone = 'http://localhost/index.php?ctl=ajax&act=check_field&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC'
    data_phone = {'field_name': 'mobile',
                  'field_data': phone
                     }
    test=post_requrest(url_phone,data_phone).text
    if eval(test)['status']==1:
        return phone
    else:
        return None

# 获取验证码
# /index.php?ctl=ajax&act=get_register_verify_code&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC
# user_mobile=13480691284&smsverify=2222

sql='select verify_code from cyo_mobile_verify_code where mobile=""'

def get_verify(phone):
    url_verfy = 'http://localhost/index.php?ctl=ajax&act=get_register_verify_code&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC'
    data_verfy = {'user_mobile': phone,
                  'smsverify': '2222'
                     }
    # sql1 = 'select verify_code from cyo_mobile_verify_code where id=(select MAX(id) from cyo_mobile_verify_code )'
    sql = 'select verify_code from cyo_mobile_verify_code where mobile="'+phone+'"'
    test=post_requrest(url_verfy,data_verfy)
    time.sleep(5)
    varify=connectSql(sql)
    print(varify)
    return varify


# # 注册
# /index.php?ctl=user&act=doregister
# user_type=0&
# user_name=lww&
# mobile=13480691284&
# smsverify=2222&
# sms_code=550048&
# user_pwd=123456aoe&
# user_pwd_confirm=123456aoe
# &referer=&
# agreement=1&
# commit=%E6%B3%A8%E5%86%8C

def user_register():
    phone = check_phone('13900000044')
    # usename = check_username('user009')
    time.sleep(2)
    varify = get_verify(phone)[0]
    time.sleep(2)
    url_phone = 'http://localhost/index.php?ctl=user&act=doregister'
    data_phone = {'user_type': 0,
                  'user_name': 'nidaye666',
                  'mobile': '13900000044',
                  'smsverify': 'aaaa',
                  'sms_code':varify,
                  'user_pwd':'sf123456',
                  'user_pwd_confirm': 'sf123456',
                  'referer': '',
                  'agreement': 1,
                  'commit': '注册'

                     }
    test=post_requrest(url_phone,data_phone,).cookies
    print(post_requrest(url_phone,data_phone).text)
    return test


# #  实名验证
# /index.php?ctl=ajax&act=getIdCardinfo&card=432503199106116117&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC
#
def check_id(id):

    url='http://localhost/index.php?ctl=ajax&act=getIdCardinfo&card='+id+'&fhash=jymfTimRGkFzvBdrbhDwnhHEJaIfZHvhNubwcPghMiUalUGjPC'
    test=get_requrest(url)
    mes=test.text
    b=eval(mes)['birthday']
    year=b[:4]
    month=b[5:7]
    day=b[8:10]
    if eval(mes)['sex']=='女':
        sex=0
    else:
        sex = 1

    result={'year':year,'month':month,'day':day,'sex':sex}
    return result
# #实名
# #
# /index.php?ctl=user&act=do_re_name_id
# real_name=123&idno=432503199106116117&sex=0&byear=1991&bmonth=06&bday=11&commit=%E9%AA%8C%E8%AF%81
def realname(id):
    r = check_id(id)
    url='http://localhost/index.php?ctl=user&act=do_re_name_id'
    data={'real_name':'liu',
          'idno':id,
          'sex':r['sex'],
          'byear':r['year'],
          'bmonth':r['month'],
          'bday':r['day'],
          'commit':'%E6%B3%A8%E5%86%8C'
    }
    cookis=user_register()
    print(cookis)
    test=requests.post(url=url,data=data,cookies=cookis)
    print(test.text)

if __name__ == '__main__':
    # phone=check_phone()
    # # usename=check_username()
    # varify=get_verify(phone)[0]
    # print(varify)
    test=user_register()
    print(test)
    # r=check_id('432503199106226227')
    # print(r)
    # realname('432503199106226227')