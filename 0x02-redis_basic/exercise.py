#!/usr/bin/env python3
"""
    Writing strings to Redis
"""
from typing import Union
import uuid
import redis


class Cache:
    """Define Cashe Class"""
    def __init__(self):
        """
            Store an instance of the Redis
            client as a private variable named _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            method that takes a data argument and returns
            a string. The method should generate a random
            key (e.g. using uuid), store the input data in Redis using
            the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key        
