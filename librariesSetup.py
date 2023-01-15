import os

# This function installs all required libraries.
def librarySetup():

    # get installed libraries...
    libraries = os.popen("pip list").read()

    # check if libraries are installed...
    if ("colorama" not in libraries) or ("maskpass" not in libraries) or  ("prettytable" not in libraries) or ("mysql-connector-python") not in libraries:
        
        # notify user.
        print("Installing Libraries.")

        # colorama library..
        if "colorama" not in libraries:
            print("Installing Colorama")
            os.system("pip install colorama -q")
            print("Installed Colorama")
        
        #maskpass library
        if "maskpass" not in libraries:
            print("Installing Maskpass")
            os.system("pip install maskpass -q")
            print("Installed Maskpass")

        #prettytable library
        if "prettytable" not in libraries:
            print("Installing PrettyTable")
            os.system("pip install prettytable -q")
            print("Installed PrettyTable")
        
        #mysql-connector library
        if "mysql-connector-python" not in libraries:
            print("Installing MySQL Connector")
            os.system("pip install mysql-connector-python -q")
            print("Installed MySQL Connector")

        print("Installed Libraries")

# install required libraries.
librarySetup()