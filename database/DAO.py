from database.DB_connect import DBConnect
from model.aereoporti import Aereoporti
from model.voli import Voli


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAereoporti():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM airports"""
        cursor.execute(query)

        for row in cursor:
            result.append(Aereoporti(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVoli(aeroporto):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)

        query = """SELECT *
                   FROM flights
                   WHERE ORIGIN_AIRPORT_ID = %s OR DESTINATION_AIRPORT_ID = %s"""

        cursor.execute(query, (aeroporto.ID, aeroporto.ID))

        for row in cursor:
            result.append(Voli(**row))

        cursor.close()
        conn.close()
        return result