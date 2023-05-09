#!/usr/bin/env python3
'''
Python script that provides some stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient


with MongoClient() as client:
    db = client.logs
    logs = db.nginx.count_documents({})
    print(str(logs) + ' logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_method = db.nginx.count_documents({"method": method})
        print('\tmethod ' + method + ': ' + str(count_method))

    stat_chk = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(str(stat_chk) + ' status check')
