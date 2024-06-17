#!/usr/bin/env python3
"""
    function that inserts a new document in a
    collection based on kwargs
"""
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)

def insert_school(mongo_collection, **kwargs):
    """Insert New Document """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
