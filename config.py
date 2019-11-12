from pymongo import MongoClient

DATABASE = MongoClient()['students'] #DB NAME but is not work i dont know why :v
DEBUG = True
client = MongoClient('localhost', 27017)
