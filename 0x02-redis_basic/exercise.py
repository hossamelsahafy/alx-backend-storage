#!/usr/bin/env python3
"""
    Writing strings to Redis
"""
from typing import Union, Callable, Optional
import uuid
import redis
import functools


def count_calls(method: callable):
    """
        we will implement a system to count how many times
        methods of the Cache class are called
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count method calls"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Define Cashe Class"""
    def __init__(self):
        """
            Store an instance of the Redis
            client as a private variable named _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    @count_calls
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


    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
            method that take a key string argument and
            an optional Callable argument named fn.
            This callable will be used to
            convert the data back to the desired format. 
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data


    def get_str(self, key: str)-> Optional[str]:
        """
            Method that retrieves a string from Redis
            using the get method
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))


    def get_int(self, key: int) -> Optional[int]:
        """
            Method that retrieves a Int from Redis
            using the get method
        """
        return self.get(key, fn=int)
