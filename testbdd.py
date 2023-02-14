import mysql.connector

mydb = mysql.connector.connect(
    host="eliascastel.ddns.net",
    port="3306",
    user="root",
    password="@RootRoot1212",
    database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM perso")
