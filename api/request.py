import requests
import json

def get_request(url):

    re=requests.get(url)
    if re.status_code==200:
        return re.text
    else:
        return None

def post_request(url,data):


    re=requests.post(url=url,data=data)
    if re.status_code==200:
        return re.cookies
    else:
        return None


if __name__ == '__main__':
    # url1 = 'http://bologe.net/portal.php'
    # get_request(url1)

    url2 = 'http://localhost/admin.php?m=mgr/admin.chklogin&ajax=1'
    data={'username':'admin','password':'admin'}
    result = post_request(url2,data)
    # c = result['PHPSESSID']
    # print(c)
    # header={'Cookie':'PHPSESSID='+c}
    # Cookie={'PHPSESSID':c}

    url3='http://localhost/admin.php?m=mgr/member2.saveMemberInfo&id='
    up_lod='http://localhost/kindeditor/php/upload_json.php?dir=imag'
    # cookies=c
    # file = {'file':open('D:\\0.jpg','rb')}
    file = {'head_img': ('0.jpg',open('D:\\0.jpg', 'rb'),'image/png'),'image_type': (None, 'other')}
    data1={'username':'10122342232',
           'realname':'100',
           'email':'2344@qq.com',
           'phone':'10122342232',
           'roleid':'请选择',
           'orid1':'0',
           'location_p':'北京市',
           'location_c':'市辖区',
           'location_a':'东城区',
           'type':'2',
           'head_img': '0.jpg'

           }

#           'head_img':file
#     t=requests.post(url=url3,data=data1,files=file,cookies=result)
    t = requsts.post(url=up_lod, files=file, cookies=result)
    # t=requests.post(url=url3, headers=header)
    print(t.text)