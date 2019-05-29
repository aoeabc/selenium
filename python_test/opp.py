#登录功能，使用类实现
# class Login(object):
#
#     error_times=0
#
#     def __init__(self,username,password):
#
#         self.username=username
#         self.password=password
#         self.user_pwd = ['admin', '123456']
#         self.flag=''
#         if self.error_times<6:
#             self.action()
#         else:
#             print('错误次数超过五次，不能登录')
#             return None
#         print('当前登录错误次数：{}'.format(Login.error_times))
#         self.error_times += 1
#
#     def action(self):
#         if self.username == self.user_pwd[0] and self.password == self.user_pwd[1]:
#             self.error_times = 0
#             print('登录成功')
#             # self.flag='登录成功'
#         else:
#             if self.username == '':
#                 print('用户名不能为空')
#             elif self.password=='':
#                 print('密码不能为空')
#             else:
#                 print('用户名密码不正确')
#         # return self.flag

# class Cat(object):
#
#     def __init__(self,col,kg=0):
#         self.col = col
#         self.kg=kg
#         self.kg_leval()
#
#     def eating(self,food='猫粮'):
#         print("开始吃东西了。。。。。")
#         if food =='鱼':
#             self.kg+=1
#         elif food=='猫粮':
#             self.kg+=2
#         else:
#             self.kg += 10
#         self.kg_leval()
#
#     def kg_leval(self):
#         if self.kg>10:
#             print('这只{}猫超重了'.format(self.col,self.kg))
#         else:
#             print('可爱的{}猫'.format(self.col))
#
#     # def __del__(self):
#     #     print("走完了这一生·····")

# class Lister(object):
#
#     def __init__(self,*li):
#         self.li=list(li)
#
#     def add_data(self,num):
#         self.li.append(num)
#         return True
#
#     def pop_data(self):
#         if len(self.li)<1:
#             return False
#         else:
#             self.li.pop()
#             return True
#
#     def remove_data(self,num):
#         if num in self.li:
#             self.li.remove(num)
#             return True
#         else:
#             return False
#
#     def get_data(self):
#         print(self.li)
#
# class List2(Lister):
#     def __init__(self):
#         super(List2,self).__init__(*li)
#         self.li
#---------------------------------------------------
#闭包函数

# def aaaa(li):
#     def inner(*args,**kwargs):
#         print('111')
#         return li
#     return inner()
#
# @aaaa
# def li(num1,num2):
#     return num1+num2
#
# print(li(88,222))
#-------------------------------------------------------
#
# class Student(object):
#
#     def __init__(self,name,age,*score):
#         self.name=name
#         self.age=age
#         self.score=list(score)
#
#     def get_name(self):
#         return str(self.name)
#
#     def get_age(self):
#         return int(self.age)
#
#     def get_score(self):
#         self.score.sort()
#         return self.score[-1]
#
# class Human(Student):
#
#     def work(self):
#         if self.get_score()>90:
#             return 'good job'
#         else:
#             return 'shit'
#
# if __name__ == '__main__':
#     stu=Human('234',22,24,98,33)
#     print(stu.work())


# class Ff1(object):
#     def __init__(self,name):
#         self.ff1=name
#
#     def ffFunc(self):
#         print(self.ff1)
#
#
# class Ff2(Ff1):
#     def __init__(self):
#         self.ff2 = 2
#
#     def ffFunc(self):
#         print(self.ff2)
#
# class Ss(Ff1):
#     def __init__(self,name):
#         super(Ss,self).__init__(name)
#         self.s = 3
#
#     def ss(self):
#         print(self.ff1)
#         self.ffFunc()
#
#
# if __name__ == '__main__':
#     s=Ss('ff')
#     s.ss()


# class Test(object):
#     aa='aa'
#     def __init__(self):
#         self.a=0
#         self.b=0
#
#     def fun(self):
#         return 111
#
#
#     # def __repr__(self):
#     #     return '这是实例说明'
#     #
#     # def __str__(self):
#     #     return '这是实例说明1'
#
#
#     # def __getattribute__(self, item):
#     #     return '保密数据'
#
# if __name__ == '__main__':
#     t=Test()
#     # print(t)
#     print(t.__dict__)
#     setattr(t,'c','这是c')
#     # print(t.__dict__)
#     print(getattr(t,'a1','111'))