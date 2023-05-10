#!/usr/bin/env python3
'''
Introduces to Redis and caching
'''
import redis
from uuid import uuid4
from typing import Union


class Cache:
    '''
    Cache class that stores an instance of reddit client
    '''
    def __init__(self):
        '''
        Initialization of Cache class
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method that takes a data argument and returns a string
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return (key)
