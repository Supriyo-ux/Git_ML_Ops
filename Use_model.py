# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:42:16 2021

@author: user
"""

import pickle
import numpy as np

local_classifier = pickle.load(open('classifier.pickle','rb'))
local_scaler = pickle.load(open('sc.pickle','rb'))

