#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:27:25 2018

@author: alyshahelenic
"""

import pandas as pd
import sklearn.linear_model as skl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Read File

ABS = pd.read_excel('Absenteeism_at_work.xls', header = 0)

# Limit to analyzing how workload affects absenteeism

WorkLoad = ABS[['ID','Reason for absence','Day of the week','Work load Average/day ',
                'Absenteeism time in hours']]

WorkLoad = WorkLoad.rename(index = str, columns = {'Work load Average/day ':
    'Work load Average/day'})
    
# Linear Regression and Correlation Coefficient of Work load v. Abstenteeism
    
Reg = skl.LinearRegression()

wl = np.asarray(WorkLoad['Work load Average/day'])
wl = wl.reshape(-1,1)
abstime = np.asarray(WorkLoad['Absenteeism time in hours'])
abstime = abstime.reshape(-1,1)

corr, p_value = pearsonr(wl, abstime)
plt.scatter(wl,abstime)
print(corr,p_value)
