from viewSQLDB import viewSQLDB

def menu():
    return showMainMenu()

def showMainMenu() -> int:
    print(f'''\u001b[1;32;40m
    -------------------
    MAIN MENU
        1. PlayerView
        2. DeveloperView (require a password)
        3. Exit Program
    -------------------
    ''')    
    userResponse = input("SELECTION: ")
    return userResponse

def showPlayerViewMenu() -> int:
    print(f'''\u001b[1;32;40m
    -------------------
    PLAYER VIEW MENU
        1. View specifics of the database
        2. Exit to main menu
    -------------------
    ''')
    userResponse = input("SELECTION: ")
    return userResponse

def showDeveloperViewMenu() -> int:
    print(f'''\u001b[1;32;40m
    -------------------
    DEVELOPER VIEW MENU
        1. Update a table
        2. Delete a row from a table
        3. Insert a new row into a table
        4. View specifics of the databse
        5. Exit to main menu
    -------------------
    ''')
    userResponse = input("SELECTION: ")
    return userResponse