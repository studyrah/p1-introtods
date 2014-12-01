# -*- coding: utf-8 -*-
import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    print scipy.stats.shapiro(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0])
    print scipy.stats.shapiro(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1])
    
    plt.figure()
        
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0].hist(alpha=1.0, range=(0,6000), bins = 25) # your code here to plot a historgram for hourly entries when it is raining
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1].hist(alpha=1.0, range=(0,6000), bins = 25) #turnstile_weather['...'] # your code here to plot a historgram for hourly entries when it is not raining


    plt.title("Histogram of ENTRIESn_hourly")
    plt.xlabel("ENTRIESn_hourly")
    plt.ylabel("Frequency")
    plt.legend(("No Rain","Rain"))
  
        
    return plt


turnstile_weather = pandas.read_csv('./turnstile_data_master_with_weather.csv')

plt = entries_histogram(turnstile_weather)

plt.show()

#
# The histogram does not show the typical bell like shape of a normal/gaussian
# distribution (not even skewed), instead it shows a pattern of consistent
# reduction in frequency from one bucket to the next
#

#Here we had a null hypothesis that the mean of the two sets is equal but we received a p value of ~ 0.02, less than the typical p critical of 0.05 so we reject the null hypothesis and assert there is a statistically significant difference between the mean of the two sets.  Non rainy days had the higher mean so we expect that more people (on average) go through the turnstiles on non rainy days.