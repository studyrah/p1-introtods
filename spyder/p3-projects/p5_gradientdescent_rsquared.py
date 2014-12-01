# -*- coding: utf-8 -*-
import numpy as np
import pandas

from random import sample

import p3_gradientdescent_2 as gd

def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    """
    If I hadn't already implemented it then something like this:
    
    ave_y = np.mean(data)
    
    #calc numerator
    sst = np.square(data - predictions).sum()
    
    #calc denominator
    ssreg = np.square(data - ave_y).sum()
    
    r_squared = 1 - (sst / ssreg)
    
    return r_squared
    """
    
    return gd.calc_r_squared(data,predictions)

####################################
#
# Note that for the online submission,
# you just complete the compute_r_squared
# method
#
# To work locally I have imported
# answer to previous excercise
# (p3_gradientdescent_2) and just
# call predictions on this to first generate the
# predictions
#
# then well I'd already implemented
# the r squared method so I just call that
#
####################################

turnstile_weather = pandas.read_csv('./turnstile_data_master_with_weather.csv')
    
percent = 15

fulllength = len(turnstile_weather)
samplesize = (fulllength / 100) * percent

# create random index
rindex =  np.array(sample(xrange(len(turnstile_weather)), samplesize))

# get samplesize random rows from df
sample = turnstile_weather.ix[rindex]

# do the grad descent
preds,plot,cost_history = gd.predictions(sample)

print compute_r_squared(sample['ENTRIESn_hourly'], preds)
