import math
print(math.floor(23.4))
# a=1
# b=2
# c=a+b
# print(type(c))
# d="isfkaddms"
# print(type(d))
# a="this is my python code"
# print(a.capitalize())
# print(a.find("my"))
# print(a.upper())
# print(a.lower())
# list
# item=["shashank",7.7,[7,78]]
# item[2][1]=67
# print(item)
# tuple 
# tup1 =(12,123,32)
# print(tup1)
# dictionary
dict1={}
dict1['virat']= 100
dict1['schine']=200
print(dict1.get('virat'))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
# set
list1=[1,3,2,2,1,4]
se= set(list1)
print(se)
# type casting
a=1
b=3
c="stdp"
print(str(a)+str(b)+c)
print("a + b",a+b)
print("a / b",int(a/b))
# input
var= int(input())
print(var)
# if else elif
if var >= 18:
    print("can vote")
elif var ==17:
    print("vote next year")
else :
    print("cant vote")
# loops
for i in range(0,100):
    print(i)
i=0
while(i<101):
    print(i)
    i=i+1  
# function
def avg(n1,n2):
    avg=(n1+n2)/2
    return avg
# call functiion
print(avg(3,6))
# try exeption
try:
    print(i)
except Exception as e:
    print(e)
# file handling
f=open("file.txt","w")
f.write("hi I didnt write any thing in file")
f.close()
f=open("file.txt","r")
content=f.read()
print(content)
f.close()