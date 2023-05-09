#!/usr/bin/env python3
'''
Python function that changes all topics of a school document
'''


def update_topics(mongo_collection, name, topics):
    '''
    Function that changes all topic of mongo_collection with
    the provided name argument and topic to be inserted
    '''
    return (mongo_collection.update_many({"name": name},
                                         {"$set": {"topics": topics}}))
