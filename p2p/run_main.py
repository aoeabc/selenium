import unittest
from HTMLTestReportCN import HTMLTestRunner
import time

def run_main():
    dirpath='./scripts/'
    discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
    curtime= time.strftime('%y%m%d%H%M%S')
    filepath='./report/report'+curtime+'.html'
    f=open(filepath,'wb')
    runner=HTMLTestRunner(stream=f,
                          title='Xsmart自动化测试报告',
                          description='当前测试功能有\"会员管理\"等',
                          tester='lww'
    )
    runner.run(discover)
    f.close()

if __name__=='__main__':
    run_main()
