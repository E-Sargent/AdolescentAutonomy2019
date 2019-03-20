#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a helper file containing three objects: the "variables" DataFrame
which stores information about the variables read from data files, the "files"
DataFrame which stores information about those DataFiles, and "mappings" which is
a dictionary containing mappings for non-numeric data.
"""
import pandas as pd
import os
import numpy as np
from collections import defaultdict
from HelperFunctions import zscore



working_directory = os.getcwd()
s6d = working_directory + '/S6/stata/stata11/'
s4d = working_directory + '/S4/stata11_se/'
s2d = working_directory + '/S2/stata11_se/'
s1d = working_directory + '/S1/stata11/'

#Column meanings:
#"dataname" is how the variable is stored in the file
#"source" is which file the variable is stored in
#"transformation" records how the variable should be transformed for analysis
#"outcome" indicates whether the variables is tied to a dependent variable, it takes a value of 1 if a higher score is good, -1 if a higher score is bad
#"map" is what mapping dictionary within the "mappings" dictionary should be applied to the variables
#"description" is a brief description of what the variable represents
variables = pd.DataFrame.from_dict({'i3' :['FOEDE000','mcs6_family_derived.dta',        np.log, 0,  None, 's6 Weekly family income'],
      's3' :['FPSCTY00', 'mcs6_parent_cm_interview.dta',      None,   0,  's3',   's6 Does Parent Pay School Fees'],
      'c3q':['FCGTRISKA','mcs6_cm_derived.dta',              zscore, 1,  None,   'CGT Risk Adjustment Score'],
      'c3v':['FCWRDSC',  'mcs6_cm_derived.dta',               zscore, 1,  None,  's6 Verbal score'],
      'n3e':['FEMOTION', 'mcs6_cm_derived.dta',               zscore, -1, None,   's6 SDQ Emotional'],
      'n3c':['FCONDUCT', 'mcs6_cm_derived.dta',               zscore, -1, None,   's6 SDQ Conduct'],
      'n3h':['FHYPER',   'mcs6_cm_derived.dta',               zscore, -1, None,   's6 SDQ Hyperactivity'],
      'n3p':['FPEER' ,   'mcs6_cm_derived.dta',               zscore, -1, None,   's6 SDQ Peer Problems'],
      'z31':['FCSCBE00', 'mcs6_cm_interview.dta',             zscore, 0,  'z31', 's6 How often try best at school'],
      'z32':['FCMISB00', 'mcs6_cm_interview.dta',             zscore, 0,  'z32', 's6 How misbehave in class'],
      'z33':['FCTRUA00', 'mcs6_cm_interview.dta',             None, 0,  'z33',   's6 Have you missed school without permission'],
      'tru':['FCTRUF00', 'mcs6_cm_interview.dta',             None, 0,  'tru',   's6 Have you missed school without permission'],
      'f31':['FCOTWD00', 'mcs6_cm_interview.dta',             zscore, 0,  'f3',  's6 Parents know what'],
      'f32':['FCOTWI00', 'mcs6_cm_interview.dta',             zscore, 0,  'f3',   's6 Parents know who'],
      'f33':['FCOUTW00', 'mcs6_cm_interview.dta',             zscore, 0,  'f3',   's6 Parents know where'],
      'i2' :['DOEDE000', 'mcs4_derived_variables.dta',        np.log, 0,  None,    's4 Weekly family income'],
      's2' :['dmsctya0', 'mcs4_parent_interview.dta',         None,   0,  's2',   's4 Does Parent Pay School Fees'],
      'c2q':['DCNSCO00', 'mcs4_cm_assessment.dta',            zscore, 1,  None,   'NFER Number skills score'],
      'c2v':['DCWRSC00', 'mcs4_cm_assessment.dta',            zscore, 1,  None,  's4 Word reading score'],
      'n2e':['DDEMOTA0', 'mcs4_derived_variables.dta',        zscore, -1, None,   's4 SDQ Emotional'],
      'n2c':['DDCONDA0', 'mcs4_derived_variables.dta',        zscore, -1, None,    's4 SDQ Conduct'],
      'n2h':['DDHYPEA0', 'mcs4_derived_variables.dta',        zscore, -1, None,    's4 SDQ Hyperactivity'],
      'n2p':['DDPEERA0', 'mcs4_derived_variables.dta',        zscore, -1, None,    's4 SDQ Peer Problems'],
      'z21':['dcsc0027', 'mcs4_cm_self_completion_final.dta', zscore, 0,  'z21', 's4 How often try best at school'],
      'z22':['dcsc0030', 'mcs4_cm_self_completion_final.dta', zscore, 0,  'z22', 's4 How misbehave in class'],
      'z23':['dcsc0035', 'mcs4_cm_self_completion_final.dta', zscore, 0,  'z23', 's4 How often talk over work'],
      'f21':['dmreofa0', 'mcs4_parent_interview.dta',         None,   0,  'f2',    's4 Reading'],
      'f22':['dmsitsa0', 'mcs4_parent_interview.dta',         None,   0,  'f2',   's4 Stories'],
      'f23':['dmplmua0', 'mcs4_parent_interview.dta',         None,   0,  'f2',   's4 Musical activites'],
      'f24':['dmpamaa0', 'mcs4_parent_interview.dta',         None,   0,  'f2',   's4 Draw and paint'],
      'f25':['dmactia0', 'mcs4_parent_interview.dta',         None,   0,  'f2',   's4 Active games '],
      'f26':['dmgamea0', 'mcs4_parent_interview.dta',         None,   0,  'f2',   's4 Indoor games'],
      'i1' :['BDOEDE00', 'mcs2_derived_variables.dta',        np.log, 0,  None,   's2 Weekly income'],
      's1' :['bmclsta0', 'mcs2_parent_interview.dta',         None,   0,  's1',   's2 Primary child care arrangement'],
      'c1q':['bdsrcs00', 'mcs2_child_assessment_data.dta',    zscore, 1,  None,   's2 Bracken composite'],
      'c1v':['bdbasr00', 'mcs2_child_assessment_data.dta',    zscore, 1,  None,   's2 Naming Vocab Raw Score'],
      'n1e':['BDEMOTA0', 'mcs2_derived_variables.dta',        zscore, -1, None,  's2 SDQ Emotional'],
      'n1c':['BDCONDA0', 'mcs2_derived_variables.dta',        zscore, -1, None,   's2 SDQ Conduct'],
      'n1h':['BDHYPEA0', 'mcs2_derived_variables.dta',        zscore, -1, None,   's2 SDQ Hyperactivity'],
      'n1p':['BDPEERA0', 'mcs2_derived_variables.dta',        zscore, -1, None,   's2 SDQ Peer Problems'],
      'f11':['bmoflia0', 'mcs2_parent_interview.dta',         None,   0,  'f11', 's2 Library'],
      'f12':['bmofaba0', 'mcs2_parent_interview.dta',         None,   0,  'f12', 's2 Alphabet'],
      'f13':['bmofcoa0', 'mcs2_parent_interview.dta',         None,   0,  'f13', 's2 Counting'],
      'f14':['bmofsoa0', 'mcs2_parent_interview.dta',         None,   0,  'f14', 's2 Songs'],
      'f15':['bmofrea0', 'mcs2_parent_interview.dta',         None,   0,  'f15', 's2 Reading'],
      'ma' :['amacqu00', 'mcs1_parent_interview.dta',         None,   0,  'ma',  "Mother's education"]
      }, orient='index', columns=['dataname','source','transformation','outcome','map','description'])

#Column meanings:
#"dir" is the directory the file is stored in
#"dupes" is whether or not the file contains duplicated entried for cohort members
#"conds" is the set of conditions necessary to clean the file of duplicate entries (as defined by the "cleandupes" fuction)
#"lower" indicates if the file's columns are written in upper or lower case letters
files = pd.DataFrame.from_dict({'mcs6_family_derived.dta':[s6d,False, None, None],
    'mcs6_parent_cm_interview.dta':[s6d,True,[('FPNUM00',1),('FCNUM00','1st Cohort Member of the family')],None],
    'mcs6_cm_derived.dta':[s6d,True,[('FCNUM00','1st Cohort Member of the family')],None],
    'mcs6_cm_interview.dta':[s6d,True,[('FCNUM00','1st Cohort Member of the family')],None],
    'mcs4_derived_variables.dta':[s4d,False,None,None],
    'mcs4_parent_interview.dta':[s4d,False,None,True],
    'mcs4_cm_assessment.dta':[s4d,True,[('DCCNUM00',1)],None],
    'mcs4_cm_self_completion_final.dta':[s4d,True,[('dccnum00',1)],None],
    'mcs2_derived_variables.dta':[s2d,False,None,None],
    'mcs2_parent_interview.dta':[s2d,False,None,True],
    'mcs2_child_assessment_data.dta':[s2d,True,[('bhcnum00',1)],None],
    'mcs1_parent_interview.dta':[s1d,False,None,True]
    },orient='index', columns=['dir','dupes','conds','lower'])

#A dictionary containing default dictionary maps for relevant variables
#Default dictionaries allow me to give a default mapping for values which don't
#explicitly appear in the dictionary
mappings = {'z31':defaultdict(lambda:0, {'Never': 0,
                             'Some of the time': 1,
                             'All of the time': 3,
                             'Most of the time': 2,
                             'Not applicable': 0}),
            'z32':defaultdict(lambda:0, {'Never': 3,
                             'Some of the time': 1,
                             'All of the time': 0,
                             'Most of the time': 2,
                             'Not applicable': 0}),
            'z33':defaultdict(lambda:1, {'Yes': 0}),
            'tru':defaultdict(lambda:0, {'Once': 0,
                                         'Less often than once a month':1}),
            'f3':defaultdict(lambda:0, {'Always': 3,
                             'Sometimes': 1,
                             'Usually': 2,
                             'Not applicable': 0,
                             'Never': 0,
                             "Don't know": 0,
                             "Don't want to answer": 0}),
            's3':defaultdict(lambda:0, {'Yes':1}),
            's2':defaultdict(lambda:0, {'Yes':1}),
            'z21':defaultdict(lambda:0, {'Never': 0,
                                 'Some of the time': 1,
                                 'All of the time': 2,
                                 'Not answered (9)': 0}),
            'z22':defaultdict(lambda:0, {'Never': 0,
                                 'Some of the time': 1,
                                 'All of the time': 2,
                                 'Not answered (9)': 0}),
            'z23':defaultdict(lambda:0, {'Never': 2,
                             'Some of the time': 1,
                             'All of the time': 0,
                             'Not answered (9)': 0}),
            'f2':defaultdict(lambda:0, {'Several times a week': 4,
                             'Not at all': 0,
                             'Every day or almost every day': 5,
                             'Once or twice a week': 3,
                             'Once or twice a month': 2,
                             'Less often than once a month': 1,
                             "Don't Know": 0}),
            'f11':defaultdict(lambda:0, {'Not Applicable': 0,
                             'Once a month': 2,
                             'Or, once a week': 4,
                             'On special occasions': 1,
                             'Once a fortnight': 3}),
            'f12':defaultdict(lambda:0, {' 6 times a week': 6,
                                         '3 times a week': 3,
                                         '7 times a week/constantly': 7,
                                         '4 times a week': 4,
                                         'Not applicable': 0,
                                         '1-2 days per week': 2,
                                         'Occasionally or less than once a week': 1,
                                         '5 times a week': 5}),
            'f13':defaultdict(lambda:0, {' 6 times a week': 6,
                                         '3 times a week': 3,
                                         '7 times a week/constantly': 7,
                                         '4 times a week': 4,
                                         'Not applicable': 0,
                                         '1-2 days per week': 2,
                                         'Occasionally or less than once a week': 1,
                                         '5 times a week': 5}),
            'f14':defaultdict(lambda:0, {' 6 times a week': 6,
                                         '3 times a week': 3,
                                         '7 times a week/constantly': 7,
                                         '4 times a week': 4,
                                         'Not applicable': 0,
                                         '1-2 days per week': 2,
                                         'Occasionally or less than once a week': 1,
                                         '5 times a week': 5}),
            'f15':defaultdict(lambda:0, {'Not at all':0, 'Less often':1,
                             'Once or twice a month':2,
                             'Once or twice a week':3,
                             'Several times a week':4,
                             'Every day':5}),
            's1':defaultdict(lambda:0, {'Private   independent day nursery crech':1,
                                        ' Nursery or Reception class in a primar':1,
                                        'Nursery School':1,
                                        'Local Authority nursery': 1,
                                        'Special day school or nursery or unit f': 1}),
            'ma':defaultdict(lambda:0, {'O level / GCSE grades A-C': 1,
                                 'First degree': 4,
                                 'GCSE grades D-G': 0,
                                 'Higher degree': 5,
                                 'Diplomas in higher education': 3,
                                 'None of these qualifications': 0,
                                 'A / AS / S levels': 2,
                                 'Other academic qualifications (incl. overseas)': 3})}


