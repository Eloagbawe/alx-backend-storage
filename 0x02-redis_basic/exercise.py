#!/usr/bin/env python3
"""This file contains the cache class"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """This represents a cache class"""
    def __init__(self) -> None:
        """initialization of the class cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method for the cache class"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
