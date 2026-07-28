#1.create integer variable convert into float string bool
# a=20
# print(a)
# b=float(a)
# print(b)
# c=bool(a)
# print(c)
# d=str(a)
# print(d)

#2.float variable into int string bool
# a=10.0
# print(a)
# b=int(a)
# print(b)
# c=bool(a)
# print(c)
# d=str(a)
# print(d)

#3.boolean variable into int string float
# a=True
# print(a)
# b=int(a)
# print(b)
# c=float(a)
# print(c)
# d=str(a)
# print(d)

#4.string variable into int float bool
# a="90"
# print(a)
# b=int(a)
# print(b)
# c=float(a)
# print(c)
# d=bool(a)
# print(d)

#5.
#int,string,float values convert in boolan and zero ans 
# a=0
# b=bool(a)
# print(b)
# c=0.0
# d=bool(c)
# print(d)
# str=""
# bool=bool(str)
# print(bool)

# 6.perform arithmatic operation
# a=int(input("enter a first value:"))
# b=int(input("enter a second value:"))
# sum=a+b
# sub=a-b
# multi=a*b
# div=a/b
# print(sum)
# print(sub)
# print(multi)
# print(div)


#7.Bit-wise operation
# val1=int(input("enter the value in 1:-"))
# val2=int(input("enter the value in 2:-"))
# bit_and=val1&val2
# print(bit_and)
# bit_OR=val1^val2
# print(bit_OR)
# bit_not=(~val1)
# print(bit_not)
# bit_left=(val1 << 2)
# print(bit_left)
# bit_right=(val1 >> 2)
# print(bit_right)


#8.perform relational operation
# a=int(input("enter a first value:"))
# b=int(input("enter a second value:"))
# c=a<b
# print(c)
# d=a>b
# print(d)
# e=a==b
# print(e)
# f=a!=b
# print(f)
# g=a<=b
# print(g)
# h=a>=b
# print(h)

#9.perform logical operation
# a=int(input("enter a first value:"))
# b=int(input("enter a second value:"))
# print("logical and opeator:",(a<b)and(a>b))
# print("logical or opeator:",(a<b)or(a>b))
# print("logical not opeator:",not(a>b))

#10.input 3 number print big number and small number

# a=int(input("enter a first value:"))
# b=int(input("enter a second value:"))
# c=int(input("enter a first value:"))

# if(a>b and a>c):
#     print("num is greater",a)
# elif(b>a and b>c):
#     print("num is greater",b) 
# else:
#     print("num is greater")    

# if(a<b and a<c):
#     print("num is smaller",a)
# elif(b<a and b<c):
#     print("num is smaller",b) 
# else:
#     print("num is smaller") 

#11. a,b,c =input("Enter three numbers separated by a space: ").split()
# if(a>b and a>c):
#      print("num is greater")    

# if(a<b and a<c):
#      print("num is smaller",a)
# elif(b<a and b<c):
#      print("num is smaller",b) 
# else:
#      print("num is smaller")

'''12.while loop use and print odd no in reverse
i = 10

while i >= 1:
    if i % 2 != 0:  
        print(i)
    i -= 1  '''


'''13.for loop use and print even number in reverse
for i in range(10,-1,-1):
     if(i%2==0):
        print(i)'''


'''14.odd numbers  between 1 to 10 using continue in both for loop
for i in range(1,11):
     if(i%2==0):
         continue
     print(i)'''

'''14(a) odd numbers  between 1 to 10 using continue in both while loop
i = 1

while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1'''

'''15.Take 10 numbers in a list(array) and print only first 3 numbers using loop
while loop use
l=[1,2,3,4,5,6,7,8,9,10]
i=0

while(i<=2):
    print(l[i])
    i+=1
    
for loop use
for i in range(3):
    print(l[i])
    i+=1'''

'''16.Create a function which will not take any argument but will print numbers from 1
to 10.
def sum():
    i=1
    while(i<=10):
      print(i)
      i+=1
sum()'''

