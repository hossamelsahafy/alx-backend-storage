#!/usr/bin/env python3
""" function that returns the list of
    school having a specific topic"""

from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)


def schools_by_topic(mongo_collection, topic):
    """
        function that returns the list of
        school having a specific topic
    """
    doc = mongo_collection.find({"topics": topic})
    return list(doc)
