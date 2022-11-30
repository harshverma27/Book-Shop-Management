import mysql.connector as mc
from prettytable import PrettyTable
mydb = mc.connect(user="root", host="localhost", passwd="root", database='bookshop')
mycursor = mydb.cursor()
adminpasswd = "bookshop"

# this fucntion runs query in SQL shell, and prints the output.
def runQuery(s: str):
    mycursor.execute(s)
    for i in mycursor.fetchall():  # type: ignore
        print(i, end="\n")
    return mycursor.fetchall()
 
# this function runs query in SQL shell, and add the data to a variable in a tabular format.
def runQueryAddData(s: str,table):
    mycursor.execute(s)
    for i in mycursor.fetchall(): # type: ignore
        table.add_row(i)
    
def admin_menu():
    choices = """\nWhat Do You Want To Do?\n1 To View Books.\n2 To Enter Book Data.\n3 To Update Book Data.\n4 To Delete Book Data.\n5 To Check Issues.\n6 To check buy requests.\n7 To EXIT"""  # All available choices
    print(choices)

    # the below code inputs chocie ensuring it is between 1 and 5.
    choice = 0
    while choice == 0:
        try:  # use try-except to make it easier.
            choice = int(input("Enter Choice: "))
            if choice < 1 or choice > 7:
                # Raise error if choice is not between 1 and 5 to run excpet part.
                raise TypeError

        except:
            print("Choice Should be in integer and between 1 & 7.")
            # this will make loop run forever until required choice is given.
            choice = 0

    return choice

def admin_main():

    # this forever loop only gets exitted using choice 5.
    while True:

        choice = admin_menu() # choices gets choosen using menu function

        if choice == 1: # To view Data.

            # first, create a table using pretty table module
            myTable =  PrettyTable(["Book_id","Book_Name","Book_Author","Genre","Book_Price"])

            # then, add data to it.
            runQueryAddData("select * from book", myTable) 

            # finally, print the table.
            print(myTable)

        if choice == 2: # To Enter Data.

            # get values from admin.
            print("Format: Book ID - Book Name - Book Author - Genre - Price")
            print("Note that Book ID and Book Name cannot be blank.")
            book_id = input("Enter Book ID: ")
            book_name = input("Enter Book Name: ")
            book_author = input("Enter Book Author Name: ")
            genre = input("Enter Book Genre: ")
            price = input("Enter Book Price:")
            if price == "": price = "NULL"

            # this below code runs the query to enter data into database;
            try:
                runQuery("insert into book values("+book_id+',"'+book_name+'","'+book_author+'","'+genre+'",'+price+');')

                mydb.commit() #commit() function saves the chages we made to mysql-server.
                print("Record Entered.\n")

            except Exception as e:
                # if we get error, we will inform user accordingly.
                if str(e)[0:12] == "1062 (23000)" : #primary key error
                    print("Book with ID "+str(e)[31]+" already exists.")

                elif str(e)[0:12] == "1054 (42S22)" : #typeerror
                    print("Price Shouldn't Contain Charcaters.")

                else:
                    print(e)
                print("Record Not Inserted.")


        if choice == 3: # To update Data
            updateid = input("Whose Record you want to update(Enter Book ID): ")
            print("What Do want to Update:-\n1 For Book Name.\n2 For Book Author.\n3 For Genre.\n4 For Book Price")
            update =  int(input("Enter Choice: "))

            # checking of choice is required to prevent unwanted error.
            if update < 1 or update > 4:

                print("Invalid Choice")
                continue  # here, "continue" stops the loop's current run and does a fresh start.

            if update == 1: #new name
                updated = input("Enter New Book Name: ")
                runQuery("update book set book_name = \""+updated+"\" where book_id = "+updateid+";")

            if update == 2: #new author
                updated = input("Enter New Author Name: ")
                runQuery("update book set book_author = \""+updated+"\" where book_id = "+updateid+";")

            if update == 3: #new genre
                updated = input("Enter New Genre: ")
                runQuery("update book set genre = \""+updated+"\" where book_id = "+updateid+";")

            if update == 4: #new price
                updated = input("Enter New Price: ")
                runQuery("update book set book_price = "+updated+" where book_id = "+updateid+";")   

            mydb.commit()
            print("Record Updated\n")

        if choice == 4: # to delete record
            deleteid = input("Whose Record you want do delete(Enter Book ID): ")

            try:
                runQuery("delete from book where book_id = "+deleteid+";")
                mydb.commit()
                print("Record Deleted")
                
            except Exception as e:
                print("Error: ",e)

        if choice == 5: # To check issues

            # create a table using pretty table module
            myTable = PrettyTable(["Book ID", "Book Name", "Client Name"])

            # add data to it.
            runQueryAddData("select issue.book_id, book_name, client_name from issue, book where book.book_id = issue.book_id;", myTable)
            
            # print the table
            print(myTable)

        if choice == 6: # To check buy requests

            # print table first.
            myTable = PrettyTable(["Book ID", "Book Name","Book Price", "Client Name"])
            runQueryAddData("select buyrequests.book_id, book_name, book_price, client_name from buyrequests,book where buyrequests.book_id = book.book_id;",myTable)
            print(myTable)

            # now, we will ask admin, which buy request he wants to accept.
            print("Which request do you want to accept? (Leave Blank for non.)")
            secondChoice = input("Enter Book ID: ")

            # if admin input a book_id to accept, then
            if secondChoice != "":
                try:
                    # first we will delete its record from buyrequsts;
                    runQuery("delete from buyrequests where book_id = "+secondChoice+";")

                    # then we will insert its record into acceptedrequests table.
                    runQuery("insert into acceptedrequests values("+secondChoice+");")

                    # then we will save our changes and infrom admin.
                    mydb.commit()
                    print("Book Selled.")
                
                except Exception as e:
                    print("Error Found: ",e)

        if choice == 7: # to exit.
            break

        finalChoice = input("Do You want to Continue or Not (Y or N):-")

        if finalChoice.lower() == 'n' or finalChoice.lower() == "no":
            break

        elif finalChoice.lower() == 'y' or finalChoice.lower() == "yes":
            continue
        
        else:
            print("Invalid Choice.")
            break

#Created by Harsh Verma (github.com/harshverma27)