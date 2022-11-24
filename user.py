import mysql.connector as mc
from prettytable import PrettyTable
mydb = mc.connect(user="root", host="localhost", passwd="root",database='bookshop')
mycursor = mydb.cursor()

# this function runs query in SQL shell, and prints the output.
def runQuery(s: str):
    mycursor.execute(s)
    for i in mycursor.fetchall():  # type: ignore
        print(i, end="\n")


# this function runs query in SQL shell, and adds the data to a table insteading of printing it.
def runQueryAddData(s: str,table):
    mycursor.execute(s)
    for i in mycursor.fetchall(): # type: ignore
        table.add_row(i)
    

# this function checks if a 'id' is in 'book_id' of table buyrequests.
def checkBookID(id: int):
    mycursor.execute("select book_id from buyrequests;")
    for i in mycursor.fetchall():  # type: ignore
        for j in i:
            if int(j) == int(id):
                return True
                break
    return False
                  
                    
# the menu fucntion is responsible for choice selection
def user_menu():
    choices = """\nWhat Do You Want To Do?\n1 To View Books.\n2 To Ask book for issue.\n3 To Submit Book.\n4 To Buy Book.\n5 to Exit."""  # All available choices
    print(choices)

    # the below code inputs chocie ensuring it is between 1 and 5.
    choice = 0
    while choice == 0:
        try:  # use try-except to make it easier.
            choice = int(input("Enter Choice: "))
            if choice < 1 or choice > 5:
                # Raise error if choice is not between 1 and 5 to run excpet part.
                raise TypeError

        except:
            print("Choice Should be in integer and between 1 & 5.")
            # this will make loop run forever until required choice is given.
            choice = 0

    return choice

# this is the main function which does the main work of working on the choices and both frontend and backend
def user_main():

    # this forever loop only gets exitted using choice 5.
    while True:

        choice = user_menu() # choices gets choosen using menu function

        if choice == 1: #To View All books data:
            print("\n1 to View All Books\n2 To see Filters")
            secondChoice = int(input("Enter Choice: "))
            
            if secondChoice == 1: # to view all books

                # create a table using PrettyTable Module
                myTable = PrettyTable(["Book_id","Book_Name","Book_Author","Genre","Book_Price"])
                
                # add data to it.
                runQueryAddData("select * from book;",myTable)

                # print it
                print(myTable) # print it.

            if secondChoice == 2: # to view books in filter

                print("\n1 To Get by Genre\n2 To Get By Author\n3 To Get by Price") # all available flters

                # get choice of filter
                thirdChoice = int(input("Enter Choice: "))
                
                # filter by genre
                if thirdChoice == 1:

                    # get unique genres uing MySQL
                    myTable = PrettyTable(["Genre"])
                    runQueryAddData("select distinct genre from book order by genre;",myTable)
                    print(myTable)
                    
                    # get choice of genre
                    print("\nWhich Genre You want to See: ")
                    fourthChoice = input("Enter Choice: ")

                    # print according to choice;
                    myTable = PrettyTable(["Book_ID", "Book_Name", "Book Author", "Genre", "Price"])
                    runQueryAddData("select * from book where genre = '"+fourthChoice+"';",myTable)
                    print(myTable)

                
                if thirdChoice == 2:

                    # get unique authors using MySQL
                    print("\nAvailable Authors:: ")
                    myTable = PrettyTable(["Authors"])
                    runQueryAddData("select distinct book_author from book;",myTable)
                    print(myTable)

                    # get choice
                    print("\nWhich Author You Want: ")
                    fourthChoice = input("Enter Choice: ")

                    # print according to choices
                    myTable = PrettyTable(["Book_ID", "Book_Name", "Book Author", "Genre", "Price"])
                    runQueryAddData("select * from book where book_author ='"+fourthChoice+"';",myTable)
                    print(myTable)

                if thirdChoice == 3:
                    
                    # in price filter, we basically adjust books in ascending price order. 
                    myTable = PrettyTable(["Book_ID","Book_Name", "Book Author", "Genre", "Price"])
                    runQueryAddData("select * from book order by book_price;",myTable)
                    print(myTable)

        if choice == 2: # to ask book for issue

            # get book details, to update issue table
            clientname = input("Enter Your Name: ")
            issueid = input("Enter Book_ID of the book you want: ")

            # try updating table
            try:
                runQuery("insert into issue values("+issueid+",'"+clientname+"');")
                mydb.commit() # here, commit() saves changes we made to database;
                print("Book Issued\n")

            except:
                print("Wrong/Invalid Book ID")


        if choice == 3: # To submit book
            
            #get book details, to update issue table
            submitid = input("Enter Book ID of book which you want to submit: ")

            #try updating table
            try:
                runQuery("delete from issue where book_id = "+submitid+";")
                mydb.commit()
                print("Book Submitted.\n ")

            except:
                print("Wrong Book ID.")
        
        
        if choice == 4: # to buy a book

            # in buy book, we have two options one to send a buy-request and other to check if you request was approved.
            # get choice
            print("\nWhat Do you want to do?\n1 To buy book.\n2 To check buy status.")
            secondChoice = int(input("Enter Choice: "))

            # choice 1, to send a request.
            if secondChoice == 1:

                # we will basically insert record in a 'buyrequests' table.
                # get values
                buyid = input("Enter Book ID of book you want to buy:: ")
                clientname = input("Enter Your Name:: ")

                # try inserting them;
                try:
                    runQuery("insert into buyrequests values("+buyid+",'"+clientname+"');")
                    mydb.commit()
                    print("Buy Request Sent.")

                except:
                    print("Error")
            
            # choice 2, to check if request was approved.
            if secondChoice == 2:

                # we will check if the same book_id is still in 'buyrequests' or not. Because if admin approves, it will delete the record from 'buyrequests'
                # get values
                buyid = input("Enter Book ID of book whose request you sent? ")

                # check if any book_id matches to buyid.
                if checkBookID(int(buyid)):
                    print("Request Not approved yet.")
                else:
                    print("Request Approved.")
            
        
        if choice == 5: # to exit.
            exit()

        finalChoice = input("Do You want to Continue or Not (Y or N):-")
        if finalChoice.lower() == 'n' or finalChoice.lower() == "no":
            break
            
#Created by Harsh Verma (github.com/harshverma27)