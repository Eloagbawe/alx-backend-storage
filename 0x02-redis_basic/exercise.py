#!/usr/bin/env python3
"""This file contains the cache class"""
import redis
from typing import Union
import uuid


class Cache:
    """This represents a cache class"""
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """store method"""
        random_string = str(uuid.uuid4())
        self._redis.set(random_string, data)
        return random_string
