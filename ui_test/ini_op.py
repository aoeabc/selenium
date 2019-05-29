# # from conf.ParseConfigurationFile import ParseConfigFile
#
# # 获取ini 文件数据
# # 模块自带的
# import configparser
# # 实例化 ConfigParser
# # Option == 可选择项
# # Section == 可选择项下面的子项
# # Section=1  1==子项的值
# conf = configparser.ConfigParser()
# # 读取文件
# conf.read('./conf.ini',encoding='utf-8')
# sections = conf.sections()
#
# # # 获取option
# print(conf.options('login'))
#
# # # 获取option内section key
# s_key = conf.get("login",'username')
# print(s_key)



import configparser

data= configparser.ConfigParser()
data.read('./conf.ini',encoding='utf-8')
print(data.options('login'))
print(data.get('login','username'))