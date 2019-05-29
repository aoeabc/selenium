class CalcClass(object):
    
    def __init__(self,a,b):
        self.numA=a
        self.numB=b


    def add_data(self):
        return self.numA+self.numB

    def sub_data(self):
        return self.numA-self.numB

if __name__=='__main__':
    c=CalcClass(1,2)
    print(c.add_data())
    print(c.sub_data())
