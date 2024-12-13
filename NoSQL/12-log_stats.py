#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in MongoDB.
"""

def schools_by_topic(mongo_collection, topic):
    """Finds and returns the list of schools with a specific topic.

    Args:
        mongo_collection: the pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List[dict]: A list of documents (schools) that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))