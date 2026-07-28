'''Exercise 2'''

'''1.Get me list of even numbers between 1 to 20 without using if condition.
l=[]
for i in range(2,21,2):
   l.append(i)
print(l)'''

'''1(a).Get me list of odd numbers between 1 to 20 without using if condition.
l=[]
for i in range(1,20,2):
    l.append(i)
print(l)'''

'''2. Get a list of 1 to 20 then remove elements from list to get only even elements.
l=[]
for i in range(1,21,1):
    if(i%2==0):
      l.append(i)
print(l)'''

'''3.Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in
a new list.
l=[1,2,3,4,5,6,7,8]
list=[4,5,6,7,8,9,10]
item=[]
for i in l:
    if i in list:
        item.append(i)
print(item)'''

'''4.Sort a shuffled list of 10 random numbers in descending order
import random
l=[2,3,56,78,65,34,89,98,67,177]
random.shuffle(l)
l.sort(reverse=True)
print(l)'''



'''5.x=(1,2,3,4,5), y=(4,5,6,7).Combine these two tuples in a single tuple ignoring the 
common elements.
x=(1,2,3,4,5)
y=(4,5,6,7)
z=()
for i in x:
    if i not in y:
        z=x+y
print(z)'''


'''6.Define two sets and perform all the set operations and validation operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result1 = A | B
print("Union using '|':", result1)

result2 = A.union(B)
print("Union using union():", result2)

result3 = A.intersection(B)
print("intersection using intersection():",result3)

result4 = A-B
print("difference a and b",result4)

result5=A.symmetric_difference(B)
print("symmetric difference",result5)'''

'''7.Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's 
method.

d={i:1 for i in range(1,11,1)}
print(d)'''

'''8 Print all the keys and values of a dictionary.

data={
    "name":"sakshi",
    "id":101,
    "hoobies":"Dancing"
     }
print(data)'''



''' 9.Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries
data={
    'a':1,
    'b':2,
    'c':3
}

datas={
    'a':4,
    'd':5,
    'e':6
}
data.update(datas)
print(data)'''

'''10.How to check whether a key is existing in a dictionary or not.
user_input=input("enter the value:-")
dict={
    "name":"sakshi",
    "age":17,
    "Talent":"Dancing"
}
if user_input in dict():
    print("key is existing")
else:
    print("key is not existing")'''


'''11.How can we have two variables refering to a single list, set and dictionary
l=[10,20]
list=l
list.append(30)
print(list)

set={20,30}
list=set
set.add(40)
print(list)

dict={
    "name":"sakshi",
    "id":101
}
dicts=dict
dicts["city"]=["jetpur"]
print(dicts)'''

'''12 Use all the case methods of strings.

s1="sakshi"
print(s1.upper())

s2="SAKSHI"
print(s2.lower())

print(s1.capitalize())

print("hello sakshi".title())

S=s1.replace("sakshi","hello")
print(S)

print(s2.count(S))'''

'''13.Use all the validation methods of strings
user=input("enter a string")
if user.isalpha():
    print("string contain only letter")
elif user.isdigit():
    print("string is only digit")
elif user.isalnum():
    print("string is only letter and digit")
else:
    print("not used of special character")'''


'''14  Create a text document using the justification methods'''

'''15How to split a string with a substring?
string="python is interpreteing language"
print(string.split())'''

'''16.Take a multiline string and split each line of this string as an element of the list

str="""this is one line
this is two line
this is three line"""

print(str.splitlines())'''

'''17How to replace a string with a substring? 
s1="sakshi is talented"
s2=s1.replace("sakshi","Ravi")
print(s2)'''

'''18.How to join multiple strings with a substring?
s1="""hello world
hyy sakshi
hyy het"""

s2="-"

result=(s2.join(s1))
print(result)'''

'''19 How to make partition of a string
str="welcome to a string"
x=str.partition("el")
print(x)'''

'''20 How to find the no of occurences of a substring?
str="hellohellohello"
print(str.count("he"))'''

'''21Create a transaction no of 5 digits. Even though the given number is 15.
num="123456781234567"
print(num[0:5])'''

'''22.Convert all the data structures to other data structures.
list1=[11,22,33,44,55]
lists=tuple(list1)
print(lists)

tuple=(1,2,3,4,5)
tuples=list(tuple)
print(tuples)

d=dict(enumerate(list1))
print(d)

st=str(list1)
print(st)'''



'''23 Get the last element of the list, tuple and string
list=[1,2,3,4,5]
print(list[4:])

tuple=(2,4,5,7,8,9,3,19)
print(tuple[7:])

str="sakshi"
print(str[5:])'''

''' 24.Get last 3 elements of the list, tuple and string.
list=[4,5,7,8,9,44,56]
print(list[4:])

tuple=(44,55,78,56,34,56,78,66,89,90)
print(tuple[7:])

str="siddhi"
print(str[3:])'''

'''25.Get first 5 elements of list, tuple and string
list=["mango","banana","kiwi","pineapple","watermelon","strawberry","guava"]
print(list[0:5])

tuple=("potato","tomato","chillies","brinjal","bittergourd","lemon","ladyfinger")
print(tuple[0:5])

str= "python is high level language"
print(str[0:5])'''


'''26.Get all the elements excluding first and last elements from list, tuple and string.
list=[22,33,44,55,66,77,55,33,99]
print(list[1:8])

tuple=[33,66,90,45,65,33,24,56,78,90,76,34]
print(tuple[1:11])

str="off campus"
print(str[1:9])'''

