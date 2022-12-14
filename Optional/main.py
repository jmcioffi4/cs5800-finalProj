from viewSQLDB import viewSQLDB
import menu
from dbConnector import dbConnector

def showDevView(database, viewDB):
    while(True):
        developerMenuInput = menu.showDeveloperViewMenu()
        if developerMenuInput == '1':
            # call to update a table
            tableToUpdate = input("\u001b[13;31;40mWhich table would you like to update? : ")
            if tableToUpdate == "" or tableToUpdate == " ":
                continue
            attribute_name = input("\u001b[13;31;40mWhich attribute did you want to update? : ")
            if attribute_name == "" or attribute_name == " ":
                continue
            new_value = input("\u001b[13;31;40mWhat do you want to change the attribtue_value to? : ")
            if new_value == "" or new_value == " ":
                continue
            old_value = input("\u001b[13;31;40mWhat was the old or current value of attribute_value? : ")
            if old_value == "" or old_value == " ":
                continue
            database.UPDATE_SQL(tableToUpdate, attribute_name, new_value, old_value)
        elif developerMenuInput == '2':
            # call to delete a row from a table
            tableToDelete = input("\u001b[13;31;40mFrom which table did you want to delete? : ")
            if tableToUpdate == "" or tableToUpdate == " ":
                continue
            attribute_name = input("\u001b[13;31;40mSelect table attribute value to search by: ")
            if attribute_name == "" or attribute_name == " ":
                continue
            value = input("\u001b[13;31;40mDelete all entries with what attribute value (specifically)? : ")
            if value == "" or value == " ":
                continue
            database.DELETE_SQL(tableToDelete, attribute_name, value)

        elif developerMenuInput == '3':
            # call to insert into a table
            table = input("\u001b[13;31;40mWhat table did you want to insert into? : ")
            if table == "" or table == " ":
                continue
            value = input("\u001b[13;31;40mwhat value (or values) did you want to insert into that table? (Ex: primaryKEY, INT, 'STRING') (NOTE: must be separated by commas, strings in single quotes) : ")
            if value == "" or value == " ":
                continue
            database.INSERT_SQL(table, value)

        elif developerMenuInput == '4':
            # call viewSQLDB.py with viewMode = "developerView"
            viewDB.viewDB("developerView")
        elif developerMenuInput == '5':
            # go back a menu, show the main
            return

if __name__ == "__main__":
    # Create Objects
    database = dbConnector()
    viewDB = viewSQLDB(database)

    # run the program
    passwordEntered = False
    while (True):
        try:
            # show the user the menu
            mainMenuInput = menu.menu()
            
            # Player View Selected
            if mainMenuInput == '1':
                while (True):
                    playerMenuInput = menu.showPlayerViewMenu()
                    if playerMenuInput == '1':
                        # call viewSQLDB.py with viewMode = "playerView"
                        viewDB.viewDB("playerView") 
                    elif playerMenuInput == '2':
                        viewDB.usageMessage(" Returning to main menu ")
                        break
                    else:
                        viewDB.usageMessage("Invalid Menu Option, please try again")
           
            # Developer Mode Selected
            elif mainMenuInput == '2':
                # ask for a passcode to seem legit
                while (True):
                    if passwordEntered == False:
                        devPassword = input("Please Enter Password: ")
                        if devPassword == 'password':
                            passwordEntered = True
                            break
                        elif devPassword == 'X':
                            break
                        else:
                            viewDB.usageMessage("Oops thats not a valid password. Try again \nOR type [capital] 'X' to go back to the main menu")
                    else:
                        break
                if (passwordEntered):
                    showDevView(database, viewDB)

            # Exit Program Selected
            elif mainMenuInput == '3':
                # User wants to exit program
                viewDB.usageMessage("!! Goodbye !!")
                exit(0)
            
            else:
                viewDB.usageMessage("Invalid Menu Option, please try again")
                continue

        except KeyboardInterrupt:
            viewDB.usageMessage("!!GoodBye!!")
            exit(0)