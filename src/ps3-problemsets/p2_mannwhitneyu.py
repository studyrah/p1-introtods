# -*- coding: utf-8 -*-
import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    ### YOUR CODE HERE ###
    without_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]
    with_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1] 
    
    
    without_rain_mean = np.mean(without_rain)
    with_rain_mean = np.mean(with_rain)
    
    print "without rain n: " + str(len(without_rain))
    print "with rain n: " + str(len(with_rain))    
    
    print "mean without rain: " + str(np.mean(without_rain))
    print "mean with rain: " + str(np.mean(with_rain))

    print "median without rain: " + str(np.median(without_rain))
    print "median with rain: " + str(np.median(with_rain))
    
    
                                
    U,p = scipy.stats.mannwhitneyu(with_rain, without_rain)    
    
    print "U: " + str(U)
    print "p: " + str(p)
    print "p: " + str(p * 2)    
    
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

turnstile_weather = pandas.read_csv('./turnstile_data_master_with_weather.csv')

print mann_whitney_plus_means(turnstile_weather)

#  Ans = (1105.4463767458733, 1090.278780151855, 1924409167.0, 0.024999912793489721)
#
#  So our P value is 0.02, so assuming a p critical of 0.05 we can reasonably
# reject the null hypothesis and thus deduce that there is a difference
# between the mean of the 2 samples
#
# The 'with rain' sample has a higher mean so we can further expect
# that traffic through the turnstile is higher when there is rain
#
# Q. what is the significance of the size of U value 1924409167.0?
