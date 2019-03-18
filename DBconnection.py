
from sqlite3 import connect

class DBconnection:

    __instance = None

    @staticmethod
    def getInstance():

        if DBconnection.__instance == None:
            DBconnection()
        return DBconnection.__instance

    def __init__(self):

        if DBconnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DBconnection.__instance = self
            self.connection = connect("bill-CRUD.db")

