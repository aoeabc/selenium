import random
#    打印99乘法表
# for i in range(1,10):
#     string=''
#     for j in range(1,i+1):
#         string = string + str(j) +'*'+str(i)+'='+str(i*j) + '  '
#     print(string+'\n')

#-----------------------------------------------

# for i in range(100):
#     string = input('请输入文字：')
#     if string=='':
#         print('没有输入任何文字')
#         continue
#     elif string in ['aaa','bb','a','傻逼','qqq']:
#         print('真是个小机灵')
#     elif len(string)>10:
#         print('不要输入这么多内容')
#     elif '\\' or '/' in string:
#         print('我不喜欢斜杠')
#     else:
#         print('不知道你在说什么')

#-----------------------------------------------

# for i in range(2,101,2):
#
#     print(i)

#-----------------------------------------------
#求和，1-100的总和
# sumnum =0
# for i in range(1,101):
#     sumnum=sumnum+i
# print(sumnum)

#------------------------------------------ -----
#打印菱形，根据输入的奇数，打印出相对应的大小的菱形
# while 1==1:
#     try:
#         num1 = int(input('输入菱形的行数，必须是奇数：'))
#         if (num1 % 2) == 1:
#             num=num1//2+1
#             tu =''
#             #datu=[]
#             for i in range(1,num*2):
#                     for j in range(0,num*2-1):
#                         if i<=num:
#                             if j in range(num-i,num+i-1):
#                                 tu = tu + '*'
#                             else:
#                                 tu = tu + ' '
#                         else:
#                             if j in range(i-num,num*2-(i-num+1)):
#                                 tu = tu + '*'
#                             else:
#                                 tu = tu + ' '
#                     print(tu)
#                     #datu.append(tu)
#                     tu=''
#             # print(datu)
#         elif num1=='':
#             print('不能为e空')
#             continue
#         else:
#             print('必须是奇数')
#             continue
#     except:
#         print('必须是数字')
#         continue

# [' ',' ','*',' ',' '] 1   [2,3]  [3-1,3]
# [' ','*','*','*',' '] 2   [1,4]  [3-2,3+1]
# ['*','*','*','*','*'] 3   [0,5]  [3-3,3+2]
# [' ','*','*','*',' '] 4   [1,4]  [4-3, 2n-(i-num+1)]
# [' ',' ','*',' ',' '] 5   [2,3]  [5-3,2n-(i-num+1)]
#--------------------------------------------------------------
# errer_times=0
# while errer_times<3:
#     login_message=input('请输入正确的用户名+密码')
#     if login_message=='lww+123456':
#         print('登录成功')
#         break
#     else:
#         errer_times+=1
#         print('用户名密码错误，请重试')

#-------------------------------------------------------------------------
#获取三个数字并给排序后打印出来
# def exceptFun():
#     age = []
#     while len(age)<3:
#         try:
#             num=int(input('输入数字：'))
#             age.append(num)
#         except Exception as e:
#             print(e)
#             print('只能 输入数字')
#     print(age)
#
#     for i in range(len(age)-1):
#         for j in range(len(age)-1):
#             print(j)
#             if age[j] > age[j+1]:
#              age[j],age[j+1] = age[j+1],age[j]
#     print(age)
# if __name__=='__main__':
#     exceptFun()

# -----------------------------------------------------
#  获取学生成绩，并打印成绩等级
# try:
#     num=int(input('输入学生成绩：'))
#     if num>100:
#         print("满分为100，输入有误")
#     elif num>=90:
#         print('该学生成绩等级为“A”')
#     elif num>=80:
#         print('该学生成绩等级为“B”')
#     elif num >= 70:
#         print('该学生成绩等级为“c”')
#     elif num>=60:
#         print('该学生成绩等级为“d”')
#     else:
#         print('该学生成绩等级为“E”')
#
# except Exception as e:
#     print(e)
#     print('只能 输入数字')


