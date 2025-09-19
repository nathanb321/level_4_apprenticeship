# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 16:37:54 2025

@author: brownn2
"""

# Import pandas
import pandas as pd

# Define the path to the dataset
path = 'C:\\Users\\brownn2\\OneDrive - Office for National Statistics\\apprenticeshipnb\\'

# Read the CSV file into a DataFrame
census_2021 = pd.read_csv(path + 'census2.csv')

# Display basic information about the DataFrame
census_2021.info()

census_2021.isnull().sum()

census_2021.dropna(subset=['employment_status'], inplace=True)

# Rename the column 'ethnic_group_tb_20b' to 'ethnicity'
census_2021.rename(columns={'hrp_ethnic_group_tb_6m': 'ethnicity'}, inplace=True)

# Check for duplicated rows
census_2021.duplicated().sum()


# View all duplicated rows (if any)
view_duplicate_rows = census_2021[census_2021.duplicated(keep=False)]

# Drop duplicated rows
census_2021 = census_2021.drop_duplicates()



census_2021['ethnicity'] = census_2021['ethnicity'].replace(['4'], ['white'])

#change to int
census_2021['ethnicity'] = census_2021['ethnicity'].astype(object)
census_2021.info()

###groupby ethnicity 
census_2021.groupby(['2022 local authorities: district']).sum().plot()

census_2021.groupby(['2022 Local authorities: district']).sum().plot(kind='bar', y='gltla22cd')

census_2021.info()
