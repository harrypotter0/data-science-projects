import numpy as np
import pandas
from sklearn.linear_model import SGDRegressor
#import compute_r_squared
import plot_residuals

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def normalize_features(features):
    ''' 
    Returns the means and standard deviations of the given features, along with a normalized feature
    matrix.
    ''' 
    means = np.mean(features, axis=0)
    std_devs = np.std(features, axis=0)
    normalized_features = (features - means) / std_devs
    return means, std_devs, normalized_features

def recover_params(means, std_devs, norm_intercept, norm_params):
    ''' 
    Recovers the weights for a linear model given parameters that were fitted using
    normalized features. Takes the means and standard deviations of the original
    features, along with the intercept and parameters computed using the normalized
    features, and returns the intercept and parameters that correspond to the original
    features.
    '''
    # NOTE(pawelb): my intuition behind the transformation
    # params: norm_params have values such that normalized_features * norm_params = values
    #   now, as we de-normalize features (use the original values), we effectively have:
    #       1. normalized_features * norm_params = values
    #       2.  features * params = values
    #       1. && 2. =>
    #          normalized_features * norm_params = features * params
    #          features / std_devs * norm_params = features * params
    #                   1/std_devs * norm_params = params
    #                                     params = norm_params / std_devs
    #
    #   intercept:
    #        - np.sum(means * norm_params / std_devs) - is basically recovering all the means back
    #        - we take -(norm_intercept - np.sum(means * norm_params / std_devs)) which is transposition (?) of chart
    intercept = norm_intercept - np.sum(means * norm_params / std_devs)
    params = norm_params / std_devs
    return intercept, params

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    """
    
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    clf = SGDRegressor(alpha=0.1, n_iter=20)
    clf.fit(features, values)
    params = clf.get_params()
    intercept = 0

    #print params
    #print len(features[0]), len(clf.coef_)
    #print clf.coef_
    #print clf.intercept_

    return clf.intercept_, clf.coef_

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subset (~50%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this exercise on your own computer, locally.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features or fewer iterations.
    '''
    ################################ MODIFY THIS SECTION #####################################
    # Select features. You should modify this section to try different features!             #
    # We've selected rain, precipi, Hour, meantempi, and UNIT (as a dummy) to start you off. #
    # See this page for more info about dummy variables:                                     #
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html          #
    ##########################################################################################
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    # Values
    values = dataframe['ENTRIESn_hourly']
    
    # Get numpy arrays
    features_array = features.values
    values_array = values.values
    
    means, std_devs, normalized_features_array = normalize_features(features_array)

    # Perform gradient descent
    norm_intercept, norm_params = linear_regression(normalized_features_array, values_array)

    intercept, params = recover_params(means, std_devs, norm_intercept, norm_params)
    
    predictions = intercept + np.dot(features_array, params)
    # The following line would be equivalent:
    # predictions = norm_intercept + np.dot(normalized_features_array, norm_params)
    #r_squared = compute_r_squared.compute_r_squared(values, predictions)
    #print 'r_squared = ', r_squared
    plot_residuals.plot_residuals(dataframe, predictions)
    
    return predictions


turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
p = predictions(turnstile_weather)
print p
