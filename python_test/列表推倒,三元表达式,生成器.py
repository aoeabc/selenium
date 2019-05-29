
## 列表推到
l = []
for i in range(1,10):
    if i % 2 == 0:
        l.append(i)
print(l)

# 等价于上面
l2 = [i for i in range(1, 10) if i % 2 == 0]
print(l2)

# 不同括号代表的意思是不一样的
l3 = (i for i in range(1, 10) if i % 2 == 0)

# 三元表达式
a = 1
flag = True if a == 1 else False
print(flag)


