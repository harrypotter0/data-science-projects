#!/usr/bin/env python3
import urllib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np

def bytesupdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter (b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if(len(split_line) == 6):
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          #%Y = full year 2016
                                                          #%y = partial year 16
                                                          #%m = number month
                                                          #%d = number day
                                                          #%H = hours
                                                          #%M = minutes
                                                          #%S = seconds
                                                          converters={0:bytesupdate2num('%Y%m%d')})
    #For unix time
    '''
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)
    '''
    #plt.plot_date(date,closep,'-', label='Price of '+stock)
    ax1.plot_date(date,closep,'-', label='Price')
    ax1.plot([],[],linewidth=5,label='Loss',color='r',alpha=0.7)  
    ax1.plot([],[],linewidth=5,label='Gain',color='g',alpha=0.7)  
    #ax1.axhline(closep[0],color='k', linewidth=5)
    ax1.fill_between(date, closep, closep[0], where=(closep>closep[0]), facecolor='g', alpha=0.7)
    ax1.fill_between(date, closep, closep[0], where=(closep<closep[0]), facecolor='r', alpha=0.7)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True) #color='g', linestyle='-',linewidth=5
    #ax1.xaxis.label.set_color('b')
    #ax1.yaxis.label.set_color('g')
    #ax1.set_yticks([0,200,400,600,800])
    #ax1.spines['left'].set_color('b')
    #ax1.spines['left'].set_linewidth(5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    #ax1.tick_params(axis='x', colors='#f06215')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock+'\n')
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.20,right=0.94,top=0.90,wspace=0.2, hspace=0)
    plt.show()

graph_data('INFY')
