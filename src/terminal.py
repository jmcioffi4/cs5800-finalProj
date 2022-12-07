from dbConnector import dbConnector
from sys import exit
from pandas import DataFrame
from tabulate import tabulate

# # Need a empty function for each query
# Functional Requirements:

# Global Variables
global database 
database = dbConnector()

# The Game Player must be able to see their player’s inventory
def playerInventory(playerID):
    """The Game Player must be able to see their player’s inventory
    Arguments:
        playerID: The ID of the player"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM IsHolding 
                                    WHERE playerID = {playerID}
                                    ''')
    makeDBandPrint(results, columnsList=['playerID', 'itemID'])
        
# The Game Player must be able to see a list of villagers that live in the player’s world
def playerVillagers(worldID):
    """The Game Player must be able to see a list of villagers that live on the specified worldID
    Arguments:
        playerID: The ID of the player"""
    results = database.executeSQL(f'''
                                    SELECT v.*
                                    FROM Villager v
                                    JOIN hasVillager h ON h.NPCID = v.NPCID
                                    WHERE h.worldID = {worldID}
                                    ''')
    makeDBandPrint(results, columnsList=['NPCID', 'Name', 'Personality', 'Gender', 'Birthday', 'Species'])

# The Game Player must be able to see a list of creatures that they have caught
def playerCaughtCreatures(playerID):
    """The Game Player must be able to see a list of creatures that they have caught
    Arguments:
        playerID: The ID of the player"""
    results = database.executeSQL(f'''
                                    SELECT creature.* 
                                    FROM hasCaught, creature 
                                    WHERE hasCaught.playerId = {playerID}
                                    AND hasCaught.creatureID = creature.creatureID; 
                                    ''')
    makeDBandPrint(results, columnsList=['CreatureID', 'Name', 'isDonated', 'rarity', 'timeOfDay', 'season'])
    
# The Game Player must be able to see a list of creatures that have been donated to their world
def playerDonatedCreatures(playerID):
    """The Game Player must be able to see a list of creatures that have been donated to their world
    Arguments:
        playerID: The ID of the player"""
    results = database.executeSQL(f'''
                                SELECT creature.* 
                                FROM creature, player, hasDonated, livesOn 
                                WHERE player.playerID = {playerID}
                                AND player.playerID = livesOn.playerID 
                                AND livesOn.WorldID = hasDonated.WorldId 
                                AND creature.CreatureID = HasDonated.creatureId; 
                                    ''')
    makeDBandPrint(results, columnsList=['creatureID', 'name', 'isDonated', 'rarity', 'timeOfDay', 'season'])

# The Game Player must be able to see details of their world
def playerWorldDetails(playerID):
    """The Game Player must be able to see details of their world
    Arguments:
        playerID: The ID of the player"""
    results = database.executeSQL(f'''
                                    SELECT world.* 
                                    FROM world, livesOn 
                                    WHERE livesOn.playerId = {playerID}
                                    AND livesOn.worldId = world.worldId;
                                    ''')
    makeDBandPrint(results, columnsList=['worldID', 'name', 'color', 'rating', 'fruit', 'season', 'weather', 'timeOfDay'])

# TODO: The Game Player must be able to get a list of players that live on their world
def playerListOfPlayers(playerID):
    """The Game Player must be able to get a list of players that live on their world
    Arguemnts:
        playerID: The ID of the player"""
    pass

# The Game Developer must be able to see a list of any player’s inventory
def devPlayerInventory(playerID):
    """The Game Developer must be able to see a list of any player’s inventory
    Arguments:
        playerID: The ID of the player"""
    playerInventory(playerID)

# The Game Developer must be able to see a list of all villagers
def devVillagers():
    """The Game Developer must be able to see a list of all villagers
    Arguments:
        None"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM villager;
                                    ''')
    makeDBandPrint(results, columnsList=['NPCID', 'name','personality','gender','birthday','species'])
   
# The Game Developer must be able to see a full list of creatures
def devCreatures():
    """The Game Developer must be able to see a full list of creatures
    Arguments:
        None"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM creature;
                                    ''')
    makeDBandPrint(results, columnsList=['creatureID','name','isDonated','rarity','timeOfDay','season'])

# The Game Developer must be able to see a full list of fish
def devFish():
    """The Game Developer must be able to see a full list of fish
    Arguments:
        None"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM fish;
                                    ''')
    makeDBandPrint(results, columnsList=['creatureID','size','shadowSize','difficulty','spawnPoint'])

# The Game Developer must be able to see a full list of bugs
def devBugs():
    """The Game Developer must be able to see a full list of bugs
    Arguments:
        None"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM bug;
                                    ''')
    makeDBandPrint(results, columnsList=['creatureID','speed','spawnPoint'])

# The Game Developer must be able to see a full list of fossils
def devFossils():
    """The Game Developer must be able to see a full list of fossils
    Arguments:
        None"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM fossil;
                                    ''')
    makeDBandPrint(results, columnsList=['creatureID','isExamined'])

