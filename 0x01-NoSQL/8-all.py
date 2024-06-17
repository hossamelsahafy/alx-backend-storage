#!/usr/bin/env python3
"""
    function that lists all documents in a collection
"""

from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    doc = list(mongo_collection.find())
    return doc
