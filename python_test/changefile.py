#获取百度新闻标题并保存至文本文档
# from selenium import webdriver
# import time
#
#
# bro = webdriver.Chrome()
# bro.get('http://news.baidu.com/')
# time.sleep(3)
# eles=bro.find_elements_by_xpath('//a[@target="_blank"]')
# with open('./newtile.txt','w+') as ff:
#     for ele in eles:
#         inner_text = ele.get_attribute('innerText')
#         ff.write(inner_text)
#         ff.write('\n')
# bro.close()
#-------------------------------------------
# 操作文本文档
# # #1
# with open('./a.txt', 'a') as ff:
#     ff.write('Hello World\n')
#
# #-------------------------------------------
# # #2
# # #
# with open('./a.txt', 'a') as ff:
#     ff.write('Hello World\n')
# # #-------------------------------------------
# # #3
# with open('./a.txt', 'r+') as ff:
#     list_lines=ff.readlines()
#     print(list_lines)
#
# ls_all=[]
#
# for list_line in list_lines:
#     l=list_line.replace('Hello','nihao')
#     ls_all.append(l)
#
# with open('./a.txt', 'w') as ff:
#     for i in ls_all:
#         ff.write(i)
#
# # #-------------------------------------------
# # #4
#
# with open('./a.txt', 'w') as ff:
#     ff.write('testing')
#----------------------------------------------------------------------------
#使用函数进行封装
# def read_line(file):
#     with open(file, 'r+') as ff:
#         list_lines=ff.readlines()
#     return list_lines
#
# def write_line(file,message,mode='a'):
#     if mode=='a':
#         with open(file, 'a+') as ff:
#             ff.write(message)
#     else:
#         with open(file, 'w+') as ff:
#             ff.write(message)
#
# def file_replace_message(file,old_message,new_message):
#     lines=read_line(file)
#     new_lines=[]
#     for line in lines:
#         new_line=line.replace(old_message,new_message)
#         new_lines.append(new_line)
#     for i in new_lines:
#         write_line(file,i,'w')
#
#
# #1
# write_line('./aa.txt','Hello World\n','w')
# # #2
# write_line('./aa.txt','Hello Python\n')
# #3
# file_replace_message('./aa.txt','Hello','nihao')
# #4
# write_line('./aa.txt','testing\n','w')
#---------------------------------------------------------------------------------

#操作文件目录

import os
# os.mkdir('d:\\eee')
# os.makedirs('d:\\eee\\eee')
# os.rename('d:\\eee\\eee','d:\\eee\\eee1')
# os.rmdir('d:\\eee')
# os.removedirs('d:\\eee\\eee')
# os.remove('d:\\a.txt')
# os.getcwd()
# os.path.abspath(__file__)
#
# os.chdir()
# os.curdir()
# os.path.normpath()
#
# os.path.isdir()
# os.path.isfile()
#
# os.path.exists()
# print(__file__)
# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))
# print(os.path.join(__file__))
# print(os.path.split(__file__))


#-----------------------------------------------------------
#1
# local=os.getcwd()
# os.chdir('d:\\')
# print(os.getcwd())
# os.mkdir('./A')
# os.chdir(local)
# print(os.getcwd())
#
# #------------------------
# #2
# work_dir='d:\\work100'
# os.mkdir(work_dir)
# for i in range(100):
#     work_path=work_dir+'\\'+str(i)+'.txt'
#     with open(work_path,'w+') as ff:
#         ff.write('Hello Python')
# #---------------------------
#3

# file_path='./test/test.txt'
#
# def is_file_exist(filename_path):
#     path1,file1=os.path.split(filename_path)
#     if os.path.exists(filename_path):
#         return '已经存在该文档'
#     else:
#         if not os.path.isdir(path1):
#             os.makedirs(path1)
#         with open(file_path, 'w+') as ff:
#             ff.write('')
#         return '创建成功'
#
# print(is_file_exist(file_path))

#--------------------------------------
#时间
# import datetime
# # print(time.time)
# datetime.datetime.strftime('%H:%M:%S')
# import  time
# def log_fun(*args,**kwargs):
#     fomat='%y-%m-%d %H:%M:%S'
#     value=time.localtime(int(time.time()))
#     ll=time.strftime(fomat,value)
#     print(ll,*args,**kwargs)
#
# log_fun('sajligerg','erlrkjglerg','ergiuergiueritrg')

#---------------------------------------------------
# def login():
#     err_times=0
#     user_pwd=['admin','123456']
#     flag = ''
#     while 1==1:
#         err_times += 1
#         username=input('输入用户名：')
#         password=input('请输入密码：')
#         if username ==user_pwd[0] and password== user_pwd[1]:
#             flag='登录成功'
#             break
#         else:
#             if username == '':
#                 print('用户名不能为空')
#             elif password=='':
#                 print('密码不能为空')
#             else:
#                 print('用户名密码不正确')
#         if err_times==5:
#             flag='失败次数超过五次，请稍后再试'
#             break
#         print('当前登录失败次数：{}'.format(err_times))
#     return flag
#-----------------------------------------------------------------
# def login():
#     err_times=0
#     user_pwd=['admin','123456']
#     flag = ''
#     while err_times<5:
#         err_times += 1
#         username=input('输入用户名：')
#         password=input('请输入密码：')
#         if username ==user_pwd[0] and password== user_pwd[1]:
#             err_times = 0
#             flag='登录成功'
#             break
#         else:
#             if username == '':
#                 print('用户名不能为空')
#             elif password=='':
#                 print('密码不能为空')
#             else:
#                 print('用户名密码不正确')
#     if err_times==5:
#         flag='失败次数超过五次，请稍后再试'
#     return flag
#
# print(login())
#-----------------------------------------------------------------
import time
# def log(*args,**kwargs):
#     fm='%y-%m-%d %H:%M:%S'
#     ti=time.localtime(int(time.time()))
#     print(time.strftime(fm,ti),*args,**kwargs)
# log('fashgkhrkughureuirgkeioirgi')

#转化时间戳成毫秒
print(int(time.time())*1000)

from datetime import datetime
day=datetime.today()
#打印当前时间
ti=day.now()
print(ti)
#当前年份、月份、日期、星期等
print(ti.year)
print(ti.month)
print(ti.day)
print(ti.weekday())
