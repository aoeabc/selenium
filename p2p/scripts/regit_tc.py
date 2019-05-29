from p2p.libs.tools import Check
from p2p.po.regit_api import Regit
import unittest

class Charge(Check):

    def setUp(self):
        self.r=Regit()

    def test_regit_api(self):
        result=self.r.regit('yoyo880','13788716677','432503198009226227')
        self.value_in_text(result.text,'注册成功')

if __name__ == '__main__':
    unittest.main()