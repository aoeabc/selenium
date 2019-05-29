dit={'name':{'age':{'year':{'aaa':'1324'}}}}



def get_dit(dit,key):
    value=dit.get(key,None)
    if value==None:
        for i in dit:
            value = get_dit(dit.get(i),key)

        return  value
    else:
        return value


a=get_dit(dit,'aaa')
print(a)