#!/usr/bin/env python
# coding: utf-8
import pandas as pd

#reading csv
file_path = "Data.csv"
df = pd.read_csv(file_path)

# Display the first few rows
print(df.head())

#display number of missing value in each column
print(df.isnull().sum())

# To drop null values
# df_dropped = df.dropna() can be used
# Fill missing values
df_filled = df.fillna({'Mark1': df['Mark1'].mean(),'Mark2': df['Mark2'].mean(),'Mark3': df['Mark3'].mean(), 'Name': 'Unknown'})
print(df_filled)

# General statistics of updated dataframe
print(df_filled.describe())

#filter dataframe with condition
filtered_df = df_filled[df_filled['Mark1'] > 30]
print(filtered_df)

#calculating mean of total marks
df_filled["Total"]=df_filled["Mark1"]+df_filled["Mark2"]+df_filled["Mark3"]

mean_total = df_filled['Total'].mean()
print("Mean of Total Marks",mean_total)

#save modifiled csv
df_filled.to_csv("modified_Datafile.csv", index=False)
