# -*- coding: utf-8 -*-
"""
Desc   Tutorial on OLS, Ridge, Lasso
Source https://www.statsmodels.org/stable/index.html
"""


# Import Libraries -----------------------------------------------------------
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import math

# Load Data -------------------------------------------------------------------
dataset = sm.datasets.get_rdataset('Guerry', 'HistData')
data = dataset.data

# Inspect Data ----------------------------------------------------------------
def inspect_data(dataset):
    print(dataset.__doc__)
    print(dataset.data.head())

data_ints = data.select_dtypes(include=np.number)



# Plot Suicides ~ Prostitutes -------------------------------------------------
def plot(data):
    df = pd.DataFrame({})
    df['prostitutes'] = data.loc[:, 'Prostitutes']
    df['suicides'] = data.loc[:, 'Suicides']
    zeros = df.loc[:, 'prostitutes'] > 0
    df = df[zeros]
    prostitutes_log = [math.log(x) for x in df.loc[:, 'prostitutes']]
    suicides_log = [math.log(x) for x in df.loc[:, 'suicides']]
    plt.scatter(prostitutes_log, suicides_log)
    plt.xlabel('Prostitutes')
    plt.ylabel('Suicides')


# Fit OLS Model Using Formula (Similar to R) ----------------------------------

def fit_using_formula(data):
    fit = smf.ols('Suicides ~ Prostitutes', data=data).fit()
    print(fit.summary())

def fit_using_arrays(data):
    fit = sm.OLS(np.log(data.Suicides), data.Prostitutes).fit()
    print(fit.summary())
    
                                              






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    