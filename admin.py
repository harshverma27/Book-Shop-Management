import mysql.connector as mc
mydb = mc.connect(user="root", host="localhost", passwd="root", database='bookshop')
mycursor = mydb.cursor()

# this fucntion runs query in SQL shell, and prints the output.
def runQuery(s: str):
    mycursor.execute(s)
    for i in mycursor.fetchall():  # type: ignore
        print(i, end="\n")


def menu():
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
            print("Choice Should be in integer and between 1 & 6.")
            # this will make loop run forever until required choice is given.
            choice = 0

    return choice

def main():

    # this forever loop only gets exitted using choice 5.
    while True:

        choice = menu() # choices gets choosen using menu function

        if choice == 1: # To view Data.
            runQuery("Select * from book;")

        if choice == 2: # To Enter Data.

            print("Format: Book ID - Book Name - Book Author - Genre - Price")
            book_id = input("Enter Book ID: ")
            book_name = input("Enter Book Name: ")
            book_author = input("Enter Book Author Name: ")
            genre = input("Enter Book Genre: ")
            price = input("Enter Book Price:")

            # this below code runs the query to enter data into database;
            try:
                runQuery("insert into book values("+book_id+',"'+book_name+'","'+book_author+'","'+genre+'",'+price+');')

                mydb.commit() #commit() function saves the chages we made to mysql-server.
                print("Record Entered.\n")

            except Exception as e:
                print("Error Found :", e)


        if choice == 3: # To update Data
            updateid = input("Whose Record you want to update(Enter Student ID): ")
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
            print("Book ID, Book Name, Client Name")
            runQuery("select issue.book_id, book_name, client_name from issue, book where book.book_id = issue.book_id;")

        if choice == 6: # To check buy requests
            print("Book ID, Book Name, Client Name")
            runQuery("select buyrequests.book_id, book_name, book_price, client_name from buyrequests,book where buyrequests.book_id = book.book_id;")

            print("Which request do you want to accept? ")
            secondChoice = input("Enter Book ID: ")

            try:
                runQuery("delete from buyrequests where book_id = "+secondChoice+";")
                mydb.commit()
                print("Book Selled.")
            
            except:
                print("Error.")

        if choice == 7: # to exit.
            break
        
main()
