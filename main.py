# import both admin and user files and required modules
from maskpass import *
from admin import *
from user import *

# get choices from user (admin or visitor)
print("Who are you?\n1 For Admin.\n2 For Visitor.")
choice = int(input("Enter Choice:- "))

# if user chooses admin then he needs to enter password.
if choice == 1:

    # get password
    passwd = askpass("Enter Password: ")
    if passwd == adminpasswd: # check password
        admin_main()
    else:
        print("Wrong Password.")

# if user chooses visitor, then he would be converted to visitor.
elif choice == 2:
    user_main()

else:
    print("Invalid Choice.")
    