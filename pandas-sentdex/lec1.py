from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
ticker = 'GLD'
data1 = data.DataReader(ticker,'yahoo',dt.datetime(2014,11,11),dt.datetime(2016,11,11))
gld_df = pd.DataFrame(data1)
date_df = pd.to_datetime(list(gld_df.index))
adj_close_df = list(gld_df["Adj Close"])
plt.plot(date_df,adj_close_df)
plt.title("SPDR Gold Shares ")
plt.show()
