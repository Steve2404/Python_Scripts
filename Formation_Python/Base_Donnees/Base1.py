import sqlite3

conn = sqlite3.connect("database.db") # connection a une base de donnee

c = conn.cursor() # creation d un curseur
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
    salaire int
)

""") # permet d executer les commandes sql
d = {"salaire": 1000,"prenom": "Paul", "nom": "Dupond"}
#c.execute("INSERT INTO employees VALUES(:salaire,:prenom, :nom)", d)
#c.execute("SELECT * FROM employees WHERE prenom=:prenom", d)
#donnee = c.fetchall() # recupere toutes les infos contenues dans la command. sql
c.execute(""" UPDATE employees SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom""", d)
#c.execute("DELETE FROM employees WHERE prenom=:prenom",d) # supprime les element dans la table

conn.commit() #on envois le tout dans la base de donee
conn.close() #fermeture de la connection