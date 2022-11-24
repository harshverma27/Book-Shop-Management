import mysql.connector as mc
mydb = mc.connect(user="root", host="localhost", passwd="root",database="bookshop")
mycursor = mydb.cursor()

mycursor.execute("CALL sys.table_exists('bookshop','book', @exists); SELECT @exists;")
for i in mycursor:
    print(i)