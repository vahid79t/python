print ("hello world")
age=input("please entert your age: ")
age=int(age)
print(age)
print(type(age))
#######################################################
age=input("please entert a number: ")
age=int(age)
print(age)
print(type(age))
if age==2:
    print("this is two")
elif age==3:
    print("this is 3")
else:
    print("get out")
#######################################################
import math
import random
a=math.sin(0.6)
b=random.random()
c=random.randrange(1,6)
print(a,",",b, ",",c)
#######################################################
def greeting(name):
    print("hello,how are you...",name)

name=input("what is your name: ")
greeting(name)
#######################################################
def mosbat(a,b):
    mosbat=a+b
    return mosbat

first_num=input("write a number : ")
first_num=int(first_num)
second=input("write second number : ")
second=int(second)
javab=mosbat(first_num,second)
print(javab)
#######################################################
for x in range(1,10):
    print("this is :",x)
##########################################################
from pydoc import cli
import random
pc_guess=random.randrange(1,101)
#print(pc_guess)
#print(type(pc_guess))
client_gues=input("please guess the pc number: ")
client_gues=int(client_gues)
#print(client_gues)
while client_gues != pc_guess:
    if pc_guess > client_gues:
        print("your answer is less than pc, try again")
        client_gues=input("please guess the pc number: ")
        client_gues=int(client_gues)
    else :
        print("your answer is bigger than pc, try again")
        client_gues=input("please guess the pc number: ")
        client_gues=int(client_gues)
if client_gues == pc_guess:
    print("that is the answer!!!!!,  well done")
#########################################################
a='asalam'
b=a[3]
print(b)
c=len(a)
print(c)
m="this a testing sentences"
s_1=m[0]
s_2=m[2]
s_3=m[:3]
s_4=m[3:8]
s_5=m[-1]
s_6="M"+m[1:]
rang=[s_1,s_2,s_3,s_4,s_5,s_6]
for i in rang:
    print(i)
##########################################################
name=input("please write your name:  ")
family=input("please write your family:  ")
m="this a testing sentences"
s_1="vahid".upper()
s_2='salam khobi khabara'.count("a")
s_3="VAHID".lower()
s_4='salam khobi khabara'.find("a",2)
s_5="  vahid  tavakkoli   ".strip()
rang=[s_1,s_2,s_3,s_4,s_5]
for i in rang:
    print(i)
print("hello %s how are you" %name)
print("hello %s how are you??,is your family %s ??" %(name,family))
#############################################################
l=[1,2]
l.append('new')
print(l)
l.extend(["vahid","ali",1])
print(l)
p=["tavakoli","banizi"]
r=l+p
print(r)
del l[0]
print(l)
p.pop()
print(p)
l.remove("ali")
print(l)
###############################################################
l=[1,2,3,4,5,6,7,8,9]
min=min(l)
max=max(l)
print(min,max)
average=sum(l)/len(l)
print(average)
###############################################################
f2e=dict()
f2e["yek"]="one"
f2e["do"]="two"
f2e["se"]="three"
f2e["char"]="four"
print(f2e["do"])
dictionarynew={}
ghad={"vahid":180,"majid":170}
print("keys for f2e::",f2e.keys())
print("values for f2e::",f2e.values())

print("keys for f2e::",list(f2e.keys()))
print("values for f2e::",list(f2e.values()))

print("do" in f2e)
##############################################################
from curses import keyname
from itertools import count
from re import S
from tokenize import String


text="hello every one this is the sample test for testing dictionary"
counter=dict()
for letter in text:
    print(letter)
    if letter in counter:
        counter[letter]+=1
        #counter[letter]=counter.get(letter,0)+1   #getting
    else:
        counter[letter]=1
print(counter)
for this_one in  list(counter.keys()):
    print("%s appears %s times" %(this_one,counter[this_one]))
####################################################################
email="vahid79t@gmail.com"
s=email.split("@")
print(s)
name,domain=email.split("@")
print(name)
print(domain)
vazne={'ali':50,'majid':60,'vahid':60}
print(vazne.items())
print(list(vazne.items()))
for (name,vazn) in list(vazne.items()):
    print("name is: %s and vazn is %s  "%(name,vazn))

#####point

for k,v in dictionary.item():
        <>
#####point
#####################################################################


counter=sum=0
myfile=open("/home/vahid/Desktop/pythontest")
for line in myfile:
    counter+=1
    this_num=float(line.strip())
    sum=sum+this_num
    print(sum)
    #print(line.strip())
print(sum)
print(counter)
average=sum/counter
print(average)


myfile2=open("/home/vahid/Desktop/pythontest2","w")
myfile2.write(str(average))
myfile.close()
myfile2.close()
# m=myfile.read()
# print(m)
# myfile.close()

#myfile.readline()
####################################################################
from asyncore import read
import csv
import statistics
with open("/home/vahid/Desktop/temp.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
        name=row[0]
        grades=row[1:]
        print(name)
        print(grades)
        these_grades=list()
        for grade in row[1:]:
            these_grades.append(int(grade))
            print(name,grade,these_grades)
        print("average of %s is %5.2f"%(name,statistics.mean(these_grades)))
###############################################################################################
from csv import reader
from hashlib import sha256
hash_password_to_password = {}
for password in range(1,10000):
    hashing_number = sha256(b'%i'% password).hexdigest()
    hash_password_to_password[hashing_number] = password
with open('D:/iliya/users password.csv') as f:
    psswords_singer = reader(f)
    for row in psswords_singer:
        name_users = row[0]
        for key in row[1:]:
            print(name_users,':',hash_password_to_password[key])
