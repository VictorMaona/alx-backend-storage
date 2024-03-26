#!/usr/bin/env python3
"""
Give some statistics regarding the Nginx logs kept in the MongoDB
database: logs, nginx, Collection show same as first line such as
There are x logs and x papers in this collection
line two: Techniques
method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in 5 lines.
a single line with path=/status and method=GET
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Def log_stats(mongo_collection, option=None) as a prototype:
    Gives some statistics regarding the MongoDB-stored Nginx logs.
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
