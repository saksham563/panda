import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flights=pd.read_csv('flights.csv')
print(flights.head())

print(flights[flights.isnull().any(axis=1)].head(5))
print(flights[flights.notnull().any(axis=1)].head(5))
print(flights.info())

flights2=flights.dropna()
print(flights2)
nomiss=flights['dep_delay'].fillna(0)
print(nomiss.isnull().any())
print(flights.value_counts(flights['arr_delay'].notnull()))
print(flights.value_counts(flights['dep_delay'].notnull()))

print(flights.describe())
