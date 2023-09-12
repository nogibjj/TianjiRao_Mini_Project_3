"""
Test goes here

"""

from main import polars_desc, polars_visual
import polars as pl

def test_desc():
    df = pl.read_csv('Electric_Vehicle_Population_Data.csv')
    # mean
    assert polars_desc(df)["Electric Range"][2] == 70.49573804284242
    # median
    assert polars_desc(df)["Model Year"][-3] == 2021.0
    # standard deviation
    assert polars_desc(df)["Electric Range"][3] == 97.12873497790751


def test_visual():
    df = pl.read_csv('Electric_Vehicle_Population_Data.csv')
    polars_visual(df)
