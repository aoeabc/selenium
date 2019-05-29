from p2p.libs.login_api import Login
from p2p.conf.config import host
class Recharge(Login):

    def prepayApi(self, check_ol_bl_pay='on', money='10000', pingzheng='',
                  memo='6222021411112222333', payment='5', bank_id='0'):
        url = '/member.php?ctl=uc_money&act=incharge_done'
        test_url=host+url
        # 登录P2P后台
        self.login()
        data = {
            'check_ol_bl_pay': check_ol_bl_pay,
            'money': money,
            'pingzheng': pingzheng,
            'memo': memo,
            'payment': payment,
            'bank_id': bank_id,
        }
        # 充值线下支付
        result = self.get_request(url=test_url, data=data, cookies=self.cookie)
        return result

if __name__ == '__main__':
    r=Recharge()
    t=r.prepayApi()