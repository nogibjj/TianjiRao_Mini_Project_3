# IDS706 Mini-Project 3

## 


# IDS_706_Data_Engineering_Systems
[![CI](https://github.com/nogibjj/TianjiRao_Mini_Project_3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/TianjiRao_Mini_Project_3/actions/workflows/cicd.yml)


## **Report**
## Week 3 Polars Descriptive Statistics Script 

This repo contains:   
- .devcontainer     
- .github   
- .gitignore    
- Makefile  
- README.md     
- requirements.txt      
- main.py   
- test_main.py
- Eletric_Vechile_Population_Data.csv (Dataset)
- some .sh files


## Purpose
The purpose of this project is using the `Pandas` to show statistics descriptions. The author use a `pd.DataFrame` as a sample data and test its descriptions using the function `desc_df()`. The visualization focus on the bar plot, using `bar_plot()`. Both functions are tested in test_main.py.

## Dataset
The experimental dataset is Eletric Vehicle Population Data that provided by DATA.GOV. Here I downloaded the .csv file and made it the dataset for testing.
The url address is https://catalog.data.gov/dataset/electric-vehicle-population-data. 
I used `pd.read_csv()` to read this dataset and save as a `pd.DataFrame`.

## Functions
There are two main functions in the `main.py`:
- `polars_desc(data)`: this function can take a DataFrame as the input and return a statistical description summary based on the method `pl.DataFrame.describe()`. The default output of `describe()` can return a list of statistics including: `count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, and `max` (fullfill the requirements, which are mean, median, and standard deviation). 

- `polars_visual(data)`: the `bar_plot()` function also take a DataFrame as the input and will plot of histgram of the `Model Year`. This function is mainly based on the `matplotlib.pyplot.hist()`. 


## Preparation
1. Setting up Codespaces
2. Check `make` operations

## Check format and test errors
1. Format `make format`
2. Lint `make lint`


3. Test `make test`



## Reference
https://pola-rs.github.io/polars/py-polars/html/   
https://catalog.data.gov/dataset/electric-vehicle-population-data