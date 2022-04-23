#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:40:42 2022

@author: saraansharya
"""

import pickle
import os
import re
from sklearn.linear_model import LogisticRegression


def findGenres(name, plot_outline):
    picklesFolder = './models_BOW'
    pickle_list = os.listdir(picklesFolder)
    pickle_list = [x for x in pickle_list if "PICKLE_" in x]
    name_plot = name + ' - ' + plot_outline
    
    countVec = pickle.load(open('./models_BOW/countVec.pkl','rb'))
    
    input_Value = countVec.transform([name_plot]).A
    
    threshold = 0.25
    output = {}
    for pickleValue in pickle_list:
        label = re.sub('PICKLE_','',pickleValue)
        label = re.sub('\.pkl','',label)
        
        model = pickle.load(open('./models_BOW/'+pickleValue,'rb'))
        
        model_out = model.predict_proba(input_Value)
        
        if model_out[0][1]>threshold:
            output[label] = 1
        else:
            output[label] = 0
            
    prediction = [key for key, value in output.items() if value == 1]
    
    return prediction