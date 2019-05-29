import os

#  测试地址
test_url='http://localhost/admin.php'

#  获取当前文件路径
current_path=os.getcwd()

#  用例文件路径
# excel_path=os.path.dirname(__file__)
# print(excel_path)

#  email配置··································
#  发送者邮箱
email_user = 'liuww_aoeiuv@163.com'
#  发送者邮箱授权码
email_password = ''
#  发送者邮箱服务器地址
email_host = 'smtp.163.com'
#   接收邮箱
email_to = '670304927@qq.com'
#   邮件主题
email_subject = '这是主题'
#   邮件内容
email_contents = '这是另一个测试邮件内容'

#  sql配置···································

#  数据库用户名
sql_user='root'
#  数据库密码
sql_password='root'
#  数据库服务器地址
sql_host='localhost'
#  数据库端口号
sql_port=3306
#  数据库名
sql_db='edu'


#  测试用例Excel配置
excel_caseNo='A'
excel_caseData='D'
excel_caseExpected='E'
excel_caseIsRun='F'
