#!/usr/bin/env python3
"""Module for updating school topics in MongoDB"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of all school documents matching name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to match
        topics (list): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
