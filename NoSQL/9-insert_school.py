#!/usr/bin/env python3
"""
a Python function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a MongoDB collection.

    Args:
        mongo_collection: the pymongo collection object.
        **kwargs: Key-value pairs in the document.

    Returns:
        The _id of the document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
