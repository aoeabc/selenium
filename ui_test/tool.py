import pymysql
import logging
import os
import time
import yagmail
from openpyxl import load_workbook

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# 类名称：InsertLog
# 类的目的：写日志
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：
# 创建时间：
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------
# 当前文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'log')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)

class InsertLog():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s - %(funcName)s line: %(lineno)3d] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        # fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

# -------------------------------------------------------------------------------
# 类名称：connectSql
# 类的目的：连接数据库,处理sql
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：
# 创建时间：
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

def connectSql(sql='',user='root',password='root',host='localhost',port=3306,db='edu'):
    try:

        with pymysql.connect(user=user,
                             password=password,
                             host=host,
                             port=port,
                             db=db) as my:
            my.execute(sql)
            result=my.fetchone()
        # -------第二种表达式-------
        # my = pymysql.connect(user=user, password=password, host=host, port=port, db=db)
        # mm=my.cursor()
        # mm.execute(sql)
        # result=mm.fetchone()
        # my.close()
        # mm.close()

        return result

    except BaseException as e:
        log=InsertLog()
        log.error('sql执行失败······')
        log.error(e)

# -------------------------------------------------------------------------------
# 类名称：sendEmail
# 类的目的：发送邮件
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：
# 创建时间：
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------
def sendEmail(user='liuww_aoeiuv@163.com',
              password='xiayu147',
              host='smtp.163.com',
              to='670304927@qq.com',
              subject='这是主题',
              contents='这是另一个测试邮件内容',
              attachments='D:/lww/python_test/action.py',
              # cc=''
              ):
    mail=yagmail.SMTP(user=user,password=password,host=host)
    mail.send(to=to,subject=subject,contents=contents,attachments=attachments)

# -------------------------------------------------------------------------------
# 类名称：sendEmail
# 类的目的：发送邮件
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：
# 创建时间：
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

def doExcel(filename,sheetname):
    workbook=load_workbook(filename)
    worksheet=workbook[sheetname]


if __name__ == '__main__':
    a=connectSql('select * from xsmart_users where username="18625426325"')
    print(a)
    sendEmail()