import unittest
from HTMLTestReportCN import HTMLTestRunner
from libs.tool import sendEmail
import time
from conf.config import current_path
from libs.tool import DoExcel
import copy

def get_dis(discover):
    '''删除excel文档中不需要执行的用例'''
    #  实例化操作excel类，获取执行的测试用例
    sheet = DoExcel()
    is_run=[]
    for name in sheet.get_sheets_name():
        #   将执行的测试用例编号放到not_run中
        sheet_obj=DoExcel(name)
        is_run+=sheet_obj.get_is_run_name()

    #  复制一份，以免for循环中删除不需要执行的用例后，下标溢出
    dis_copy = copy.deepcopy(discover)
    #  获取tc.py模块集
    mod_dis=dis_copy._tests
    for i in range(len(mod_dis)):
        #  获取单个模块中的测试类集
        cla=mod_dis[i]._tests
        for j in range(len(cla)):
            #  获取单个模块中的测试用例集
            case=mod_dis[i]._tests[j]._tests
            for c in range(len(case)):
                #  如果用例编号不需要执行，就把用例删掉
                if case[c]._testMethodName not in is_run:
                    discover._tests[i]._tests[j]._tests.remove(case[c])
    return discover
# <tests=[<tests=[<tests=[<n_001>, <n_002>, <003>]>]>,
#     <tests=[<tests=[t_001>, <t_002>, <t_003>, <t_004>]>]>]>
# <tests=[<tests=[<tests=[<n_001>, <n_002>]>]>, < tests=[<tests=[<t_001>, <t_004>, <t_005>]>, <tests=[<r_001>, <r_002>]>]>]>


def run_main():
    #  加载路径下tc.py模块下的所有测试用例
    dirpath=current_path+'/scripts/'
    discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
    #  对比后得到需要执行的测试用例
    discover_last=get_dis(discover)
    curtime= time.strftime('%y%m%d%H%M%S')
    filepath=current_path+'/report/report'+curtime+'.html'
    f=open(filepath,'wb')
    runner=HTMLTestRunner(stream=f,
                          title='Xsmart自动化测试报告',
                          description='当前测试功能有\"会员管理\"、"登录"等',
                          tester='lww'
    )
    runner.run(discover_last)
    f.close()
    # sendEmail(filepath)
if __name__=='__main__':
    run_main()
    # dirpath=current_path+'/scripts/'
    # discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
    # get_dis(discover)
