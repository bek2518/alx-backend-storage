#!/usr/bin/env python3
'''
Python function that inserts a new document in a collection
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Function that inserts new document to collection based on kwargs
    '''
    result = mongo_collection.insert_one(kwargs)
    return (result.inserted_id)
