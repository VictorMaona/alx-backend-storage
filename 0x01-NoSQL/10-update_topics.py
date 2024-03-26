#!/usr/bin/env python3
"""
switch up the subject at school
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update several rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
