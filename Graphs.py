#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:16:54 2019

@author: erics
"""

import pandas as pd
import matplotlib.pyplot as plt
from HelperFrames import working_directory

destination = working_directory + '/Graphs/'

def summaryhist(dfcol, bins, xtitle, name, title, save=True):
    fig, ax = plt.subplots()
    ax.hist(dfcol, bins=bins, density=True, color='#3B243D', edgecolor='k')
    ax.grid(True, axis='y', zorder=0)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title(title)
    ax.set_ylabel('Density')
    ax.set_xlabel(xtitle)
    plt.tight_layout()
    if save==True:
        plt.savefig(destination+name+'.png', dpi=200)
    return fig

try:
    mcs = pd.read_pickle('mcs.pkl')
except FileNotFoundError:
    from Data import mcs

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 18.0
plt.rcParams['axes.axisbelow'] = True



q3 = summaryhist(mcs['c3q'], 'auto', 'CGT Risk Adjustment Score', 'q3', 'Age 14')
q2 = summaryhist(mcs['c2q'], 'doane', 'NFER Number Skills', 'q2', 'Age 7')
q1 = summaryhist(mcs['c1q'], 'auto', 'BSRA', 'q1', 'Age 3')

v3 = summaryhist(mcs['c3v'], 'doane', 'BCS70 Vocab', 'v3', 'Age 14')
v2 = summaryhist(mcs['c2v'], 'doane', 'BAS Word Reading', 'v2', 'Age 7')
v1 = summaryhist(mcs['c1v'], 'doane', 'BAS Naming Vocabulary', 'v1', 'Age 3')

internal3 = summaryhist(mcs['internal3'], 'doane', '', 'internal3', 'Age 14')
internal2 = summaryhist(mcs['internal2'], 'doane', '', 'internal2', 'Age 7')
internal1 = summaryhist(mcs['internal1'], 'doane', 'Internalising Score', 'internal1', 'Age 3')

external3 = summaryhist(mcs['external3'], 'doane', '', 'external3', 'Age 14')
external2 = summaryhist(mcs['external2'], 'doane', '', 'external2', 'Age 7')
external1 = summaryhist(mcs['external1'], 'doane', 'Externalising Score', 'external1', 'Age 3')

try:
    nov = pd.read_pickle('nov_means.pkl')
except FileNotFoundError:
    from TimeUseDiaries import nov_means as nov
plt.rcParams['font.size'] = 12.0
time, bx = plt.subplots()
bx.barh(nov.index, nov.values.flatten(), color='#3B243D', edgecolor='k')
bx.set_xticks([i for i in range(0,9)])
bx.grid(True, axis='x', zorder=0)
#bx.spines['right'].set_visible(False)
#bx.spines['top'].set_visible(False)
bx.set_xlabel('Average Hours')
plt.tight_layout()
plt.savefig(destination+'nov_means.png', dpi=200)