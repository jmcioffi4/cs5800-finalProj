from viewSQLDB import viewDB, usageMessage
import menu

def showDevView():
    developerMenuInput = menu.showDeveloperViewMenu()
    if developerMenuInput == 1:
        # call to modify a table
        pass
    elif developerMenuInput == 2:
        # call to delete a table
        pass
    elif developerMenuInput == 3:
        # call to insert into a table
        pass
    elif developerMenuInput == 4:
        # call viewSQLDB.py with viewMode = "developerView"
        viewDB("developerView")
        return # if user backs to main menu, restart with main menu
    elif developerMenuInput == 5:
        # go back a menu, show the main
        pass

if __name__ == "__main__":    
    while (True):
        try:
            # show the user the menu
            mainMenuInput = menu.menu()
            
            # Player View Selected
            if mainMenuInput == '1':
                playerMenuInput = menu.showPlayerViewMenu()
                if playerMenuInput == 1:
                    # call viewSQLDB.py with viewMode = "playerView"
                    viewDB("playerView")
                    continue # if user backs to main menu, restart with main menu
                elif playerMenuInput == 2:
                    usageMessage(" Returning to main menu ")
                else:
                    usageMessage("Invalid Menu Option, please try again")
                    continue
           
            # Developer Mode Selected
            elif mainMenuInput == '2':
                # ask for a passcode to seem legit
                while (True):
                    devPassword = input("Please Enter Password: ")
                    if devPassword == 'password':
                        showDevView()
                        break
                    elif devPassword == 'X':
                        break
                    else:
                        usageMessage("Oops thats not a valid password. Try again \nOR type 'X' to go back to the main menu")

            # Exit Program Selected
            elif mainMenuInput == '3':
                # User wants to exit program
                usageMessage("!! Goodbye !!")
                exit(0)
            
            else:
                usageMessage("Invalid Menu Option, please try again")
                continue

        except KeyboardInterrupt:
            usageMessage("!!GoodBye!!")
            exit(0)