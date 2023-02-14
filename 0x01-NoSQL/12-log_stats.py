#!/usr/bin/env python3
"""This file provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(
        nginx_collection.count_documents({'method': {'$regex': 'GET'}})))
    print("\tmethod POST: {}".format(
        nginx_collection.count_documents({'method': {'$regex': 'POST'}})))
    print("\tmethod PUT: {}".format(
        nginx_collection.count_documents({'method': {'$regex': 'PUT'}})))
    print("\tmethod PATCH: {}".format(
        nginx_collection.count_documents({'method': {'$regex': 'PATCH'}})))
    print("\tmethod DELETE: {}".format(
        nginx_collection.count_documents({'method': {'$regex': 'DELETE'}})))
    filtered_logs = nginx_collection.aggregate([
        {
            '$match': {'$and': [{'path': '/status'}, {'method': 'GET'}]}
        },
        {
            '$count': "filters"
        }
    ])
    filtered_logs = list(filtered_logs)
    print("{} status check".format(filtered_logs[0].get('filters')))
