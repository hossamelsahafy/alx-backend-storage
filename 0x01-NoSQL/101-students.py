#!/usr/bin/env python3
"""
    function that returns all students sorted by average score
"""

from pymongo import DESCENDING

def top_students(mongo_collection):
    """top Students""" 
    students = mongo_collection.find()
    top_students = []

    for student in students:
        total_score = 0.0
        num_topics = len(student['topics'])
        
        for topic in student['topics']:
            total_score += topic['score']
        
        if num_topics > 0:
            average_score = total_score / num_topics
        else:
            average_score = 0.0
        
        student['_id'] = str(student['_id'])
        student['averageScore'] = average_score
        top_students.append(student)

    top_students.sort(key=lambda x: x['averageScore'], reverse=True)

    result = []
    for student in top_students:
        result.append({
            '_id': student['_id'],
            'name': student['name'],
            'averageScore': student['averageScore']
        })

    return result
