import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import os


def symbol_to_path(symbol, base_dir="../data/"):
    """
    Return CSV path to specified symbol
    :type symbol: char
    :type base_dir: String
    :rtype: String
    """
    if not os.path.exists(os.path.join(base_dir, "{}.csv".format(str(symbol)))):
        start = dt.datetime(2010, 1, 1)
        end = dt.datetime(2016, 12, 31)
        df = web.DataReader(symbol, 'google', start, end)
        df.to_csv(os.path.join(base_dir, "{}.csv".format(str(symbol))))
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates, base_dir="../data/"):
    """
    Read stock data (close) for given symbols for given period of time
    :type symbols: char array
    :type dates: DatetimeIndex
    :type base_dir: String
    :rtype: DataFrame
    """
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        temp_df = pd.read_csv(symbol_to_path(symbol, base_dir), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Close'],
                              na_values=['nan'])
        temp_df = temp_df.rename(columns={'Close': symbol})
        df = df.join(temp_df, how='inner')
    return df


def plot_data(df, title="Stock Price"):
    """
    Plot given DataFrame
    :type df: DataFrame
    :type title: String
    """
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
