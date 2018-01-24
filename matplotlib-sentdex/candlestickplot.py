#!/usr/bin/env python3
import urllib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import datetime as dt
import numpy as np

style.use('ggplot')
#print (plt.style.available)
MA1 = 10
MA2 = 30

def bytesupdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter (b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs - lows

def graph_data(stock):
    fig = plt.figure(facecolor='#f0f0f0')
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax1)
    #plt.xlabel('Date')
    ax2v = ax2.twinx()
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel('MAvgs')

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
    x = 0
    y = len(date)
    ohlc = []
    
    while x < y:
        append_me = [date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]]
        ohlc.append(append_me)
        x+=1

    ma1 = moving_average(closep,MA1) 
    ma2 = moving_average(closep,MA2)
    
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date[-start:], h_l[-start:], '-', label='H-L')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5,prune='lower'))

    candlestick_ohlc(ax2, ohlc[-start:], width=0.4, colorup='#77d879', colordown='#db3f3f')


    '''
    font_dict = {'family':'serif',
                 'color': 'darkred',
                 'size': 15
    }

    ax2.text(date[10],closep[1],'Text example',fontdict=font_dict)
    '''
    bbox_props=dict(boxstyle='larrow', fc='w', ec='k')
    ax2.annotate(closep[-1], (date[-1],closep[-1]),
                 xytext=(date[-1]+5,closep[-1]),
                 bbox=bbox_props
    )
    ax2v.plot([],[],color='#0079a3', alpha=0.3, label='Volume')
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7,prune='upper'))
    ax2v.fill_between(date[-start:],0, volume[-start:],
                      facecolor='#0079a3', alpha=0.3)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 3*volume.max())


    ax3.plot(date[-start:],ma1[-start:], label=(str(MA1)+' MA'), linewidth=1)
    ax3.plot(date[-start:],ma2[-start:], label=(str(MA2)+' MA'), linewidth=1)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], 
               where=(ma1[-start:] < ma2[-start:]),
               facecolor='r', edgecolor='r', alpha=0.5)
    
    ax3.fill_between(date[-start:],ma2[-start:], ma1[-start:], 
               where=(ma1[-start:] > ma2[-start:]),
               facecolor='g', edgecolor='g', alpha=0.5)


    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5,prune='upper'))
    '''
    ax2.annotate('Great!', (date[140], highp[140]),
                 xytext=(0.8,0.9), textcoords='axes fraction',
                 arrowprops=dict(facecolor='grey',color='grey')
    )
    '''
    ax1.legend()
    leg = ax1.legend(loc=9, ncol=2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    ax2v.legend()
    leg = ax2v.legend(loc=9, ncol=2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    ax3.legend()
    leg = ax3.legend(loc=9, ncol=2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.09,bottom=0.20,right=0.90,top=0.90,wspace=0.2, hspace=0)
    plt.show()

    fig.savefig('test.png', facecolor=fig.get_facecolor())

graph_data('INFY')
