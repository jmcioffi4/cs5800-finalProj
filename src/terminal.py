# # Need a empty function for each query
# Functional Requirements:

# The Game Player must be able to see their player’s inventory
def playerInventory(playerID):
    pass

# The Game Player must be able to see a list of villagers that live in the player’s world
def playerVillagers(playerID):
    pass

# The Game Player must be able to see a list of creatures that they have caught
def playerCaughtCreatures(playerID):
    pass

# The Game Player must be able to see a list of creatures that have been donated to their world
def playerDonatedCreatures(playerID):
    pass    

# The Game Player must be able to see details of their world
def playerWorldDetails(playerID):
    pass

# The Game Developer must be able to see a list of any player’s inventory
def devPlayerInventory(playerID):
    playerInventory(playerID)

# The Game Developer must be able to see a list of all villagers
def devVillagers():
    pass    

# The Game Developer must be able to see a full list of creatures
def devCreatures():
    pass

# The Game Developer must be able to see a full list of fish
def devFish():
    pass

# The Game Developer must be able to see a full list of bugs
def devBugs():
    pass

# The Game Developer must be able to see a full list of fossils
def devFossils():
    pass

# The Game Developer must be able to see a full list of crustaceans
def devCrustaceans():
    pass

# The Game Developer must be able to see details of any world
def devWorldDetails(worldID):
    pass

# The Game Developer must be able to get a list of players that live on a specific world
def devWorldPlayers(worldID):
    pass


# Terminal must take one or two arguments, the first decides which function is called, and the second is used if the function requires an argument
def terminal():
    # Take input from user, split it into a list, and then assign it to a variable
    user_input = input("Enter function name, and if neccesary, argument: ").split()
    # Check if the user input is valid
    if len(user_input) == 1:
        # Check if the function exists
        if user_input[0] in globals():
            # Call the function
            globals()[user_input[0]]()
        else:
            print("Function does not exist")
    elif len(user_input) == 2:
        # Check if the function exists
        if user_input[0] in globals():
            # Call the function
            globals()[user_input[0]](user_input[1])
        else:
            print("Function does not exist")
    else:
        print("Invalid input")

if __name__ == "__main__":
    terminal()
