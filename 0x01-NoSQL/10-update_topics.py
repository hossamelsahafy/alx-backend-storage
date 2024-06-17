#!/usr/bin/env python3
"""
    changes all topics of a school document based on the name
"""
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)


def update_topics(mongo_collection, name, topics):
    """
        changes all topics of a school document based on the name
    """

    doc = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
