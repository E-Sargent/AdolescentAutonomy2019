#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:16:27 2019

@author: erics
"""

import pandas as pd
import statsmodels.api as sm

try:
    mcs = pd.read_pickle('mcs.pkl')
except FileNotFoundError:
    from Data import mcs


#------------------------------------------------------------------------------
#Identifying Factor Loadings and measurement error severity
#------------------------------------------------------------------------------
#Factor Loadings
fl = {'c1':(mcs['c1v'].cov(mcs['c2q']))/(mcs['c1q'].cov(mcs['c2q'])),
      'c2':(mcs['c2v'].cov(mcs['c3q']))/(mcs['c2q'].cov(mcs['c3q'])),
      'c3':(mcs['c2q'].cov(mcs['c3v']))/(mcs['c2q'].cov(mcs['c3q'])),
      'n1':(mcs['external1'].cov(mcs['internal2']))/(mcs['internal1'].cov(mcs['internal2'])),
      'n2':(mcs['external2'].cov(mcs['internal3']))/(mcs['internal2'].cov(mcs['internal3'])),
      'n3':(mcs['internal2'].cov(mcs['external3']))/(mcs['internal2'].cov(mcs['internal3']))}

#Latent Ability Variance
var = {'c1':(mcs['c1q'].cov(mcs['c1v']))/fl['c1'],
        'c2':(mcs['c2q'].cov(mcs['c2v']))/fl['c2'],
        'c3':(mcs['c3q'].cov(mcs['c3v']))/fl['c3'],
        'n1':(mcs['internal1'].cov(mcs['external1']))/fl['n1'],
        'n2':(mcs['internal2'].cov(mcs['external2']))/fl['n2'],
        'n3':(mcs['internal3'].cov(mcs['external3']))/fl['n3']}

#Measurement Error Variance
vare = {'c1':(mcs['c1q'].var() -var['c1']),
        'c2':(mcs['c2q'].var() -var['c2']),
        'c3':(mcs['c3q'].var() -var['c3']),
        'n1':(mcs['internal1'].var() -var['n1']),
        'n2':(mcs['internal2'].var() -var['n2']),
        'n3':(mcs['internal3'].var() -var['n3'])}

#Explained Variance
explained_variance = {'c1':var['c1']/(var['c1']+vare['c1']),
                      'c2':var['c2']/(var['c2']+vare['c2']),
                      'c3':var['c3']/(var['c3']+vare['c3']),
                      'n1':var['n1']/(var['n1']+vare['n1']),
                      'n2':var['n2']/(var['n2']+vare['n2']),
                      'n3':var['n3']/(var['n3']+vare['n3'])}

unexplained_variance = map(lambda i: 1-i, list(explained_variance.values()))

#------------------------------------------------------------------------------
#Basic production functions for t = 2, t =3
#Uses matrix formula:
# A_t = γA_t-1 + ρX_t + η_t
#------------------------------------------------------------------------------

#Third Sweep, self-investment measured as effort
#Let e denote effort
x3e = ['c2p','n2p','z3','f3','s3','ma']

c3e_model = sm.OLS(mcs['c3p'], exog=mcs[x3e])
c3e_fit = c3e_model.fit()
#print(c3e_fit.summary())

n3e_model = sm.OLS(mcs['n3p'], exog=mcs[x3e])
n3e_fit = n3e_model.fit()
#print(n3e_fit.summary())

#Third Sweep, self-investment measured with time use diaries
#Let t denote time use
x3t = ['c2p','n2p','f3','s3','ma', 'hr','exercise','creative']

c3t_model = sm.OLS(mcs['c3p'], exog=mcs[x3t])
c3t_fit = c3t_model.fit()
#print(c3t_fit.summary())

n3t_model = sm.OLS(mcs['n3p'], exog=mcs[x3t])
n3t_fit = n3t_model.fit()
#print(n3t_fit.summary())

#Third Sweep, self-investment measured using both effort and time use diaries
#Let b denote both time use and effort
x3b = ['c2p','n2p','f3','s3','ma', 'hr','exercise','creative','z3']

c3b_model = sm.OLS(mcs['c3p'], mcs[x3b])
c3b_fit = c3b_model.fit()
#print(c3b_fit.summary())

n3b_model = sm.OLS(mcs['n3p'], mcs[x3b])
n3b_fit = n3b_model.fit()
#print(n3b_fit.summary())

#Second Sweep, self-investment measured as effort
x2e = ['c1p', 'n1p','z2','f2','s2','ma']

c2e_model = sm.OLS(mcs['c2p'], exog=mcs[x2e])
c2e_fit = c2e_model.fit()
#print(c2e_fit.summary())

n2e_model = sm.OLS(mcs['n2p'], exog=mcs[x2e])
n2e_fit = n2e_model.fit()

#------------------------------------------------------------------------------
#Basic production functions excluding self-investment
#------------------------------------------------------------------------------
#Third Sweep, excluding measure of self-investment
#Let x denote exogenous
x3 = ['c2p','n2p','f3','s3','ma']

c3_model = sm.OLS(mcs['c3p'], exog=mcs[x3])
c3_fit = c3_model.fit()
#print(c3_fit.summary())

n3_model = sm.OLS(mcs['n3p'], exog=mcs[x3])
n3_fit = n3_model.fit()
#print(n3_fit.summary())

#Second Sweep, no self-investment
x2 = ['c1p', 'n1p','f2','s2','ma']

c2_model = sm.OLS(mcs['c2p'], exog=mcs[x2])
c2_fit = c2_model.fit()
#print(c2e_fit.summary())

n2_model = sm.OLS(mcs['n2p'], exog=mcs[x2])
n2_fit = n2_model.fit()

#------------------------------------------------------------------------------
#Production functions which account for time-invariant omitted inputs
#Uses matrix formula:
# A_t - A_t-1 = γ(A_t-1 - A_t-2) + ρ(X_t - X_t-1) + (u_t - u_t-1)
#------------------------------------------------------------------------------
#Investment difference between t = 3, t = 2
#Let d denote difference
mcs['z3d'] = mcs['z3'] - mcs['z2']
mcs['f3d'] = mcs['f3'] - mcs['f2']
mcs['s3d'] = mcs['s3'] - mcs['s2']

#Let e denote endogenous
mcs['ecd'] = mcs['c3q'] - mcs['c2q']
mcs['xcd'] = mcs['c3v'] - mcs['c2v']

mcs['end'] = mcs['internal3'] - mcs['internal2']
mcs['xnd'] = mcs['external3'] - mcs['external2']

c3d_model = sm.OLS(mcs['ecd'], mcs['xcd'])
c3d_fit = c3d_model.fit()
mcs['c3d'] = c3d_fit.predict()

n3d_model = sm.OLS(mcs['end'], mcs['xnd'])
n3d_fit = n3d_model.fit()
mcs['n3d'] = n3d_fit.predict()

#Third Sweep first differences, time invariant
xdc = ['c2p','c1p','n3d','z3d','f3d','s3d']
c3s_model =  sm.OLS(mcs['c3p'], exog=mcs[xdc])
c3s_fit = c3s_model.fit()
#print(c3d_fit.summary())

xdn = ['n2p','n1p','c3d','z3d','f3d','s3d']
n3s_model = sm.OLS(mcs['n3p'], exog=mcs[xdn])
n3s_fit = n3s_model.fit()
#print(n3d_fit.summary())

#------------------------------------------------------------------------------
#Production functions which account for time-varying omitted inputs
#Uses matrix formula:
# A_t - A_t-1 = γ_t*A_t-1 - γ_t-1*A_t-2 + ρ_t*X_t - ρ_t*X_t-1 + u_t - u_t-1
#------------------------------------------------------------------------------
#Third sweep first differences, time varying
#Let v denote time-varying differences
x3v = ['c2p','n2p','c1p','n1p','z3','f3','s3','ma','z2','f2','s2']
c3v_model = sm.OLS(mcs['c3p'], exog=mcs[x3v])
c3v_fit = c3v_model.fit()

n3v_model = sm.OLS(mcs['n3p'], exog=mcs[x3v])
n3v_fit = n3v_model.fit()


#------------------------------------------------------------------------------
#Identifying variance in the base equations caused by omitted inputs
#------------------------------------------------------------------------------
residuals = pd.DataFrame({'cog2':c2e_fit.resid,
                          'cog3':c3e_fit.resid,
                          'ncog2':n2e_fit.resid,
                          'ncog3':n3e_fit.resid})

rcov = residuals.cov()
flr = {'n2':rcov.loc['ncog2','cog3']/rcov.loc['cog2','cog3'],
       'n3':rcov.loc['ncog3','cog2']/rcov.loc['cog2','cog3']}

varom = {'t2':rcov.loc['cog2','ncog2']/flr['n2'],
         't3':rcov.loc['cog3','ncog3']/flr['n3']}

varan = {'n2':residuals['ncog2'].var()-(flr['n2']**2)*varom['t2'],
         'n3':residuals['ncog3'].var()-(flr['n3']**3)*varom['t3'],
         'c2':residuals['cog2'].var()-varom['t2'],
         'c3':residuals['cog3'].var()-varom['t3']}

explained_residual_variance = {'n2':varom['t2']/(varom['t2']+varan['n2']),
                               'n3':varom['t3']/(varom['t3']+varan['n3']),
                               'c2':varom['t2']/(varom['t2']+varan['c2']),
                               'c3':varom['t3']/(varom['t3']+varan['c3'])}

unexplained_residual_variance = map(lambda i: 1-i, list(explained_residual_variance.values()))

#------------------------------------------------------------------------------
#Identifying variance in the effort omitted equations caused by omitted inputs
#------------------------------------------------------------------------------
#Let k denote estimations which ignore self-investment
kresiduals = pd.DataFrame({'cog2':c2_fit.resid,
                          'cog3':c3_fit.resid,
                          'ncog2':n2_fit.resid,
                          'ncog3':n3_fit.resid})

kcov = residuals.cov()
flk = {'n2':kcov.loc['ncog2','cog3']/kcov.loc['cog2','cog3'],
       'n3':kcov.loc['ncog3','cog2']/kcov.loc['cog2','cog3']}

varomk = {'t2':kcov.loc['cog2','ncog2']/flk['n2'],
         't3':kcov.loc['cog3','ncog3']/flk['n3']}

varank = {'n2':kresiduals['ncog2'].var()-(flk['n2']**2)*varomk['t2'],
         'n3':kresiduals['ncog3'].var()-(flk['n3']**3)*varomk['t3'],
         'c2':kresiduals['cog2'].var()-varomk['t2'],
         'c3':kresiduals['cog3'].var()-varomk['t3']}

explained_kresidual_variance = {'n2':varomk['t2']/(varomk['t2']+varank['n2']),
                               'n3':varomk['t3']/(varomk['t3']+varank['n3']),
                               'c2':varomk['t2']/(varomk['t2']+varank['c2']),
                               'c3':varomk['t3']/(varomk['t3']+varank['c3'])}

unexplained_kresidual_variance = map(lambda i: 1-i, list(explained_kresidual_variance.values()))
