#!/usr/bin/env python3
'''
Python function that returns the list of schools having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Function that returns list of schools from mongo_collection
    which have a specific topic
    '''
    return (mongo_collection.find({"topics": topic}))
