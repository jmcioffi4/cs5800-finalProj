from sys import exit
from pandas import DataFrame
from tabulate import tabulate

class viewSQLDB():
    def __init__(self, database) -> None:
        self.database = database
        # Dictionary of all functions based on viewMode
        self.playerViewFunctions = {
            "playerInventory": self.playerInventory,
            "playerVillagers": self.playerVillagers,
            "playerCaughtCreatures": self.playerCaughtCreatures,
            "playerDonatedCreatures": self.playerDonatedCreatures,
            "playerWorldDetails": self.playerWorldDetails,
            "playerListOfPlayers" : self.playerListOfPlayers,
            "help": self.help,
            "functionHelp": self.functionHelp,
        }
        self.developerViewFunctions = {
            "devPlayerInventory": self.devPlayerInventory,
            "devVillagers": self.devVillagers,
            "devCreatures": self.devCreatures,
            "devFish": self.devFish,
            "devBugs": self.devBugs,
            "devFossils": self.devFossils,
            "devCrustaceans": self.devCrustaceans,
            "devWorldDetails": self.devWorldDetails,
            "devFullPlayerList" : self.devFullPlayerList,
            "devWorldPlayers": self.devWorldPlayers,
            "usageMessage" : self.usageMessage,
            "help": self.help,
            "functionHelp": self.functionHelp,
        }
        self.mainDict = self.playerViewFunctions

    # The Game Player must be able to see their player’s inventory
    def playerInventory(self, playerID):
        """The Game Player must be able to see their player’s inventory
        Arguments:
            playerID: The ID of the player"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM IsHolding 
                                        WHERE playerID = {playerID}
                                        ''')
        self.makeDBandPrint(results, columnsList=['playerID', 'itemID'])
            
    # The Game Player must be able to see a list of villagers that live in the player’s world
    def playerVillagers(self, worldID):
        """The Game Player must be able to see a list of villagers that live on the specified worldID
        Arguments:
            playerID: The ID of the player"""
        results = self.database.executeSQL(f'''
                                        SELECT v.*
                                        FROM Villager v
                                        JOIN HasVillager h ON h.NPCID = v.NPCID
                                        WHERE h.worldID = {worldID}
                                        ''')
        self.makeDBandPrint(results, columnsList=['NPCID', 'Name', 'Personality', 'Gender', 'Birthday', 'Species'])

    # The Game Player must be able to see a list of creatures that they have caught
    def playerCaughtCreatures(self, playerID):
        """The Game Player must be able to see a list of creatures that they have caught
        Arguments:
            playerID: The ID of the player"""
        results = self.database.executeSQL(f'''
                                        SELECT Creature.*
                                        FROM HasCaught, Creature
                                        WHERE HasCaught.playerId = {playerID}
                                        AND HasCaught.creatureID = Creature.creatureID; 
                                        ''')
        self.makeDBandPrint(results, columnsList=['CreatureID', 'Name', 'isDonated', 'rarity', 'timeOfDay', 'season'])
        
    # The Game Player must be able to see a list of creatures that have been donated to their world
    def playerDonatedCreatures(self, playerID):
        """The Game Player must be able to see a list of creatures that have been donated to their world
        Arguments:
            playerID: The ID of the player"""
        results = self.database.executeSQL(f'''
                                    SELECT Creature.*
                                    FROM Creature, Player, HasDonated, LivesOn
                                    WHERE Player.playerID = {playerID}
                                    AND Player.playerID = LivesOn.playerID
                                    AND LivesOn.WorldID = HasDonated.WorldId
                                    AND Creature.CreatureID = HasDonated.creatureId; 
                                        ''')
        self.makeDBandPrint(results, columnsList=['creatureID', 'name', 'isDonated', 'rarity', 'timeOfDay', 'season'])

    # The Game Player must be able to see details of their world
    def playerWorldDetails(self, playerID):
        """The Game Player must be able to see details of their world
        Arguments:
            playerID: The ID of the player"""
        results = self.database.executeSQL(f'''
                                        SELECT World.*
                                        FROM World, LivesOn
                                        WHERE LivesOn.playerID = {playerID}
                                        AND LivesOn.worldId = World.worldID;
                                        ''')
        self.makeDBandPrint(results, columnsList=['worldID', 'name', 'color', 'rating', 'fruit', 'season', 'weather', 'timeOfDay'])

    # The Game Player must be able to get a list of players that live on their world
    def playerListOfPlayers(self, playerID):
        """The Game Player must be able to get a list of players that live on their world
        Arguemnts:
            playerID: The ID of the player"""
        results = self.database.executeSQL(f'''
                                        SELECT playerID
                                        FROM LivesOn
                                        WHERE LivesOn.worldID = (SELECT worldID 
                                                                FROM LivesOn 
                                                                WHERE playerID = {playerID});
                                        ''')
        self.makeDBandPrint(results, columnsList=['playerID'])

    # The Game Developer must be able to see a list of any player’s inventory
    def devPlayerInventory(self, playerID):
        """The Game Developer must be able to see a list of any player’s inventory
        Arguments:
            playerID: The ID of the player"""
        self.playerInventory(playerID)

    # The Game Developer must be able to see a list of all villagers
    def devVillagers(self):
        """The Game Developer must be able to see a list of all villagers
        Arguments:
            None"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Villager;
                                        ''')
        self.makeDBandPrint(results, columnsList=['NPCID', 'name','personality','gender','birthday','species'])
    
    # The Game Developer must be able to see a full list of creatures
    def devCreatures(self):
        """The Game Developer must be able to see a full list of creatures
        Arguments:
            None"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Creature;
                                        ''')
        self.makeDBandPrint(results, columnsList=['creatureID','name','isDonated','rarity','timeOfDay','season'])

    # The Game Developer must be able to see a full list of fish
    def devFish(self):
        """The Game Developer must be able to see a full list of fish
        Arguments:
            None"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Fish;
                                        ''')
        self.makeDBandPrint(results, columnsList=['creatureID','size','shadowSize','difficulty','spawnPoint'])

    # The Game Developer must be able to see a full list of bugs
    def devBugs(self):
        """The Game Developer must be able to see a full list of bugs
        Arguments:
            None"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Bug;
                                        ''')
        self.makeDBandPrint(results, columnsList=['creatureID','speed','spawnPoint'])

    # The Game Developer must be able to see a full list of fossils
    def devFossils(self):
        """The Game Developer must be able to see a full list of fossils
        Arguments:
            None"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Fossil;
                                        ''')
        self.makeDBandPrint(results, columnsList=['creatureID','isExamined'])

    # The Game Developer must be able to see a full list of crustaceans
    def devCrustaceans(self):
        """The Game Developer must be able to see a full list of crustaceans
        Arguments:
            None"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Crustacean;
                                        ''')
        self.makeDBandPrint(results, columnsList=['creatureID','speed'])

    # The Game Developer must be able to see details of any world
    def devWorldDetails(self, worldID):
        """The Game Developer must be able to see details of any world
        Arguments:
            worldID: The ID of the world"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM World 
                                        WHERE worldID = {worldID};
                                        ''')
        self.makeDBandPrint(results, columnsList=['worldID','name','color','rating','fruit','season','weather','timeOfDay'])

    # The Game Developer must be able to get a full list of players
    def devFullPlayerList(self):
        """The Game Developer must be able to get a full list of players"""
        results = self.database.executeSQL(f'''
                                        SELECT * 
                                        FROM Player;
                                        ''')
        self.makeDBandPrint(results, columnsList=['playerID','name','birthday','hairColor','eyeColor','isWorldRep'])

    # The Game Developer must be able to get a list of players that live on a specific world
    def devWorldPlayers(self, worldID):
        """The Game Developer must be able to get a list of players that live on a specific world
        Arguments:
            worldID: The ID of the world"""
        results = self.database.executeSQL(f'''
                                    SELECT playerID 
                                    FROM livesOn 
                                    WHERE liveson.worldID = {worldID};
                                    ''')
        self.makeDBandPrint(results, columnsList=['playerID'])

    # Print a list of all functions, and their arguments
    def help(self):
        """Print a list of all functions, and their arguments
        Arguments:
            None"""

        print("List of functions:")
        for i in self.mainDict:
            print("\t"+i)

    # Give details of a specific function
    def functionHelp(self, function):
        """Gives details of a specific function
        Arguments:
            function: The name of the function"""
        if function in self.mainDict:
            self.usageMessage(self.mainDict[function].__doc__)
        else:
            self.usageMessage("Invalid input")

    def usageMessage(self, message):
        """Reports a Usage Message to the user if something invalid happens
            FOR INTERNAL USE ONLY"""
        print(f'''\u001b[1;32;40m
            \n----------------
            \n>> USAGE MESSAGE << 
            \n{message}
            \n----------------''')

    def makeDBandPrint(self, results, columnsList):
        """Internal Function that is called by all functions to 
        create a pretty sql looking table and output the data to the user
    
        Arguments:
            results: the results from the .executeSQL() function call
            columnsList: the column names in a list of strings; is important to be 
                right otherwise program will crash (make sure that you have the right
                number of columns and the right column names from the SQL data returned)
                
        FOR INTERNAL USE ONLY"""
        df = DataFrame(results, columns=columnsList)
        print(tabulate(df, headers='keys', tablefmt='psql'))

    # viewDB must take one or two arguments, the first decides which function is called, and the second is used if the function requires an argument
    def viewDB(self, viewMode):
        if viewMode == "playerView":
            self.mainDict = self.playerViewFunctions
        if viewMode == "developerView":
            self.mainDict = self.developerViewFunctions

        while True:
            # Show the user help message
            print('''\u001b[1;32;40m
                \n------------------------------------------------"
                \n>> USAGE MESSAGE (VIEWING DATABASE) <<
                \n* Use keyword 'exit' to exit to the previous menu
                \n* Enter a function, or type 'help' for a list of functions in your view
                \n* Input must be in the format '<functionName> [<argument that is a singular INT>]'
                \n------------------------------------------------\n''')

            # Take input from user, split it into a list, and then assign it to a variable
            user_input = input("\u001b[13;31;40m YOUR INPUT: ").split()
            if len(user_input) > 2:
                self.usageMessage("!! Too Many Parameters Buddy !! ")
            
            # print a line for space
            print("") 
            
            # check the args
            try:
                if user_input[0] in self.mainDict:
                    if (len(user_input)==1):
                        # Check if there's an argument needed
                        if self.mainDict[user_input[0]].__code__.co_argcount == 2:
                            self.usageMessage("!!Function requires an argument!!")
                        elif self.mainDict[user_input[0]].__code__.co_argcount == 0:
                            self.usageMessage("!! No Args for this Function !!")
                        else:
                           self.mainDict[user_input[0]]()
                    if (len(user_input) == 2):
                        if (user_input.__contains__('functionHelp')):
                            self.mainDict[user_input[0]](user_input[1])
                            continue
                        # if we aren't getting functionHelp, then the arg needs to be a int (ID)
                        try:
                            if (user_input[1].isdigit()):
                            # Call the function
                                self.mainDict[user_input[0]](user_input[1])
                            else:
                                self.usageMessage(f"[{user_input[1]}] is not a valid ID")
                        except TypeError:
                            self.usageMessage("Invalid Input for the ID arg (try without an ID argument)")
                            continue
            
                elif (user_input[0].lower() == "exit"):
                        self.usageMessage("Returning to Main Menu")
                        break
                else:
                        self.usageMessage("!!Invalid input!!")
            except IndexError:
                    self.usageMessage("Invalid Input")
                    continue