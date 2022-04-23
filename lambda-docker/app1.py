#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:14:00 2022

@author: saraansharya
"""
import json
import requests
import pickle
import os
import re
#import sys
from runModel1 import findGenres

#print("Hello World")



def handler(event,context):

    predictions = findGenres(event['queryStringParameters']['name'],event['queryStringParameters']['plot'])
    #predictions = ['Crime', 'Drama', 'Action']


    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Predictions ": predictions
        })
    }
