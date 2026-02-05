#!/usr/bin/env python3
"""Module for retrieving schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Return list of schools that match a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search

    Returns:
        List of matching documents
    """
    return list(mongo_collection.find({"topics": topic}))
