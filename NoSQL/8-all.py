#!/usr/bin/env python3
"""Module for listing all documents in a MongoDB collection"""


def list_all(mongo_collection):
    """
    List all documents in the provided collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents, or empty list if none exist
    """
    return list(mongo_collection.find())
