# -*- coding: utf-8 -*-
import numpy as np
import pandas
import pandasql

from random import sample
from datetime import *

import numpy as np
import scipy
import matplotlib.pyplot as plt
import p3_gradientdescent_2 as gd



def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    
    plt.title("Histogram of ENTRIESn_hourly Residuals")
    plt.xlabel("Residual")
    plt.ylabel("Frequency")
    
    
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(alpha=1.0, bins = 100)
    return plt
    

####################################
#
# Note that for the online submission,
# you just complete the plot_residals
# method
#
# To work locally I have imported
# answer to previous excercise
# (p3_gradientdescent_2) and just
# call this to first generate the
# predictions
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

plot_residuals(sample, preds)

plt.show()