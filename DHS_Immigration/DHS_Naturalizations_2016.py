#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:18:52 2018

@author: alyshahelenic
"""

import numpy as np
import pandas as pd

# where DACA refugees went by state in 2016
DHS = pd.read_excel('DHS_Naturalizations_2016_supplement_fy2016_natzsuptable1d.xls',header=1,
                    skiprows=2)

DHS = DHS.drop(DHS.index[0]) # remove first few rows of header info

# extract continent-of-origin data and replace '-' with 0s
DHS_cont = DHS.drop(DHS.index[8:234])
DHS_cont = DHS_cont.replace(to_replace = '-', value = 0)

# extract country-of-origin data and replace '-' with 0s 
# & withheld info with NaN
DHS_try = DHS.drop(DHS.index[0:10])
DHS_try = DHS_try.drop(DHS.index[229:234])
DHS_try = DHS_try.replace(to_replace = '-', value = 0)
DHS_try = DHS_try.replace(to_replace = 'D', value = np.nan)
DHS_try = DHS_try.reset_index(drop = True)

# Add row for area of country and populate
DHS_cont = DHS_cont.append(pd.Series([np.nan]), ignore_index= True)
DHS_cont = DHS_cont.drop(DHS_cont.columns[58],axis = 1)
DHS_cont = DHS_cont.rename(index = str, columns = {"U.S. Territories1":"U.S. Territories"})
DHS_cont = DHS_cont.replace(to_replace = 'D', value = np.nan)
DHS_cont.at[8,'Region and country of birth'] = 'US Region'
DHS_cont.at[8,['Connecticut','Maine','Massachusetts','New Hampshire','Vermont',
                'Rhode Island']] = 'New England'
DHS_cont.at[8,['New Jersey','New York','Pennsylvania']] = 'Mid-Atlantic'  
DHS_cont.at[8,['Illinois','Indiana','Michigan','Ohio','Wisconsin']] = 'East North Central'
DHS_cont.at[8,['Iowa','Kansas','Minnesota','Missouri','Nebraska','North Dakota',
               'South Dakota']] = 'West North Central'
DHS_cont.at[8,['Delaware','Florida','Georgia','Maryland','North Carolina',
               'South Carolina','Virginia','District of Columbia','West Virginia'
               ]] = 'South Atlantic'  
DHS_cont.at[8,['Alabama','Kentucky','Mississippi','Tennessee']] = 'East South Central' 
DHS_cont.at[8,['Arkansas','Louisiana','Oklahoma','Texas']] = 'West South Central' 
DHS_cont.at[8,['Arizona','Colorado','Idaho','Montana','Nevada','New Mexico',
               'Utah','Wyoming']] = 'Mountain'
DHS_cont.at[8,['Alaska','California','Hawaii','Oregon','Washington']] = 'Pacific'
DHS_cont.at[8,['Puerto Rico','Guam','U.S. Armed Services Posts','U.S. Territories','Unknown']] = 'Other'
    
# Add row for area of country and populate
DHS_try = DHS_try.append(pd.Series([np.nan]), ignore_index= True)
DHS_try = DHS_try.drop(DHS_try.columns[58],axis = 1)
DHS_try.at[219,'Region and country of birth'] = 'US Area'
DHS_try.at[219,['Connecticut','Maine','Massachusetts','New Hampshire','Vermont',
                'Rhode Island']] = 'New England'

print(DHS_cont)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('DHSimm.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
DHS_cont.to_excel(writer, sheet_name='Sheet1',na_rep='D')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