''' 17.Create a function which will take 4 arguments where 2 wil be mandatory and 2
keyword arguments. Perform multilpication if 2 values are passed. Perform
addition if 3 are passed. Perform addition of 1st two operands and 2nd two operands
and then do a subtraction if 4 arguments are passed

def sum(a,b,c=None,d=None):
    if c is None and d is None:
        print(a * b)
    elif c is not None and d is None:
        print(a+b+c)
    elif c is not None and d is not None:
        print((a+b)-(c+d))

sum(3,4)
sum(3,4,6)
sum(4,8)'''


#18Create a function that will take unlimited arguments and should add all the arguments which are passed.
# def add(*args):
#     total=0
#     for i in args:
#         total=total+i
#     print(total)

# add(10,20,30)

#19. Create a function which will take unlimited arguments both non keyword and keyword arguments. Add the values of all non keyword arguments and also the value of keyword arguments.
# def add(*args,**args2):#* is used non-key argument and ** is used of unliment keybord of used
#     total=0
#     for i in args:
#         total=total+i
#     print(total)
#     for value in args2:
#         total += value
# add(10,20,30)

#20.Write a function with recursion to give the power of a number. It will be having two parameters no and power. If no power is passed it should take 0.

# def power(no, exp=0):
#     if exp==0:
#         return 1
#     return no * power(no , exp- 1)


# print(power(6,7))

#21Create a function with recursion which will find the factorial of a given no.


# def factorial(n):
#     if n ==0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# num=int(input("enter the number"))
# print("factorial = ",factorial(num))

#22.
# def calculator(choice):
#     def addition(a,b,c):
#         print("addition",a+b+c)
#     def subtraction(a,b,c):
#         print("subtraction",a-b-c)
#     def multiplication(a,b,c):
#         print("mulitiplcation",a*b*c)
#     def division(a,b):
#         print("division",a/b)
#     def exponent(a,b):
#         print("exponent",a**b)
#     def floor_divison(a,b):
#         print("floor_division",a//b)
#     if choice==1:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         c=int(input("enter the number:-"))
#         addition(a,b,c)
#     elif choice==2:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         c=int(input("enter the number:-"))
#         subtraction(a,b,c)
#     elif choice==3:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         c=int(input("enter the number:-"))
#         multiplication(a,b,c)
#     elif choice==4:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         division(a,b)
#     elif choice==5:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         exponent(a,b)
#     elif choice==6:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         floor_divison(a,b)
# print('''
#     1.Addition
#     2.subtratction
#     3.mulitiplcation
#     4.division
#     5.exponent
#     6.floor_division
# ''')
# num=int(input("enter the chioce"))
# print("calcuate the number",calculator(num))

#23Create a two funcitons. Call one function from another function.
# def calcuate():
#     x=int(input("enter the number:-"))
#     y=int(input("enter the number:-"))
#     sum(x,y)

# def sum(a,b):
#     print("addition",a+b)

# calcuate()

#24.Create a function that will take 5 arguments 2 will be mandatory and 3 will be keyword parameters. If 2 parameters are passed perform multiplication of 2 parameters. If 3 parameters are passed print all the 3 parameters. If 4 parameters are passed addition of 4 parameters. If 5 parameters are passed multiply 2mandatory parameters and then separately multiply 3 keyword parameters and add both of them.
# def calculator(a,b,c=None,d=None,e=None):
#     if c is None and d is None and e is None:
#         print("mulitiplcation",a*b)
#     elif c is not None and d is None and e is None:
#         print("first element",a)
#         print("second element",b)
#         print("thrid element",c)
#     elif c is not None and d is not None and e is None:
#         print("addition",a+b+c+d)
#     elif c is not None and d is None and e is not None:
#         print("multiplication",(a*b)+(c*d*e))

# calculator(1,2)
# calculator(1,2,3)
# calculator(11,12,13,14)
# calculator(55,66,77,88,99)

''' 25.Define a class and define two member variables and two methods inside the class.
One method will have one parameter and other method will not have any
parameter. Create a constructor for the class accepting two parameters and assign
them to the class member variables. One of the two methods will perform an
operation on the member variables and give result. The second method will print
the result.

class calculcator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.result=0

    def show(self):
         self.result=(self.a+self.b)

    def display(self):
        print("first number",self.a)
        print("second number",self.b)
        print("third number:",self.result)

obj=calculcator(10,20)
obj.show()
obj.display()'''

