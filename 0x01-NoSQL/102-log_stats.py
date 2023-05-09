#!/usr/bin/env python3
'''
Python script that provides some stats about Nginx logs stored in MongoDB
and sorts and lists top 10 IPs 
'''
from pymongo import MongoClient

if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        logs = db.nginx.count_documents({})
        print(str(logs) + ' logs')
        print('Methods:')
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count_method = db.nginx.count_documents({"method": method})
            print('\tmethod ' + method + ': ' + str(count_method))

        st_chk = db.nginx.count_documents({"method": "GET", "path": "/status"})
        print(str(st_chk) + ' status check')

        result = db.nginx.aggregate([
            {"$group": {"_id": "$ip", "total_count": {"$sum": 1}}},
            {"$sort": {"total_count": -1}},
            {"$limit": 10},
        ])

        print('IPs:')
        for ip in result:
            print(str(ip["_id"]) + ": " + str(ip["total_count"]))
