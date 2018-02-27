# NOTE(pawelb): this is only an example how to use statsmodel.api.OLS (Ordinay Least Squared).
# The method is exact && slow, thus I am using gradient_descent for all excercises where 
# # of features is large.
import statsmodels.api as sm

def linear_regression(features, values):
    """
    Performs linear regression given a dataset with an arbitrary number of features.
    'features' is the input data points (or the X's) and 'values' is the output data points
    (or the Y's).
    
    Returns the intercept and the parameters, that is, the optimal values of theta.
    
    This page contains example code that may be helpful:
    http://statsmodels.sourceforge.net/0.5.0/generated/statsmodels.regression.linear_model.OLS.html
    """

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    features = sm.add_constant(features)
    print features
    print values
    model = sm.OLS(values, features)
    results = model.fit()
    intercept = results.params[0]
    params = results.params[1:]
    return intercept, params

import numpy as np
import scipy
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''

    plt.figure()
    (turnstile_weather['''choose the right column here'''] - predictions).hist()
    return pltlo