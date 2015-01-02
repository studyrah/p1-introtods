import numpy as np
import pandas
#import scipy
import statsmodels.api as sm

from datetime import *
from ggplot import *
from random import sample


"""
In this optional exercise, you should complete the function called 
predictions(turnstile_weather). This function takes in our pandas 
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.  

In exercise 3.5 we used Gradient Descent in order to compute the coefficients
theta used for the ridership prediction. Here you should attempt to implement 
another way of computing the coeffcients theta. You may also try using a reference implementation such as: 
http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.OLS.html

One of the advantages of the statsmodels implementation is that it gives you
easy access to the values of the coefficients theta. This can help you infer relationships 
between variables in the dataset.

You may also experiment with polynomial terms as part of the input variables.  

The following links might be useful: 
http://en.wikipedia.org/wiki/Ordinary_least_squares
http://en.wikipedia.org/w/index.php?title=Linear_least_squares_(mathematics)
http://en.wikipedia.org/wiki/Polynomial_regression

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent computed in Exercise 3.5?

You can look at the information contained in the turnstile_weather dataframe below:
https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~10%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting 
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""

def predictions(weather_turnstile):

    pandas.options.mode.chained_assignment = None
    weather_turnstile['DAYOFWEEKn'] = [1 if datetime.strptime(d,'%Y-%m-%d').weekday() < 5 else 0 for d in weather_turnstile['DATEn']]    

    # Select Features (try different features!)
    features = weather_turnstile[['rain', 'precipi', 'Hour', 'meantempi', 'DAYOFWEEKn']]
    #features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
        
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    features = features.join(dummy_units)
   
    # Values
    values = weather_turnstile[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)
    
    
    # try a higher order poly
    featuressq = np.power(features,2)
    featurescu = np.power(features,3)
    features = features + featuressq + featurescu
      
    
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    model = sm.OLS(values_array, features_array)

    results = model.fit()

    #try with regularisation
    #results = model.fit_regularized()

    predictions = results.predict()
    
    print results.rsquared    
    
    return predictions




def normalize_features(array):
   """
   Normalize the features in the data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma


"""    
###############################################################################
#for the submission version
###############################################################################
turnstile_weather = pandas.read_csv('./turnstile_data_master_with_weather.csv')
print predictions(turnstile_weather)
"""

###############################################################################
# for my local experimentation
###############################################################################

turnstile_weather = pandas.read_csv('./turnstile_data_master_with_weather.csv')


# just take a proportion of rows
percent = 15

fulllength = len(turnstile_weather)
samplesize = (fulllength / 100) * percent

# create random index
rindex =  np.array(sample(xrange(len(turnstile_weather)), samplesize))

# get samplesize random rows from df
sample = turnstile_weather.ix[rindex]

# do the grad descent
preds = predictions(sample)

print preds