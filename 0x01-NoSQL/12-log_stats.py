#!/usr/bin/env python3
"""
    script that provides some stats
    about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    """States"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.log
    collection = db.nginx

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    specific_count = collection.count_documents({"method": "GET",
                                                 "path": "/status"})
    print("{} status check".format(specific_count))
