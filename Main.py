# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 09:26:00 2022

@author: shado
"""

import pandas as pd
from os.path import exists
filepath="Raw Data/Real Data/CONTENT_INTERACTION/ViewingActivity.csv"
selectedpath="Raw Data/Sample Netflix Data.csv"
selectedShow="Jessica Jones"
if exists(filepath):
    selectedpath=filepath

print(selectedpath)
df = pd.read_csv(selectedpath)

df.shape
df.head(1)
df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

#print(df.head(1))

df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
#print(df.dtypes)
df=df.set_index('Start Time')
df.index=df.index.tz_convert('Europe/London')

df=df.reset_index()

#print(df.head(1))

df['Duration'] = pd.to_timedelta(df['Duration'])

programName = df[df['Title'].str.contains(selectedShow, regex=False)]
programName = programName[(programName['Duration'] > '0 days 00:01:00')]
print(programName['Duration'].sum())