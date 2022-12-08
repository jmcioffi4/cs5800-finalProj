from viewSQLDB import viewSQLDB
import menu
from dbConnector import dbConnector

def showDevView(database, viewDB):
    developerMenuInput = menu.showDeveloperViewMenu()
    if developerMenuInput == '1':
        # call to update a table
        tableToUpdate = input("Which table would you like to update? : ")
        attribute_name = input("Which attribute did you want to update? : ")
        new_value = input("What do you want to change the attribtue_value to? : ")
        old_value = input("What was the old or current value of attribute_value? : ")
        database.UPDATE_SQL(tableToUpdate, attribute_name, new_value, old_value)
    elif developerMenuInput == '2':
        # call to delete a table
        tableToDelete = input("Which table did you want to delete? : ")
        attribute_name = input("which attribute did you want to delete? : ")
        value = input("What is the value of the attribute to delete? : ")
        database.DELETE_SQL(tableToDelete, attribute_name, value)

    elif developerMenuInput == '3':
        # call to insert into a table
        table = input("What table did you want to insert into? : ")
        value = input("what value (or values) did you want to insert into that table? : ")
        database.INSERT_SQL(table, value)

    elif developerMenuInput == '4':
        # call viewSQLDB.py with viewMode = "developerView"
        viewDB.viewDB("developerView")
        return # if user backs to main menu, restart with main menu
    elif developerMenuInput == '5' or developerMenuInput == 'X':
        # go back a menu, show the main
        return

if __name__ == "__main__":
    # Create Database Connector Object
    database = dbConnector()
    viewDB = viewSQLDB(database)

    while (True):
        try:
            # show the user the menu
            mainMenuInput = menu.menu()
            
            # Player View Selected
            if mainMenuInput == '1':
                playerMenuInput = menu.showPlayerViewMenu()
                if playerMenuInput == '1':
                    # call viewSQLDB.py with viewMode = "playerView"
                    viewDB.viewDB("playerView")
                    continue # if user backs to main menu, restart with main menu
                elif playerMenuInput == '2' or playerMenuInput == 'X':
                    viewDB.usageMessage(" Returning to main menu ")
                else:
                    viewDB.usageMessage("Invalid Menu Option, please try again")
                    continue
           
            # Developer Mode Selected
            elif mainMenuInput == '2':
                # ask for a passcode to seem legit
                while (True):
                    devPassword = input("Please Enter Password: ")
                    if devPassword == 'password':
                        showDevView(database, viewDB)
                        break
                    elif devPassword == 'X':
                        break
                    else:
                        viewDB.usageMessage("Oops thats not a valid password. Try again \nOR type 'X' to go back to the main menu")

            # Exit Program Selected
            elif mainMenuInput == '3' or mainMenuInput == 'X':
                # User wants to exit program
                viewDB.usageMessage("!! Goodbye !!")
                exit(0)
            
            else:
                viewDB.usageMessage("Invalid Menu Option, please try again")
                continue

        except KeyboardInterrupt:
            viewDB.usageMessage("!!GoodBye!!")
            exit(0)