# -*- coding: utf-8 -*-
import numpy as np
import pandas

from ggplot import *
import matplotlib.pyplot as plt

from random import sample
from datetime import *

"""
In this question, you need to:
1) implement the compute_cost() and gradient_descent() procedures
2) Select features (in the predictions procedure) and make predictions.

"""

alpha = 100.0
num_iterations = 75

def normalize_features(array):
   """
   Normalize the features in the data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    
    This can be the same code as the compute_cost function in the lesson #3 exercises,
    but feel free to implement your own.
    """
    
    # your code here
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)
    
    return cost


def calculate_next_theta(features, values, theta, alpha):
    """
    (rahaugh)
    matrix styly implementaion of the formula to calculate the next iteration of
    theta
    
    recall formula is:
    
    theta_j = theta_j + (   ( alpha / m ) * sum_i_to_m(y_i - h(x_i)x_ij)
    
    where m is the number of samples (num rows in x - in our case features)
    & j goes up to n (num columns in x - in our case features)    
    """
    
    # first h(X)
    hx = np.dot(features, theta)
    
    # next Y - h(X)
    Y_minus_hx = values - hx
    
    # next do the tricky bit
    #Y_minus_hx_times_X = np.dot(np.transpose(features), Y_minus_hx)
    Y_minus_hx_times_X = np.dot(Y_minus_hx,features)    
    
    
    # next multiply by learning rate / m
    lr_divide_m_times_Y_minus_hx_times_X = (alpha / features.size) * Y_minus_hx_times_X
    
    # now finish off
    theta = theta + lr_divide_m_times_Y_minus_hx_times_X
    
    return theta


def calc_r_squared(values, predictions):

    ave_y = np.mean(values)
    
    #calc numerator
    sst = np.square(values - predictions).sum()
    
    #calc denominator
    ssreg = np.square(values - ave_y).sum()
    
    r_squared = 1 - (sst / ssreg)
    
    return r_squared
    #return 9


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """
    
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        # your code here
        cost_history.append(compute_cost(features, values, theta))        
        
        # what are our predictions given theta (h(x))
        predictions = np.dot(features, theta)        
        # use those predictions to calculat R^2
        r_squared = calc_r_squared(values, predictions)
                
        theta = calculate_next_theta(features, values, theta, alpha)        

    return theta, pandas.Series(cost_history)


def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.20 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~15%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this computer on your own computer, locally. 
    
    
    If you'd like to view a plot of your cost history, uncomment the call to 
    plot_cost_history below. The slowdown from plotting is significant, so if you 
    are timing out, the first thing to do is to comment out the plot command again.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a 
    smaller number for num_iterations if that's the case.
    
    If you are using your own algorithm/models, see if you can optimize your code so 
    that it runs faster.
    '''
    
    #dataframe['DAYOFWEEKn'] = [datetime.strptime(d,'%Y-%m-%d').weekday() for d in dataframe['DATEn']]    
    pandas.options.mode.chained_assignment = None

    dataframe['DAYOFWEEKn'] = [1 if datetime.strptime(d,'%Y-%m-%d').weekday() < 5 else 0 for d in dataframe['DATEn']]    

    # Select Features (try different features!)
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi', 'DAYOFWEEKn']]
        
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Add weekday to features using dummy variables
    #sample['WEEKDAYn'] = [datetime.strptime(d,'%Y-%m-%d').weekday() for d in sample['DATEn']]
    #weekdays = [datetime.strptime(d,'%Y-%m-%d').weekday() for d in sample['DATEn']]
    #dummy_weekday = pandas.get_dummmies([datetime.strptime(d,'%Y-%m-%d').weekday() for d in sample['DATEn']], prefix='weekday')
    #dummy_weekday = pandas.get_dummies([datetime.strptime(d,'%Y-%m-%d').weekday() for d in dataframe['DATEn']], prefix='weekday')
    #dummy_weekday = pandas.get_dummies(dataframe['DAYOFWEEKn'], prefix='weekday')
    #features = features.join(dummy_weekday)
    
    # Values
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    # Set values for alpha, number of iterations.
    #alpha = 0.1 # please feel free to change this value
    #num_iterations = 75 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    # 
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed 
    # the 30 second limit on the compute servers.
    
    predictions = np.dot(features_array, theta_gradient_descent)
    return predictions, plot, cost_history
    #return predictions, plot

def plot_cost_history(alpha, cost_history):
   """This function is for viewing the plot of your cost history.
   You can run it by uncommenting this

       plot_cost_history(alpha, cost_history) 

   call in predictions.
   
   If you want to run this locally, you should print the return value
   from this function.
   """
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )

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
preds,plot,cost_history = predictions(sample)

##### output some facts and figures
vals = sample[['ENTRIESn_hourly']]
vals_array = np.array(vals).flatten()

#cost history
print plot

print "alpha: %f" % alpha
print "num_iterations: %d" % num_iterations
print "R^2: %f" % calc_r_squared(vals_array, preds)
print "Min Cost: %f" % min(cost_history)
print "Initial Cost: %f" % cost_history[0]
print "predictions: "
print preds


# just for a laugh histogram observed vs predicted
plt.figure()


plt.title("Histogram of ENTRIESn_hourly")
plt.xlabel("ENTRIESn_hourly")
plt.ylabel("Frequency")

#vals.hist(alpha=1.0, range=(0,6000), bins = 100) # your code here to plot a historgram for hourly entries when it is raining
#pandas.DataFrame(preds).hist(alpha=1.0, range=(0,6000), bins = 100) #turnstile_weather['...'] # your code here to plot a historgram for hourly entries when it is not raining
plt.hist(preds, alpha=1.0, range=(0,6000), bins = 100)
plt.hist(vals_array,alpha=0.8, range=(0,6000), bins = 100)

plt.legend(("Predicted","Observed"))
    
plt.show()
