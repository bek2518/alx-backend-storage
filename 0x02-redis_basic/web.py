#!/usr/bin/env python3
'''
Obtain HTML content of a particular URL and returns it
'''
import requests
import redis
from functools import wraps
from typing import Callable


r = redis.Redis()


def cache_tracker(f: Callable):
    '''
    Decorator function that sets expiry for web cache and tracks
    how many times a particular url was accessed
    '''
    @wraps(f)
    def wrapper(url):
        counter_key = f"count:{url}"
        cache_key = f"cache:{url}"

        if r.get(counter_key) is not None:
            r.incr(counter_key)
            return r.get(counter_key).decode()
        r.setex(cache_key, 10, f(url))
        r.setex(counter_key, 10, 1)
        return (f(url))
    return wrapper


@cache_tracker
def get_page(url: str) -> str:
    '''
    Function that tracks how many times URL was accesses and cache
    the result with an expiration of 10 seconds
    '''
    response = requests.get(url)
    return (response.content.decode("utf-8"))
