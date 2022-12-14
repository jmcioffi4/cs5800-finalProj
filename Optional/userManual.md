# User Manual for `Optional/main.py`
## Main Menu
*   The main menu will look like this:
    *   ```
        -------------------
        MAIN MENU
            1. PlayerView
            2. DeveloperView (requires a password)
            3. Exit Program
        -------------------

        SELECTION: 
        ```
*   `SELECTION` is asking for which menu option you want. Respond with 
    *   `1` to go the Player View Menu
    *   `2` to go to the Developer View Menu
    *   `3` to exit the program


## Player View Menu
*   The player view menu will look like this:
    *   ```
        -------------------
        PLAYER VIEW MENU
            1. View specifics of the database
            2. Exit to main menu
        -------------------
        
        SELECTION: 
        ```
*   `SELECTION` is asking for which menu option you want. Respond with 
    *   `1` to go to the UI that lets you view the Database (in player view)
    *   `2` to return to the main menu

## Developer View Menu
*   The developer view menu option (the first time it is accesseed) will ask for a password, enter `password`
*   The developer view menu will look like this:
    *   ```
        -------------------
        DEVELOPER VIEW MENU
            1. Update a table
            2. Delete a row from a table
            3. Insert a new row into a table
            4. View specifics of the databse
            5. Exit to main menu
        -------------------
        
        SELECTION:
        ```
*   `SELECTION` is asking for which menu option you want. Respond with 
    *   `1` to Update a table of your choice
    *   `2` to Delete a row from a table (based on attribute)
    *   `3` to Insert a new row into a table
    *   `4` to go to the UI that lets you view the Database (in developer view)
    *   `5` to go back to the previous menu

## Player View - UI for Viewing Database
*   You will see the following usage message (it's there to help you):
    *   ```
        ------------------------------------------------"
                        
        >> USAGE MESSAGE (VIEWING DATABASE) <<
                        
        * Use keyword 'exit' to exit to the previous menu
                        
        * Enter a function, or type 'help' for a list of functions in your view
                        
        * Input must be in the format '<functionName> [<argument that is a singular INT>]'
                        
        ------------------------------------------------

        YOUR INPUT:
        ```
*   `YOUR INPUT` is asking what function (with the parameter if it needs it) you want to run
    *   Exit to the previous menu by entering `exit`
    *   Available Functions (via typing `help`):
        *   ```
            List of functions:
                playerInventory <int (playerID)>
                playerVillagers <int (playerID)>
                playerCaughtCreatures <int (playerID)>
                playerDonatedCreatures <int (playerID)>
                playerWorldDetails <int (playerID)>
                playerListOfPlayers <int (playerID)>
                help
                functionHelp <function>
            ```
    *   You will see a usage message if you did not give a proper parameter

## Developer View - UI for Viewing Database
*   You will see the following usage message (it's there to help you):
    *   ```
        ------------------------------------------------"
                        
        >> USAGE MESSAGE (VIEWING DATABASE) <<
                        
        * Use keyword 'exit' to exit to the previous menu
                        
        * Enter a function, or type 'help' for a list of functions in your view
                        
        * Input must be in the format '<functionName> [<argument that is a singular INT>]'
                        
        ------------------------------------------------

        YOUR INPUT:
        ```
*   `YOUR INPUT` is asking what function (with the parameter if it needs it) you want to run
    *   Exit to the previous menu by entering `exit`
    *   Available Functions (via typing `help`):
        *   ```
            List of functions:
                devPlayerInventory <int (playerID)>
                devVillagers 
                devCreatures
                devFish
                devBugs
                devFossils
                devCrustaceans
                devWorldDetails <int (worldID)>
                devFullPlayerList
                devWorldPlayers <int (worldID)>
                usageMessage <String> (For internal use only)
                help
                functionHelp <function>
            ```
    *   You will see a usage message if you did not give a proper parameter

## Developer View - INSERT, UPDATE, and DELETE options
*   **IMPORTANT**
    *   There are enums, see [create.sql](../SQL/create.sql) to see which enums you can use for attribute values, otherwise it will crash.
*   `INSERT`
    *   The code runs the following SQL code: `INSERT INTO {table} VALUE ({values});`
    *   If an error occurs, it will tell you via a SQL error message
    *   On screen prompts will take input for the variables it needs
    *   Enter dates like this: `'YYYY-MM-DD'`
    *   *NOTE* For sub-entity tables, you must insert on the parent before that child table
    *   Example:
        *   ```
            What table did you want to insert into? : Player
            What value (or values) did you want to insert into that table? (Ex: primaryKEY, INT, 'STRING') (NOTE: must be separated by commas, strings in single quotes) : 44, 'jackjack', '1969-04-20', 'pink', 'hazel', 1
            ```
*   `UPDATE`
    *   The code runs the following SQL code: `UPDATE {table} SET {attribute_name} = {new_value} WHERE {attribute_name} = {old_value};`
        *   there is another version for any strings passed, don't worry it works.
    *   On screen prompts will take input for the variables it needs
    *   Example:
        *   ```
            Which table would you like to update? : Tool
            Which attribute did you want to update? : type
            What do you want to change the attribtue_value to? : pole
            What was the old or current value of attribute_value? : shovel
            ```
*   `DELETE`
    *   The code runs the following SQL code: `DELETE FROM {table} WHERE {attribute_name} = {value};`
        *   there is another version for any strings passed, don't worry it works.
    *   On screen prompts will take input for the variables it needs
    *   Example:
        *   ```
            From which table did you want to delete? : Tool
            Select table attribute value to search by: color
            Delete all entries with what attribute value (specifically)? : green
            ```