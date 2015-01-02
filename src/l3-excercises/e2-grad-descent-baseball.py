# -*- coding: utf-8 -*-
import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
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
    
    I think if you shut your eyes and hope you can calculate the tricky bit
    matrix styly by:
    
    X_transpose . ( Y - h(X) )
    
    """
    
    # first h(X)
    hx = numpy.dot(features, theta)
    
    # next Y - h(X)
    Y_minus_hx = values - hx
    
    # next do the tricky bit
    Y_minus_hx_times_X = numpy.dot(numpy.transpose(features), Y_minus_hx)
    
    # next multiply by learning rate / m
    lr_divide_m_times_Y_minus_hx_times_X = (alpha / features.size) * Y_minus_hx_times_X
    
    # now finish off
    theta = theta + lr_divide_m_times_Y_minus_hx_times_X
    
    return theta

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """
    
    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    

    
    cost_history = []

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    for i in range(num_iterations):
        cost_history.append(compute_cost(features, values, theta))        
        theta = calculate_next_theta(features, values, theta, alpha)
        
    return theta, pandas.Series(cost_history) # leave this line for the grader


#(rahaugh) no idea how to run this as I don't know the datasets!!!!!