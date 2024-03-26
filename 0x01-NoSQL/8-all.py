#!/usr/bin/env python3
"""
There is a useful function in this module that lists every document
"""
import pymongo


def list_all(mongo_collection):
    """
    list every collection
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
