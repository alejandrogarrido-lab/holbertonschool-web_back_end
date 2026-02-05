#!/usr/bin/env python3
"""Module for inserting a document into a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection using kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: fields to insert into the document

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
