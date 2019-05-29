import requests
from p2p.libs.tools import BaseRequest
from p2p.conf.config import host

class Login(BaseRequest):
    cookie=''
    def login(self,
              url='/index.php?ctl=user&act=dologin',
              data={'email': 'liuww',
                    'user_pwd': 'bkNoY1B0TnFrcGZxQ1hnUVFDSEVFdmJlTm90c0x1T0xGU1hhQWxRYWpoSXd2TVphZ3UlMjV1NjVCOSUyNXU3RUY0MTIzcXdlJTI1dThGNkYlMjV1NEVGNg==',
                    'ajax': '1'}):
        '''

        登录接口
        :param url:接口路径
        :param data:请求数据
        :return:<Response [200]>
        '''
        # url = '/index.php?ctl=user&act=dologin'
        # data = {'email': 'liuww',
        #         'user_pwd': 'bkNoY1B0TnFrcGZxQ1hnUVFDSEVFdmJlTm90c0x1T0xGU1hhQWxRYWpoSXd2TVphZ3UlMjV1NjVCOSUyNXU3RUY0MTIzcXdlJTI1dThGNkYlMjV1NEVGNg==',
        #         'ajax': '1'}
        test_url=host+url
        res=self.get_request(method='post',url=test_url,data=data)
        self.cookie=res.cookies
        return res

if __name__ == '__main__':
    url='/index.php?ctl=user&act=dologin'
    data = {'email': 'liuww',
            'user_pwd': 'bkNoY1B0TnFrcGZxQ1hnUVFDSEVFdmJlTm90c0x1T0xGU1hhQWxRYWpoSXd2TVphZ3UlMjV1NjVCOSUyNXU3RUY0MTIzcXdlJTI1dThGNkYlMjV1NEVGNg==',
            'ajax': '1'}
    l=Login().login(url,data)
    print(l.json())