import yagmail


#链接邮箱服务器
#user   用户邮箱
#password    邮箱授权码，邮箱中设置
#host    邮箱服务器地址
# yag = yagmail.SMTP(user="liuww_aoeiuv@163.com",
#                    password="xiayu147",
#                    host='smtp.163.com')

# yag = yagmail.SMTP(user="670304927@qq.com",
#                    password="xpofjceeuqbpbebj",
#                    host='smtp.qq.com')
mail = yagmail.SMTP(user='',password='',host='')
mail.send(to='',subject='',contents='',attachments='',cc='')


#邮箱正文
contents = [u'这是另一个测试邮件内容']

# 发送邮件
#  to   接受邮箱
#   subject   邮件主题
#  contents   邮件内容
#   attachments   附件
#   cc     抄送
yag.send(to=['2951843853@qq.com'],
         subject=u'又一封测试邮件',
         contents=contents,
         attachments='D:/lww/python_test/action.py')

#  多个用户发送邮件
# yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'], 'subject', contents)
#xpofjceeuqbpbebj