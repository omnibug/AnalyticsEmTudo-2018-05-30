# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:10:41 2018

@author: Carlos
"""

#==============================================================================
# This program will prepare the original dataset for later use
#==============================================================================

#==============================================================================
# Original article: https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
# Dataset: https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data
#==============================================================================

#==============================================================================
# Attribute Information:
#
# No: row number
# year: year of data in this row
# month: month of data in this row
# day: day of data in this row
# hour: hour of data in this row
# pm2.5: PM2.5 concentration (ug/m^3)
# DEWP: Dew Point (â„ƒ)
# TEMP: Temperature (â„ƒ)
# PRES: Pressure (hPa)
# cbwd: Combined wind direction
# Iws: Cumulated wind speed (m/s)
# Is: Cumulated hours of snow
# Ir: Cumulated hours of rain
#==============================================================================

# load data
from pandas import read_csv
from datetime import datetime


def parse(x):
    return datetime.strptime(x, '%Y %m %d %H')

#path_name = 'C:/Users/Carlos/Documents/MEGAsync/MIT/AnalyticsEmTudo/'
path_name = '/home/carlos/MEGAsync/MIT/AnalyticsEmTudo/'
file_name = 'PRSA_data_2010.1.1-2014.12.31.csv'

dataset = read_csv(path_name + file_name,  parse_dates=[['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True)
# manually specify column names
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'
# mark all NA values with 0
dataset['pollution'].fillna(0, inplace=True)
# drop the first 24 hours
dataset = dataset[24:]
# summarize first 5 rows
print(dataset.head(5))
print(dataset.describe())
# save to file
dataset.to_csv(path_name + 'pollution.csv')
