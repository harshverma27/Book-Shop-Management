import mysql.connector as mc
mydb = mc.connect(user="root", host="localhost", passwd="root")
mycursor = mydb.cursor()

# this function checks if a database exist in mysql.
def checkDatabaseExists():
    mycursor.execute("show databases like 'bookshop';")
    if(mycursor.fetchall() == []):
        return False
    else:
        return True

# This fucntion creates a database in mySQL
def createDatabase():
    print("Creating Databases :- ")
    mycursor.execute("create database bookshop;")
    mycursor.execute("use bookshop")

# This function checks if a table exists in mySQL
def checkTableExists():
    mycursor.execute("use bookshop")
    mycursor.execute("show tables like 'book'")
    if(mycursor.fetchall() == []):
        return False
    else:
        return True

# This fucntion creates required tables in mySQL
def createTables():
    #Create all tables in databases;
    print("Creating Table :- ")
    mycursor.execute("create table book(book_id int primary key, book_name varchar(100), book_author varchar(30) not null, genre varchar(30), book_price int not null);")
    mycursor.execute("create table issue(book_id int, client_name varchar(30), foreign key (book_id) references book(book_id));")
    mycursor.execute("create table buyrequests(book_id int, client_name varchar(30), foreign key (book_id) references book(book_id));")
    mycursor.execute("cretae table acceptedrequests(book_id int, foreign key (book_id) references book(book_id));")

#Created by Harsh Verma (github.com/harshverma27)