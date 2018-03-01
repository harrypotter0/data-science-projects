import numpy as np
import pandas
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import pylab

def entries_histogram(turnstile_weather):
    '''
    turnstile_weather['column_to_graph'].hist()
    '''
    tw = turnstile_weather
    # sunny_hist = tw[(tw['rain'] == 0.0) & (tw['ENTRIESn_hourly'] <= 6000)]
    # plt.hist(sunny_hist['ENTRIESn_hourly'].tolist(), 20, alpha=0.5, label='sunny')
    # rain_hist = tw[(tw['rain'] == 1.0) & (tw['ENTRIESn_hourly'] <= 6000)]
    # plt.hist(rain_hist['ENTRIESn_hourly'].tolist(), 20, alpha=0.5, label='rainy')
    # plt.legend(loc='upper right')
    # plt.show()


    # alternatively, 2 figures
    sunny_hist = tw[(tw['rain'] == 0.0) & (tw['ENTRIESn_hourly'] <= 6000)]
    sunny_hist.hist(column='ENTRIESn_hourly', stacked=True, bins=20)
    rain_hist = tw[(tw['rain'] == 1.0) & (tw['ENTRIESn_hourly'] <= 6000)]
    rain_hist.hist(column='ENTRIESn_hourly', stacked=True, bins=20)
    return plt

turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
x = entries_histogram(turnstile_weather)
pylab.show()
