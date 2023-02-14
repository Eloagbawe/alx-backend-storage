#!/usr/bin/env python3
"""This file provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


# def log_stats(collection):
#     """This function provides some stats about Nginx logs
#     stored in MongoDB"""
#     count = collection.count_documents({})
#     get_count = collection.count_documents({'method': {'$regex': 'GET'}})
#     post_count = collection.count_documents(
#         {'method': {'$regex': 'POST'}})
#     put_count = collection.count_documents(
#         {'method': {'$regex': 'PUT'}})
#     patch_count = collection.count_documents(
#         {'method': {'$regex': 'PATCH'}})
#     delete_count = collection.count_documents(
#         {'method': {'$regex': 'DELETE'}})
#     status_check = collection.count_documents({'path': '/status'})
#     print(f"{count} logs")
#     print("Methods:")
#     print(f"\tmethod GET: {get_count}")
#     print(f"\tmethod POST: {post_count}")
#     print(f"\tmethod PUT: {put_count}")
#     print(f"\tmethod PATCH: {patch_count}")
#     print(f"\tmethod DELETE: {delete_count}")
#     print(f"{status_check} status check")
#
#     filtered_logs = nginx_collection.aggregate([
#         {
#             '$match': {'$and': [{'path': '/status'}, {'method': 'GET'}]}
#         },
#         {
#             '$count': "filters"
#         }
#     ])
#     filtered_logs = list(filtered_logs)
#     print("{} status check".format(filtered_logs[0].get('filters')))

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
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
