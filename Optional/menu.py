from viewSQLDB import usageMessage

def menu():
    return showMainMenu()

def showMainMenu() -> int:
    print(f'''
        MAIN MENU
            1. PlayerView
            2. DeveloperView (require a password)
            3. Exit Program
        ''')
    userResponse = input("SELECTION: ")
    return userResponse

def showPlayerViewMenu() -> int:
    print(f'''
        1. View specifics of the database
        2. Exit to main menu
        ''')
    userResponse = input("SELECTION: ")
    return userResponse

def showDeveloperViewMenu() -> int:
    print(f'''
        1. Modify a table
        2. Delete a table
        3. Insert into a table
        4. View specifics of the databse
        5. Exit to main menu
        ''')
    userResponse = input("SELECTION: ")
    return userResponse