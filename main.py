"""
Main Function For Polars Descriptive Statistics
"""

# import polars as pl
import matplotlib.pyplot as plt

def polars_desc(data):
    # data = pl.read_csv('Electric_Vehicle_Population_Data.csv')
    return data.describe()

def polars_visual(data):
    # data = pl.read_csv('Electric_Vehicle_Population_Data.csv')
    plt.hist(data["Model Year"])