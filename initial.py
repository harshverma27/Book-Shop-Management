import mysql.connector as mc
mydb = mc.connect(user="root", host="localhost", passwd="root")
mycursor = mydb.cursor()

#Create databases;
print("Creating Databases :- ")
mycursor.execute("create database bookshop;")
mycursor.execute("use bookshop")

#Create all tables in databases;
print("Creating Table :- ")
mycursor.execute("create table book(book_id int primary key, book_name varchar(100), book_author varchar(30) not null, genre varchar(30), book_price int not null);")
mycursor.execute("create table issue(book_id int, client_name varchar(30), foreign key (book_id) references book(book_id));")
mycursor.execute("create table buyrequests(book_id int, client_name varchar(30), foreign key (book_id) references book(book_id));")

#Notify user.
print("All Done.")
print("You can insert book data using 'admin.py' file.")


#Created by Harsh Verma (github.com/harshverma27)