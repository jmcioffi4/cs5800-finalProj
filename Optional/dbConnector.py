import mysql.connector

class dbConnector():
    def __init__(self):

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            # password="",
            database="theDBGame"
        )
        self.mycursor = self.mydb.cursor()

    def executeSQL(self, SQL):
        try:
            self.mycursor.execute(SQL)
            result = self.mycursor.fetchall()
            return result

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))