'''27Get all the elements in a list using : operator.
list=[44,78,89,90,67,43,56,78,54,44]
print(list[0:])'''

'''28. Get last 5 elements from a list of 1 to 10 using negative indexing.
list=[1,2,3,4,5,6,7,8,9,10]
print(list[-5:])'''

'''29.Get 4 elements of the list excluding last 2 elements using negative indexing.
list=[1,2,3,4,5,6,7,8,9,10]
print(list[-10:-6])'''

'''30.Convert a list of tuple to dictionary.
a=[("a",1),("b",2),("c",3)]
result=dict(a)
print(result)'''

'''31. Iterate through all the data structures.
b=(["a",6],["b",7],["c",8])
result=dict(b)
print(result)'''


'''32.Use the overloaded operators ‘+’ and ‘*’ with list, tuple and string.
list=[1,2,3,4,5,6,7]
print(list * 2)

list1=[1,2,3,4,5]
list2=[7,8,9,2,4]
print(list1+list2)

tuple=(4,5,6,7)
print(tuple*2)

tuples=(8,9,10,110,45)
print(tuple+tuples)

str="hello"
print(str*2)

str1="sakshi"
print(str+str1)'''

'''33.Use the in, not in, is and is not operators with data structures
list=["apple","banana","kiwi","orange","strawberry"]
print("pineapple" in list)
print("kiwi"not in list)
print("orange" in list)

list1=["potato","tomato","bittergourd"]
list2=["bmw","scorpio","mercedes","potato"]
print(list1 is list2)
print(list1 is not list2)'''




'''34 Create a dictionary as following. {'a':1, 'b':2, 'c':3, 'd':4, 'e':5....'y':25, 'z':26}
data={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26

}
print(data)'''

'''35.There are two lists [1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]. Get a third list from these two lists as [12,14,16,18,20,22,24,26,28,30].
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17,18,19,20]
list3=[]
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)'''

'''36.Get Square of all the elments in a list from 1 to 10 numbers.
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for x in list1:
    list2.append(x**2)
    print(list2)'''

'''37. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7].
list1=[1,2,3,4,5]
list2=[4,5,6,7]
list3=[x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(list3)'''

'''38.Fetch 5 which is the value of ‘e’ from below which is marked in red.x = {‘a’:1, ‘b’:2, ‘c’:3,’d’:[1,2,3,4,(5.6.7,{‘e’:5}),10,15], ‘f’:45}
x = {'a':1, 'b':2, 'c':3, 'd':[1,2,3,4,(5,6,7,{'e':5}),10,15], 'f':45}
result = x['d'][4][3]['e']
print(f"Result: {result}")

x = {'a':{'b':[1,2,(3,4,{'c':3,'d':4,'e':[1,2,3]})], 'x':[1,2,3,4]}
result1 = x['d'][3][4]['e']
print(f"result:{result1}")

x=[1, 2, (3, 4, 5, {'a':1, 'b':[2,3,4,(5,6)]})]
result2=x[2][3]['b'][3][1]
print(f"result:{result2}")

x = {True:[1,2,3,{'a':1,'b':2}],False:[(2,3,4,5,{1:2})]}
result3=x[False][0][4][1]
print("Result:",result3)

x = {1:2,2:3,3:4,4:{'a':'b','c':'d','e':'f','f':[1,2,3,{1:9,3:8}]}
result4=x[4]['f'][3][1]'''    


'''39.Create a function for string that will check whether a string is having the first letter as Capital and not anyother letter is capital.
def checkstring( text:str)-> bool:
    return bool(text) and text == text.capitalize()
    
print(checkstring("Hello"))
print(checkstring("hello"))
print(checkstring("H"))'''


'''40.Format a string with inputs passed using the index and keyword techniques.

first="hello{1},you have any message passed {0}".format("alice",5)
print(first)'''

'''41.
class Student:

    def __init__(self,name,regno,rollno,std,year):

        self.marks=[]
        self.result=False

        if name.isalpha():
            self.name=name

        if regno.isalnum():
            self.regno=regno

        if rollno.isdigit():
            self.rollno=rollno

        if std.isdigit():
            self.standard=std

        if year.isdigit():
            self.admission_year=year

    def add_marks(self,d):

        result="PASS"

        for sub,mark in d.items():

            if mark>100:
                print("Invalid Marks")
                return

            if mark<40:
                result="FAIL"

        d["Result"]=result

        self.marks.append(d)

    def generate_result(self):

        total=0
        passing=0
        obtained=0
        final="PASS"

        print("*"*60)
        print("Name :",self.name)
        print("Roll No :",self.rollno)
        print("Standard :",self.standard)
        print("*"*60)

        print("{:<15}{:<15}{:<15}{:<15}".format(
        "Subject","Total","Passing","Obtained"))

        for d in self.marks:

            for k,v in d.items():

                if k!="Result":

                    print("{:<15}{:<15}{:<15}{:<15}".format(
                    k,100,40,v))

                    total+=100
                    passing+=40
                    obtained+=v

            if d["Result"]=="FAIL":
                final="FAIL"

        print("*"*60)
        print("Total :",total)
        print("Passing :",passing)
        print("Obtained :",obtained)
        print("Percentage :",obtained/total*100)
        print("Result :",final)


s=Student("Sakshi","GTU123","1","6","2026")

s.add_marks({
"Python":78,
"Java":89,
"C":67
})

s.generate_result()'''







    

















































































      
