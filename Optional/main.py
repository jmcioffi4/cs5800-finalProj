from viewSQLDB import viewDB, usageMessage
from menu import menu

if __name__ == "__main__":    
    # TODO: Implement the menu
    
    # TODO : Update this so it only runs when the menu option is selected
    try:
        # show the user the 
        # TODO: Add more options (with 'exit') so user can go back to main menu in viewDB()
        viewMode = "developerView" # TEMP - need to get this from the menu option
        viewDB(viewMode)
    except KeyboardInterrupt:
        usageMessage("!!GoodBye!!")