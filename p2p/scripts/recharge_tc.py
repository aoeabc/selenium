from p2p.libs.tools import Check
from p2p.po.recharge import Recharge
import unittest

class Charge(Check):
    def setUp(self):
        self.r=Recharge()

    def test_recharge_api(self):
        resoult=self.r.prepayApi()
        self.check_status_code(resoult.status_code)

if __name__ == '__main__':
    unittest.main()