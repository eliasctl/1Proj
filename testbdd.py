import mysql.connector

mydb = mysql.connector.connect(
    host="eliascastel.ddns.net",
    port="3306",
    user="pi",
    password="@root123",
    database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM perso")
