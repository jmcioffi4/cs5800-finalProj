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

    # FOR MODIFYING THE DATABASE
    def INSERT_SQL(self, table, values):
        """INSERT INTO {table} {values};"""
        try:
            sql = f"INSERT INTO {table} {values};"
            self.mycursor.execute(sql)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def DELETE_SQL(self, table, attribute_name, value):
        """DELETE FROM {table} WHERE {attribute_name} = {value};"""
        try:
            if value.isnumeric():
                sql = f"DELETE FROM {table} WHERE {attribute_name} = {value};"
            else:
                sql = f"DELETE FROM {table} WHERE {attribute_name} = '{value}';"
            self.mycursor.execute(sql)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def UPDATE_SQL(self, table, attribute_name, new_value, old_value):
        """UPDATE {table} SET {attribute_name} = {new_value} WHERE {attribute_name} = {old_value};"""
        try:
            if new_value.isnumeric() and old_value.isnumeric():
                sql = f"UPDATE {table} SET {attribute_name} = {new_value} WHERE {attribute_name} = {old_value};"
            else:
                sql = f"UPDATE {table} SET {attribute_name} = '{new_value}' WHERE {attribute_name} = '{old_value}';"
            self.mycursor.execute(sql)
            self.mydb.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))