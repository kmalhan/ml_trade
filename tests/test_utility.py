import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ml_trade import utility

# TODO: Implement CI tool


def test_symbol_to_path(tmpdir_factory):
    # Create new
    base = tmpdir_factory.mktemp('data')
    path1 = utility.symbol_to_path('SPY', base)
    assert path1 == os.path.join(base, "SPY.csv")
    # Get existing
    path2 = utility.symbol_to_path('SPY', base)
    assert path2 == os.path.join(base, "SPY.csv")


def test_get_data(tmpdir_factory):
    base = tmpdir_factory.mktemp('data')
    dates = pd.date_range('2010-1-1', '2010-12-31')
    symbol = ['SPY']
    df = utility.get_data(symbol, dates, base)
    assert df.head(1).iloc[0, 0] == 113.33
    assert df.tail(1).iloc[0, 0] == 125.75
    assert df.shape == (252, 1)


def test_plot_data():
    plt.ion()
    dates = pd.date_range('2010-1-1', periods=6)
    df = pd.DataFrame(np.random.randn(6, 1), index=dates, columns=list('A'))
    utility.plot_data(df, title="Test Plot")
    ax = plt.gca()
    assert ax.get_title() == "Test Plot"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Price"
