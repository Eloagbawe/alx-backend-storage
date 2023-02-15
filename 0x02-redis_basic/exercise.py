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

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """store method for the cache class"""
        random_string = str(uuid4())
        self._redis.set(random_string, data)
        return random_string
