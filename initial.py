import mysql.connector as mc
mydb = mc.connect(user="root", host="localhost", passwd="root")
mycursor = mydb.cursor()

# This fucntion creates a database in mySQL
def mysqlSetup():
    print("Creating Databases :- ")
    mycursor.execute("create if not exits database bookshop;")
    mycursor.execute("use bookshop")
    print("Database Created.")

    print("Creating Tables")
    mycursor.execute("create table if not exists book(book_id int primary key, book_name varchar(100) not null, book_author varchar(50), genre varchar(30), book_price int );")
    mycursor.execute("create table if not exists issue(book_id int, client_name varchar(30), foreign key (book_id) references book(book_id));")
    mycursor.execute("create table if not exists buyrequests(book_id int, client_name varchar(30), foreign key (book_id) references book(book_id));")
    mycursor.execute("create table if not exists acceptedrequests(book_id int, foreign key (book_id) references book(book_id), client_name varchar(30));")
    print("Table Created.")

try :
    mycursor.execute("use bookshop;")
except:
    mysqlSetup()

#Created by Harsh Verma (github.com/harshverma27)