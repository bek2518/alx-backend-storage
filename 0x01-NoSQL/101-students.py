#!/usr/bin/env python3
'''
Python function that returns all students sorted by average score
'''


def top_students(mongo_collection):
    '''
    Function that returns all students from mongo_collection sorted
    by average score
    '''
    result = mongo_collection.aggregate([
        {
            '$project': {
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ])
    return result
