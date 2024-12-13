#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """To finds and return the list of schools having a specific topic.

    Args:
        mongo_collection: the pymongo collection object.
        topic (str): the specific topic.

    Returns:
        List[dict]: List of schools having the specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
