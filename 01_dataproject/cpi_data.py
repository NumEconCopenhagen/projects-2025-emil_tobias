# Imports
import numpy as np
import pandas as pd
from dstapi import DstApi
import matplotlib.pyplot as plt
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.rcParams.update({'axes.grid':True,'grid.color':'black','grid.alpha':'0.25','grid.linestyle':'--'})
plt.rcParams.update({'font.size': 14})

# a. Import data PRIS113 from DST
PRIS113 = DstApi("PRIS113")

# b. Table summary
PRIS113.tablesummary(language="en")

# a. set download parameters
params = {
    'table': 'PRIS113',
    'format': 'BULK', # semicolon separated file
    'lang': 'en',
    'variables': [
        {'code': 'TYPE', 'values': ['INDEKS']},
        {'code': 'Tid', 'values': ['*']}, # '*' is everything
        ]
    
    }

# b. download
CPI = PRIS113.get_data(params=params)

# c. display
display(CPI.head())
display(CPI.info())

# a. function to load PRIS113 data from DST

def load_PRIS113(INDEKS, Tid, varname):

    params = {
        'table': 'PRIS113',
        'format': 'BULK', # semicolon separated file
        'lang': 'en',
        'variables': [
            {'code': 'INDEKS', 'values': [INDEKS]},
            {'code': 'Tid', 'values': ['*']},
            ]
    }    

    # b. download
    df = DstApi('PRIS113').get_data(params=params)

    # c. set types and rename
    df['Tid'] = df['Tid'].astype(int)
    df['INDEKS'] = df['INDEKS'].astype(float)
    df = df.rename(columns={'INDEKS': varname, 'Tid': 'year'})
    df = df.set_index('year').sort_index()
    
    return df

df = load_NAN1('B1GQK','LAN_M','RealGDP')
df['RealGDP_per_capita'] = load_NAN1('B1GQK','LAN_C','RealGDP_per_capita')
df['TotalHours'] = load_NAN1('EMPH_DC','V_M','TotalHours')
df['Emp'] = load_NAN1('EMPM_DC','V_M','Emp')
df.head(5)