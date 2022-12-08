def menu():
    return showMainMenu()

def showMainMenu() -> int:
    print(f'''\u001b[1;32;40m
        MAIN MENU
            1. PlayerView
            2. DeveloperView (require a password)
            3. (or 'X') Exit Program
        ''')
    userResponse = input("SELECTION: ")
    return userResponse

def showPlayerViewMenu() -> int:
    print(f'''\u001b[1;32;40m
        1. View specifics of the database
        2. (or 'X') Exit to main menu
        ''')
    userResponse = input("SELECTION: ")
    return userResponse

def showDeveloperViewMenu() -> int:
    print(f'''\u001b[1;32;40m
        1. Update a table
        2. Delete a table
        3. Insert into a table
        4. View specifics of the databse
        5. (or 'X') Exit to main menu
        ''')
    userResponse = input("SELECTION: ")
    return userResponse