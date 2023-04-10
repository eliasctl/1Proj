import mysql.connector

mydb = mysql.connector.connect(
   host="eliascastel.ddns.net",
   user="pi",
   password="@root123",
   database="test"
)

#requete = "select * from perso"
#
#with mysql.connector.connect(**mydb) as db :
#   with db.cursor() as c:
#       c.execute(requete)
#       resultats = c.fetchall()
#       for utilisateur in resultats:
#           print(utilisateur)
            