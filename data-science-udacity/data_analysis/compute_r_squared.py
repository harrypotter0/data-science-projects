import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    #print data
    #print predictions
    n = len(data)
    prediction_error = sum((data - predictions)**2)
    data_mean = np.mean(data)
    data_var = sum((data - np.repeat(data_mean, n))**2)
    #print prediction_error
    #print data_var
    r_squared = 1.0 - 1.0 * prediction_error / data_var

    return r_squared

