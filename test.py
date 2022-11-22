import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="INSERT PASSWORD HERE",
  database = "theDBGame"
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM Player')

result = mycursor.fetchall()

for x in result:
  print(x)

print(mydb)