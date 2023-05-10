#!/usr/bin/env python3
'''
Introduces to Redis and caching
'''
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    Method that defines a decorator method that takes single method
    Callable argument and returns a callable
    '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''
        wrapper function that increases the value of the key
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method that takes a data argument and returns a string
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''
        Method that takes argument key and optional callable argument
        fn which will be used to convert the data back to the desired format
        '''
        if fn is None:
            return (self._redis.get(key))

        return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        '''
        Method that automatically parametrize Cache.get with string
        conversion function
        '''
        return (str(self.get(key)))

    def get_int(self, key: str) -> int:
        '''
        Method that automatically parametrize Cache.get with integer
        conversion function
        '''
        return (int(self.get(key)))
