
#pip3 search mysql-connect
#sudo pip3 install mysql-connector
#mysql server ip is:192.168.1.140
#create user python@192.168.1.75 ==> is a server wich i want to connect
# Remotely connect:::                                                                           --
# /etc/mysql/mysql.conf.d/mysqld.cnf                                                            --                                                                                             --
# bind-address            = 127.0.0.1   ==>  bind-address            = 0.0.0.0 

#best practice for creating user in mysql
#create user "pydata"@"%" identified by 'password';
#GRANT ALL PRIVILEGES ON python.* TO 'pydata'@'%';
#FLUSH PRIVILEGES;


import queue
from sqlite3 import Cursor
import mysql.connector

print ("connecting")

cnx=mysql.connector.connect(user="pydata",password="password",host="192.168.1.100",database="python")

print("connected to db")

age=int(input("please write yourn age:  "))
name=input("please write your name: ")


cursor=cnx.cursor()

cursor.execute("insert into t1 (name,age) values (\'%s\',\'%s\')" %( name,age))
cnx.commit()
query="select * from t1"
cursor.execute(query)
for (id,name,age) in cursor:
    print("id is : %i ..... name is : %s..........age is : %s "%(id,name,age))

cnx.close()

###############################################################################################
# import queue
# from sqlite3 import Cursor
# import mysql.connector

# print ("connecting")



# cnx=mysql.connector.connect(user="pydata",password="password",host="192.168.1.100",database="python")

# print("connected to db")

# name=input("please write name: ")
# age=input("please write your age: ")

# cursor=cnx.cursor()
#---------------------------------------------------------------------------
# seek=str(input("which name are you looking for??! "))
# query=f"select * from t1 where name = '{seek}'"
# print(query)
# cursor.execute(query)
# for x in cursor:
#     print (x)
#---------------------------------------------------------------------------------
# for (id,name,age) in cursor:
#     if name ==seek:
#         print("id is : %i ..... username is : %s..........age is : %s "%(id,name,age))
#         break;
#     else:
#         print("it is not exist")
# cnx.close()