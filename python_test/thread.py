import threading
import time
# a=0
# l=threading.Lock()
# def add():
#     l.acquire()
#     global a
#     # l.acquire()
#     num=a
#     num=num+1
#     a=num
#     # a+=1
#     time.sleep(0.001)
#     print('111111111111',a)
#     l.release()
#
# for i in range(30):
#     t=threading.Thread(target=add)
#     t.start()
#
def a():
    time.sleep(5)
    print('a is end')

def b():
    time.sleep(1)
    print('b is end')

def c():
    t1 = threading.Thread(target=a)
    t2 = threading.Thread(target=b)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    print('m is end')

c()