# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 10:33:41 2025

@author: brownn2
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the dataset
path = r'C:\Users\brownn2\OneDrive - Office for National Statistics\apprenticeshipnb\\'
census_2021 = pd.read_csv(path + 'census2021.csv')

# Show initial info and check for duplicates and nulls
census_2021.duplicated().sum()
census_2021.isnull().sum()

#view duplicated rows and view blank rows 
view_duplicate_rows = census_2021[census_2021.duplicated(keep=False)]
view_blank_rows = census_2021.isnull()

# Drop duplicates and nulls
census_2021 = census_2021.drop_duplicates()
census_2021 = census_2021.dropna()

# Select needed columns
cen_2021 = census_2021[['resident_id_m', 'gltla22cd', 'sex', 'hrp_ethnic_group_tb_6m']]

# Rename columns
cen_2021 = cen_2021.rename(columns={
    'hrp_ethnic_group_tb_6m': 'ethnicity',
    'sex': 'gender',
    'gltla22cd': 'region',
    'resident_id_m': 'resident_id'
})

# replace sex values with names 

gender_dictionary = {
    '1.0' : 'female',
    '2.0' : 'male'}
cen_2021['gender'] = cen_2021['gender'].astype(str).replace(gender_dictionary)

# Replace region Values with names
region_dictionary = {
    'E68000230': 'Lewisham',
    'E68000009': 'Kingston upon Hull',
    'E68000011': 'North East Lincolnshire',
    'E68000014': 'Derby',
    'E68000015': 'Leicester',
    'E68000022': 'Bristol',
    'E68000023': 'North Somerset',
    'E68000024': 'South Gloucestershire',
    'E68000026': 'Torbay',
    'E68000037': 'Windsor and Maidenhead',
    'E68000038': 'Wokingham',
    'E68000039': 'Milton Keynes',
    'E68000040': 'Brighton and Hove',
    'E68000044': 'County Durham',
    'E68000046': 'Cheshire West and Chester',
    'E68000049': 'Wiltshire',
    'E68000057': 'West Northamptonshire',
    'E68000059': 'Fenland',
    'E68000061': 'South Cambridgeshire',
    'E68000063': 'Barrow-In-Furness',
    'E68000072': 'South Hams',
    'E68000073': 'Teignbridge',
    'E68000079': 'Harlow',
    'E68000084': 'Tendring',
    'E68000091': 'Fareham',
    'E68000113': 'Fylde',
    'E68000119': 'Charnwood',
    'E68000122': 'East Lindsey',
    "E68000128": "King's Lynn and West Norfolk",
    'E68000138': 'Oxford',
    'E68000142': 'South Somerset',
    'E68000154': 'Spelthorne',
    'E68000165': 'Bromsgrove',
    'E68000172': 'Bolton',
    'E68000176': 'Rochdale',
    'E68000182': 'Knowsley',
    'E68000183': 'Liverpool',
    'E68000184': 'S.Helens',
    'E68000192': 'North Tyneside',
    'E68000195': 'Birmingham',
    'E68000197': 'Dudley',
    'E68000198': 'Sandwell',
    'E68000200': 'Walsall',
    'E68000205': 'Leeds',
    'E68000210': 'Barnet',
    'E68000214': 'Camden',
    'E68000216': 'Ealing',
    'E68000219': 'Hackney',
    'E68000220': 'Hammersmith and Fulham',
    'E68000221': 'Haringey',
    'E68000223': 'Havering',
    'E68000229': 'Lambeth',
    'E68000237': 'Tower Hamlets'
}
cen_2021['region'] = cen_2021['region'].replace(region_dictionary)

# Replace ethnicity codes with names
ethnicity_dictionary = {
    '-8.0': 'Does Not Apply',
    '1.0': 'Asian, Asian British or Asian Welsh',
    '2.0': 'Black, Caribbean or African',
    '3.0': 'Mixed or Multiple ethnic groups',
    '4.0': 'White',
    '5.0': 'Other Ethnic Group'
}
cen_2021['ethnicity'] = cen_2021['ethnicity'].astype(str).replace(ethnicity_dictionary)

# Group ethnicities per region
ethnicity_counts_by_region = cen_2021.groupby(['region', 'ethnicity']).size().unstack(fill_value=0)

#aggregates by gender and count by region

gender = pd.crosstab(cen_2021['region'], cen_2021['gender'])
agg_stats = cen_2021.groupby('region').agg({'resident_id': 'count'})

# Plot as a stacked bar chart
ethnicity_stacked = ethnicity_counts_by_region.plot(kind='bar', width=0.5, stacked=True, figsize=(15,7))
ethnicity_stacked.set_xlabel('Region')
ethnicity_stacked.set_ylabel('Count')
ethnicity_stacked.set_title('Ethnicity Counts by Region')
ethnicity_stacked.legend(title='Ethnicity', loc='center left', bbox_to_anchor=(1,0.5))
plt.tight_layout()
plt.show()

# Plot as a non-stacked bar chart
ethnicity_bar = ethnicity_counts_by_region.plot(kind='bar', width=0.5, stacked=False, figsize=(15,7))
ethnicity_bar.set_xlabel('Region')
ethnicity_bar.set_ylabel('Count')
ethnicity_bar.set_title('Ethnicity Counts by Region')
ethnicity_bar.legend(title='Ethnicity', loc='center left', bbox_to_anchor=(1,0.5))
plt.tight_layout()
plt.show()

# Plot as a horizontal stacked bar chart
ethnicity_horizontal = ethnicity_counts_by_region.plot(kind='barh', stacked=True, figsize=(10, 12))
ethnicity_horizontal.set_ylabel('Region')
ethnicity_horizontal.set_xlabel('Count')
ethnicity_horizontal.set_title('Ethnicity Counts by Region')
ethnicity_horizontal.legend(title='Ethnicity')
plt.tight_layout()
plt.show()








