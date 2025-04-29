from database.DB_connect import DBConnect
from model.aereoporti import Aereoporti
from model.voli import Voli


class DAO():
    def __init__(self):
        pass
    def getAereoporti(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM aereoporti"""
        cursor.execute(query)

        for row in cursor:
            result.append(Aereoporti(**row))

        cursor.close()
        conn.close()
        return result

    def getVoli(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM flights"""
        cursor.execute(query)

        for row in cursor:
            result.append(Voli(**row))

        cursor.close()
        conn.close()
        return result