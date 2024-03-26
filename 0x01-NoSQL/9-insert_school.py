#!/usr/bin/env python3
"""
One useful feature of this module is the ability to insert documents.
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    enter the educational setting
    """
    return mongo_collection.insert_one(kwargs).inserted_id