'''26.Create a parent class and a child class. Create two methods in the parent class.
Create one method in the child class. Create an object of parent and try to access
the method of parent and child class. Create an object of child class and try to
access the method of parent and child class.

class A():
    def b(self):
        print("hello a")
    def c(self):
        print("hello b")
class d():
    def e(self):
        print("hello e")

s=A()
s.b()
s.c()
#s.e()

r=d()
r.e()
#r.b()
#r.c()'''

'''27.Create a constructor and destructor for the above class
class employee():
    def __init__(self):
        print("parent constructor")
    def method1(self):
        print("method 1")
    def method2(self):
        print("method 2")
        
class manager(employee):
    def __init__(self):
        super().__init__()
        print("child constructor:")
    def method3(self):
        print("method 3")
        

obj=employee()
obj.method1()
obj.method2()
#obj.method3()'employee' object has no attribute 'method3'
objs=manager()
objs.method3()
objs.method1()#call thase parent class method because super keyword use in child class 
objs.method2()'''



'''28.Override and Overwrite a method of the parent class in child class

# class partent:
#     def show(self):

#         print("partent class method")
# class child :
#     def show(self):
#         print("child class")

# c=child()
# c.show()'''

'''29.
multiple inheritance
class Flyer:
    def fly(self):
        return "I can fly high!"

class Swimmer:
    def swim(self):
        return "I can swim deep!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack quack!"


donald = Duck()
print(donald.fly())    
print(donald.swim())   
print(donald.quack())  


multilevel inheritance
class teacher():
    def teach(self):
        print("40000")
        
class parent(teacher):
    def manager(self):
        print("50000")

class child(parent):
    def study(self):
        print("6000")

c=child()
c.study()
c.manager()
c.teach()'''

'''30.Perform overloading for constructors and methods defined in the class
class calcuate:
     def __init__(self,name=None,age=None):
         if name is None and age is None:
             print("Default Construction")
         elif age is None:
             print("Name",name)
         else:
             print("Name",name)
             print("age",age)
 cal=calcuate()
 cal=calcuate("sakshi")
 cal=calcuate("sakshi",20)'''


'''31
class my_parent_class:
    x = 40
    y = 5

    
def __init__(self, a=None, b=None):
        if a is None:
            self.a = self.x
        else:
            self.a = a

        if b is None:
            self.b = self.y
        else:
            self.b = b


def add(self, p=0, q=0):
        self.res1 = self.a + self.b
        self.print_result()

    
def sub(self, p=0, q=0):
        self.res2 = self.a - self.b
        self.print_result()


    def print_result(self):
        if hasattr(self, "res1"):
            print("Addition =", self.res1)
        if hasattr(self, "res2"):
            print("Subtraction =", self.res2)



class my_child_class(my_parent_class):

    
    def __init__(self, a=None, b=None, z=2):
        super().__init__(a, b)
        self.z = z

    
    def add(self, p=0, q=0):
        super().add()      # Calls parent add()
        print("Addition of x, y and z =", self.a + self.b + self.z)

    
    def print_result(self):
        print("Addition of x, y and z =", self.a + self.b + self.z)

    def sub(self, p=0, q=0):
        print("Multiplication =", self.a * self.b * self.z)

    
    def __del__(self):
        print("Destructor called for Child Object")



print(" Parent Class Objects ")

obj1 = my_parent_class()
print("Object 1:")
obj1.add()
obj1.sub()

print()

obj2 = my_parent_class(20)
print("Object 2:")
obj2.add()
obj2.sub()

print()

obj3 = my_parent_class(30, 15)
print("Object 3:")
obj3.add()
obj3.sub()
print("\n Child Class Object ")

c1 = my_child_class(10, 5, 3)
c1.add()
c1.sub()


print("\nManual Destructor Call")
del c1

print("Program End")'''







        
        
 





























        












































    


    

