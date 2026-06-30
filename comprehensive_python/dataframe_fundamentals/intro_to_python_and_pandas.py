# Pandas is a library to work with structured data like csv, excel, json, sql, etc 
# pandas dataframe is similar to excel sheets

# import pandas
import pandas as pd

# load data as
df = pd.read_csv(data.csv)
df = pd.read_excel(data.xls)
df = pd.read_json(data.json)
df = pd.read_sql("SELECT * FROM employees", connection)

# selecting columns
# to select columns of a dataframe, we use dataframe['_col_'] for single column and dataframe[['_col1_', '_col2_']]

# Q1. Select first name and last name from `techcorp_workforce`.
techcorp_workforce[['first_name', 'last_name']]

# Q2. Display all columns and rows from `techcorp_workforce`.
techcorp_workforce

# rather than viewing the entire dataset at once, we can use .head() and .tail() to see the top and bottom of the dataset
techcorp_workforce.head()    # default 5 rows
techcorp_workforce.head(10)  # can specify the number of rows to be displayed
techcorp_workforce.tail() 

# inspecting a dataframe

# How many rows and columns?
techcorp_workforce.shape   # like (50,8) which means 50 rows 8 cols, returns a tuple

# What are the column names?
techcorp_workforce.columns # give the column names

# What data type is each column?
techcorp_workforce.dtypes  # give the column names and their data types

# Get a full summary: columns, types, non-null counts
techcorp_workforce.info()  # gives column names, types, and how many non-null values each column has.

# get a quick statistical summary of numerical columns and their data
techcorp_workforce.describe()   # gives the mean, count, min, p25, p50, p75, max, std of numerical columns

# Q3. Select the facility name, score, and grade from `los_angeles_restaurant_health_inspections`.
los_angeles_restaurant_health_inspections[['facility_name', 'score', 'grade']]

# Q4. Find out how many rows and columns `los_angeles_restaurant_health_inspections` has.
los_angeles_restaurant_health_inspections.shape

