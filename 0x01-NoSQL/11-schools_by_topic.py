#!/usr/bin/env python3
"""
search by subject
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    search by topic
    """
    return mongo_collection.find({"topics": topic})