# The Game Developer must be able to see a full list of crustaceans
def devCrustaceans():
    """The Game Developer must be able to see a full list of crustaceans
    Arguments:
        None"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM crustacean;
                                    ''')
    makeDBandPrint(results, columnsList=['creatureID','speed'])

# The Game Developer must be able to see details of any world
def devWorldDetails(worldID):
    """The Game Developer must be able to see details of any world
    Arguments:
        worldID: The ID of the world"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM world 
                                    WHERE worldID = {worldID};
                                    ''')
    makeDBandPrint(results, columnsList=['worldID','name','color','rating','fruit','season','weather','timeOfDay'])

# The Game Developer must be able to get a full list of players
def devFullPlayerList():
    """The Game Developer must be able to get a full list of players"""
    results = database.executeSQL(f'''
                                    SELECT * 
                                    FROM player;
                                    ''')
    makeDBandPrint(results, columnsList=['playerID','name','birthday','hairColor','eyeColor','isWorldRep'])

# The Game Developer must be able to get a list of players that live on a specific world
def devWorldPlayers(worldID):
    """The Game Developer must be able to get a list of players that live on a specific world
    Arguments:
        worldID: The ID of the world"""
    results = database.executeSQL(f'''
                                SELECT playerID 
                                FROM livesOn 
                                WHERE liveson.worldID = {worldID};
                                ''')
    makeDBandPrint(results, columnsList=['playerID'])

# Print a list of all functions, and their arguments
def help():
    """Print a list of all functions, and their arguments
    Arguments:
        None"""

    print("List of functions:")
    for i in functions:
        print("\t"+i)

# Give details of a specific function
def functionHelp(function):
    """Gives details of a specific function
    Arguments:
        function: The name of the function"""
    if function in functions:
        usageMessage(functions[function].__doc__)
    else:
        usageMessage("Invalid input")

def usageMessage(message):
    """Reports a Usage Message to the user if something invalid happens
        FOR INTERNAL USE ONLY"""
    print(f'''\n----------------
           \n>> USAGE MESSGE << 
           \n{message}
           \n----------------''')

def makeDBandPrint(results, columnsList):
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



# create a dictionary of functions
functions = {
    "playerInventory": playerInventory,
    "playerVillagers": playerVillagers,
    "playerCaughtCreatures": playerCaughtCreatures,
    "playerDonatedCreatures": playerDonatedCreatures,
    "playerWorldDetails": playerWorldDetails,
    "devPlayerInventory": devPlayerInventory,
    "devVillagers": devVillagers,
    "devCreatures": devCreatures,
    "devFish": devFish,
    "devBugs": devBugs,
    "devFossils": devFossils,
    "devCrustaceans": devCrustaceans,
    "devWorldDetails": devWorldDetails,
    "devFullPlayerList" : devFullPlayerList,
    "devWorldPlayers": devWorldPlayers,
    "usageMessage" : usageMessage,
    "makeDBandPrint" : makeDBandPrint,
    "help": help,
    "functionHelp": functionHelp,
}


# Terminal must take one or two arguments, the first decides which function is called, and the second is used if the function requires an argument
def terminal():
    while True:
        # Show the user help message
        print('''\n------------------------------------------------"
            \n>> USAGE MESSAGE <<
            \n* Use keyword 'exit' or ^C to exit the program
            \n* Enter a function, or type 'help' for a list of functions
            \n* Input must be in the format '<functionName> <argument>'
            \n------------------------------------------------\n''')

        # Take input from user, split it into a list, and then assign it to a variable
        user_input = input("INPUT: ").split()
        
        # print a line for space
        print("") 
        
        # check the args
        try:
            if user_input[0] in functions:
                if (len(user_input)==1):
                    # Check if there's an argument needed
                    if functions[user_input[0]].__code__.co_argcount == 1:
                        usageMessage("!!Function requires an argument!!")
                    else:
                        functions[user_input[0]]()
                if (len(user_input) == 2):
                    # bypass isDigit check for every other function that needs it
                    if (user_input.__contains__('functionHelp')):
                        functions[user_input[0]](user_input[1])
                        continue
                    # if we aren't getting functionHelp, then the arg needs to be a int (ID)
                    try:
                        if (user_input[1].isdigit()):
                        # Call the function
                            functions[user_input[0]](user_input[1])
                        else:
                            usageMessage(f"[{user_input[1]}] is not a valid ID]")
                    except TypeError:
                        usageMessage("Invalid Input for the ID arg")
                        continue;
        
            elif user_input[0] == "exit":
                    usageMessage("!!GoodBye!!")
                    exit(0)
            
            else:
                    usageMessage("!!Invalid input!!")
        except IndexError:
                usageMessage("Invalid Input")
                continue;


if __name__ == "__main__":
    # Repeat the terminal until the user enters "exit" or uses keyboard interrupt
    try:
        terminal()
    except KeyboardInterrupt:
        usageMessage("!!GoodBye!!")

