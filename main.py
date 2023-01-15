# import required modules
from librariesSetup import * 
from mysqlSetup import * 
from colorama import Fore, Back, Style
from maskpass import *
from admin import *
from user import *

# header
print(Fore.BLUE, Style.BRIGHT)
print("::::BOOK SHOP MANAGEMENT::::")
print(Fore.RESET,Style.NORMAL)

# set colorscheme to White.
print(Fore.WHITE,Style.BRIGHT)

# get choices from user (admin or visitor)
print("Who are you?\n1 For Admin.\n2 For Visitor.\n3 To Exit")

while True:
    try:
        choice = int(input("Enter Choice:- "))

    except ValueError:
        print("Enter Integer Only.")
        continue

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

    # if user decides to exit, the loop will break
    elif choice == 3:
        break;
        
    # invalid choice will result in error.
    else:
        print("Invalid Choice.")

    break
        
print("Thank You for using my project.")
print(Fore.RESET,Back.RESET,Style.NORMAL)

#Created by Harsh Verma (github.com/harshverma27)