import mysql.connector

mydb = mysql.connector.connect(
    host="eliascastel.ddns.net",
    user="pi",
    password="@root123"
)

print(mydb)
