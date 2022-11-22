from dbConnector import dbConnector

def displayTables():
    return "SHOW TABLES;"

def menu():
    print(f"""
===================================
(1) Display Tables
(2) option 2
(3) option 3 
(4) Option 4
===================================
            """)

    selection = int(input("Select Menu Option: "))
    if selection == 1:
        return "SHOW TABLES;"
    menu()

def viewFriends(data, database):
    friendList = {}

    for i in data:
        playerId = data[0][0]
        NPCID = data[0][1]



if __name__ == "__main__":
    Database = dbConnector()

    # data = Database.executeSQL("SELECT * FROM Player")


#player ID NPC ID

    while True:
        print(f"""
        ===================================
        (1) Display Tables
        (2) option 2
        (3) option 3 
        (4) Option 4
        ===================================
                    """)

        selection = int(input("Select Menu Option: "))
        if selection == 1:
            data = Database.executeSQL("SELECT * FROM IsFriendsWith")
            print(data[3][1])

