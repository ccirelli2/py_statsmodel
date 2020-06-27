# -*- coding: utf-8 -*-
"""
Desc   Tutorial on Ridge & Lasso Regression
Source https://www.statsmodels.org/stable/regression.html
"""


# Import Libraries ------------------------------------------------------------
import pandas as pd
pd.set_option('display.max.columns', None)
import numpy as np
import statsmodels.api as sm

# Load Data set ---------------------------------------------------------------
'Not clear what methods can be used on a sm dataset'
spector_data = sm.datasets.spector.load(as_pandas = False)

#help(sm.datasets.spector)
#print(sm.datasets.spector.DESCRLONG)


# Fit Model -------------------------------------------------------------------
mod = sm.OLS(spector_data.endog, spector_data.exog)
res = mod.fit()
print(res.summary())



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    