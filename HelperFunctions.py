#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:22:32 2019

@author: erics
"""

import pandas as pd

def zscore(dfcol, flip_sign = False):
    '''
    Takes a column and returns the zscore transformation of the column
    '''
    x = 1
    if flip_sign==True:
        x = -1
    result = x*(dfcol - dfcol.mean())/dfcol.std()
    return result

def cleandupes(df, conditions):
    '''
    Takes in a dataframe and conditions for cleaning, conditions must be a list
    (or similar) of conditions in format (column, expexted value). For example
    if you wanted the conditions (df['apple']=='red')&(df['puppy']=='cute') these
    could be passed as condition = [('apple','red),('puppy','cute)]

    Also reindexes to use MCSID as the index
    '''
    for con in conditions:
        df = df[df[con[0]] == con[1]]
    if 'MCSID' in df.columns:
        df = df.set_index('MCSID')
    elif 'mcsid' in df.columns:
        df = df.set_index('mcsid')
        df.index.names = ['MCSID']
    return df

def isnumeric(i):
    if type(i) in (int,float):
        return True
    else:
        return False

i = pd.Series('mcsid')
I = pd.Series('MCSID')
raw = {}
