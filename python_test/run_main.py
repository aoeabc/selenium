import unittest
from HTMLTestReportCN import HTMLTestRunner
import time

def run_main():
    dirpath='./scripts/'
    discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_test.py')
    curtime= time.strftime('%y%m%d%H%M%S')
    filepath='./report'+curtime+'.html'
    with open(filepath,'wb') as f:
        runner=HTMLTestRunner(stream=f,
                              title='计算器自动化测试报告',
                              description='测试加法、减法功能',
                              tester='Lww'
        )
        runner.run(discover)

if __name__=='__main__':
    run_main()
