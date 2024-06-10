#=====SIMPLE CALCULATOR using classes and objects======
class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a//self.b
    def mod(self):
        return self.a%self.b
    def check(self):
        print("enter you choice:")
        print("1.ADD")
        print("2.sub")
        print("3.mul")
        print("4.div")
        print("5.mod")
        while True:
            choice=input()
            if choice in ('1','2','3','4','5'):
                if choice=='1':
                    print("addition is:",p1.add())
                if choice=='2':
                    print("subtraction is:",p1.sub())
                if choice=='3':
                    print("multiplication is:",p1.mul())
                if choice=='4':
                    print("division is:",p1.div())
                if choice=='5':
                    print("modulus is:",p1.mod())
                print("if you want again the menu of choice type (YES/NO):")
                choice1=input()
                if choice1=="YES" or choice1=="yes":
                    p1.check()
                elif choice1=="NO" or choice1=="no":
                    exit()
                else:
                    print("Invalid input")
                    exit()
v=int(input("enter first number:"))
l=int(input("enter second number:"))
p1 = addition(v,l)
p1.check()


