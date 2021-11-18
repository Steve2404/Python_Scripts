import sqlite3

#Verbingung, Cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Sortierung absteigend
sql = "SELECT * FROM personen ORDER BY gehalt DESC"
cursor.execute(sql)
for dsatz in cursor:
    print(f"{dsatz[0]} - {dsatz[1]} - {dsatz[3]}")

print()

# Sortierung nach mehreren Felden
sql = "SELECT * FROM personen ORDER BY name, vorname"
cursor.execute(sql)
for dsatz in cursor:
    print(f"{dsatz[0]} - {dsatz[1]}")

# Verbindung beenden
connection.close()