#------------------------------------------------------------------
#猜字游戏，随机生成1-9的数字，当输入数字大于随机数时，提示太太，当输入数字小于随机数时，提示太小，
# 当输入数字等于随机数时，提示猜对了，游戏结束
# rand_num = random.randint(1,10)
# while True:
#     try:
#         num=int(input('输入0-9的整数：'))
#         if  num >10 or num<1:
#             print ('输入有误，只能输入1-9的整数')
#             continue
#         if num>rand_num:
#             print('太大')
#             continue
#         if num<rand_num:
#             print('太小')
#             continue
#         if num==rand_num:
#             print('恭喜你猜对了')
#             break
#
#     except Exception as e:
#         print(e)
#         print('只能 输入数字')
#
# #-------------------------------------------------------
#  判断字符串中，字母个数与数字个数
# string='admin123456'
# num=0
# a=0
# for i  in string:
#     try:
#         if type(int(i)) is int:
#             num=num+1
#     except:
#         a=a+1
# print('数字的个数为%d,字母的个数为%d'%(num,a))
# #----------------------------------------------------------
#  判断字符串中，字母个数与数字个数

# string='admin123456'
#
# num=0
# a=0
# for i  in string:
#     if i.isdigit():
#         num=num+1
#     else:
#         a=a+1
# print('数字的个数为%d,字母的个数为%d'%(num,a))
#--------------------------------------------------------------
#--------------冒泡排序
# age=[234,43534,23,5645,78,99,55,23]
# for i in range(len(age)-1):
#     for j in range(len(age)-1):
#         if age[j] > age[j+1]:
#             age[j],age[j+1] = age[j+1],age[j]
# print(age)
#--------------------------------------------------------------------
#实参为方法名
# #eval()
# def fun1():
#     print('1111')
# def fun2(a):
#     a()
#     #eval(a)()
# fun2(fun1)
#---------------------------------------------------------------------
# dit_word = {}
# def set_message(word,fy):
#
#     if word not in list(dit_word.keys()):
#         dit_word[word]=fy
#         print('收集成功！！！')
#     else:
#         print('已经收集过该单词。')
#     return dit_word
#
# def get_note(word):
#     if word  in list(dit_word.keys()):
#         string='单词是：'+word+'；这个单词的翻译是：'+dit_word.get(word)+'；'
#         print(string)
#     else:
#         print('没有找到笔记')
# #
# # set_message('srt','werwer')
# # set_message('srt1','werwer')
# # set_message('srt2','werwer')
# # set_message('srt','werwer')
# get_note('srt')
# get_note('111')
#-----------------------------------------------------
#匿名函数
# c = lambda x: x > 30
# print(c(30))
# print(list(filter(c,[49,123,2])))
# filter(lambda x: x > 30,[49,123,2])
# reduce(lambda x,y:x*y,[49,123,2])
# print((lambda x,y : x if x > y else y)(12,13))
# import functools
# print(functools.reduce(lambda x,y:x+y,range(1,101)))
#
# a=functools.reduce(lambda x,y:x+y,list(filter(lambda x : x%2==0,range(1,101))))
# print(a)


#-----------------------------------------------
#字符串处理
# a='elirjgihrgiwjtr'
# b='2349868576795'
# c=a+'{}'.format(b)


# a='1'
# b='22222'
# print(a.join(b))

a='/'
b='https://www.cnblogs.com/yangliguo/p/7921338.html'
# print(b.split(a))
# print(b.replace('/',' '))
# print(b.count('/'))
# print(b.find('uo'))
#
# c=b+'/{aaa}/{bbb}'.format(aaa='safwe',bbb='ksjdfk')
# c=b+'{0}/{1}/{0}'.format('000','111')
# print(c)
# dit={'name1':'ky1','name2':'ky2'}
# list=['name1','name2']
# c=b+'{name1}/{name2}'.format(**dit)
# d=b+'/{0[0]}/{0[1]}'.format(list)
# print(d)
#------------------------------------------------
#内建函数

#------------------------------------------------
dit_word={}
def study_hand(word,trans):
    if word in list(dit_word.keys()):
        if trans==dit_word.get(word):
            print('翻译正确')
        else:
            print('翻译错误')
    else:
        dit_word[word] = trans
        print('录入成功')

study_hand('123','111')
study_hand('123','111')
study_hand('123','112')
study_hand('123','111')

