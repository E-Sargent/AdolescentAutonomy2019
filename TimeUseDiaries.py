#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:48:41 2019

@author: erics
"""
import pandas as pd
import numpy as np
from HelperFrames import working_directory


#This is the code used to compact the time use diaries into a more manageable form
#Takes the sum of occurences for each activity then
tud = pd.read_stata(working_directory+'/S6/stata/stata11/mcs6_cm_tud_harmonised.dta', 
                    columns =  ['MCSID','FCTUDACT','FCTUDMONTH','FCTUDWEEKDAY'], index_col = 'MCSID')
tud = tud.rename(index=str, columns={'FCTUDACT':'activity','FCTUDWEEKDAY':'day'})
tud = tud[(tud['day'] != 'Sunday') & (tud['day'] != 'Saturday')]
nov = tud[(tud['FCTUDMONTH'] == 'November')].copy()

activities = ['Homework','Reading (not for school)','Team ball games and training (e.g. football, hockey)',
              'Jogging, running, walking, hiking', 'Other exercise and sports, dancing, keeping fit, skiing, gymnastics',
              'Cycling', 'Individual ball games and training (e.g. tennis, badminton)', 'Swimming and other water sports',
              'Hobbies, arts and crafts, musical activities, writing stories, poetry etc.', 'Exhibition, museum, library, other cultural events',
              'Cinema, theatre, performance, gig etc.']
ids = np.array(tud.index.unique())

summary = pd.DataFrame(index = ids, columns = activities)
for person in ids:
    summary.loc[person] = tud[tud.index == person]['activity'].value_counts()

summary = summary.fillna(0)

#Categorise activities
summary = pd.DataFrame({'hr':summary['Homework']+summary['Reading (not for school)'],
                        'exercise':summary['Team ball games and training (e.g. football, hockey)']+summary['Jogging, running, walking, hiking']+summary['Other exercise and sports, dancing, keeping fit, skiing, gymnastics']+summary['Cycling']+summary['Individual ball games and training (e.g. tennis, badminton)']+summary['Swimming and other water sports'],
                        'creative':summary['Hobbies, arts and crafts, musical activities, writing stories, poetry etc.']+summary['Exhibition, museum, library, other cultural events']+summary['Cinema, theatre, performance, gig etc.']})

summary.to_pickle('tud_weekday.pkl')


#Subset for month of november 
nov_ids = nov.index.unique()

novsum = pd.DataFrame(index = nov_ids, columns = nov['activity'].value_counts().index)
for person in nov_ids:
    novsum.loc[person] = nov[nov.index == person]['activity'].value_counts()
    
novsum = novsum.fillna(0)

td = pd.DataFrame({'Homework / Reading':novsum['Homework']+novsum['Reading (not for school)'],
                        'Exercise':novsum['Team ball games and training (e.g. football, hockey)']+novsum['Jogging, running, walking, hiking']+novsum['Other exercise and sports, dancing, keeping fit, skiing, gymnastics']+novsum['Cycling']+novsum['Individual ball games and training (e.g. tennis, badminton)']+novsum['Swimming and other water sports'],
                        'Creative':novsum['Hobbies, arts and crafts, musical activities, writing stories, poetry etc.']+novsum['Exhibition, museum, library, other cultural events']+novsum['Cinema, theatre, performance, gig etc.'],
                        'School':novsum['School breaks']+novsum['In class']+novsum['School clubs'],
                        'Sleep':novsum['Sleeping and resting (including sick in bed)'],
                        'Social Media':novsum['Browsing and updating social networking sites (e.g. Twitter, Facebook, BBM, Snapchat)'] + novsum['General internet browsing, programming (not time on social networking sites)']+novsum['Answering emails, instant messaging, texting'],
                        'Recreation':novsum['Playing electronic games and Apps']+novsum['Watch TV, DVDs, downloaded videos']})
nov_means = pd.DataFrame.from_dict({col:td[col].mean()/6 for col in td.columns}, orient='index')
nov_means.to_pickle('nov_means.pkl')