#!/usr/bin/env python3
"""
    script that provides some stats
    about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats():
    """Stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    print("IPs:")
    top = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top:
        print("\t{}: {}".format(ip['_id'], ip['count']))
    
    
if __name__ == "__main__":
    log_stats()
