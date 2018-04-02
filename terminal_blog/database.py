import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"   # all objects are goinf to use the same uri and database, so no __init__ func
    #  here.
    DATABASE = None

    @staticmethod
    def initialize():    # made static bcz we are not using self here
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
