class dbClass():

    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "wouter", "passwd": "root", "db": "SmartHome"}
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def insert_comment(self, name, email, comment):
        q = "INSERT INTO tblContact(Naam,Emailadres,Bericht, Tijdstip)" \
            "VALUES('" + name + "','" + email + "','" + comment + "', now())"
        print(q)
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def signup(self, Naam, Passwoord):
        q = "INSERT INTO Gebruikers(Naam,Passwoord)"
        self.__cursor.execute(q)
        self.__connection.commit()
        self.__connection.close()

    def checkGebruiker(self, Naam, Passwoord):
        q = "SELECT count(*) FROM Gebruikers WHERE Naam = '" + Naam + "' and passwoord = '" + Passwoord + "';"
        self.__cursor.execute(q)
        result = self.__cursor.fetchone()
        self.__connection.close()
        return result

    def getDataTemp(self):
        q = "SELECT concat(Datum, ' ', Uur), Meting FROM Temperatuur ORDER BY Datum and Uur DESC LIMIT 3;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        print(result)
        return result

    def getDataLicht(self):
        q = "SELECT concat(datum, ' ', Uur), Meting FROM Licht ORDER BY Datum and Uur DESC LIMIT 3;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        print(result)
        return result

    def getDataDeur(self):
        q = "SELECT concat(datum, ' ', Uur), Meting, SensorSerieNr FROM BewegingsSensor ORDER BY Datum and Uur DESC LIMIT 3;"
        self.__cursor.execute(q)
        result = self.__cursor.fetchall()
        self.__connection.close()
        print(result)
        return result
