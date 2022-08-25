import numpy as np
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv')
print(df.describe)
print(df['sex'].head(10))
print(df.sex.head(10))
print(df.service.median())

print(df.salary.mean())
print(df.salary.mode())
print(df.salary.median())
print(df.salary.count())
print(df.salary.unique())
print(df.salary.nunique())
df_rank=df.groupby('rank')
print(df_rank)
print(df_rank.mean())

df_sex=df.groupby('sex')
print(df_sex)
print(df_sex.mean())
df_sub=df[df.salary>100000]
print(df_sub.head())

df_w=df[df.sex=='Female']
print(df_w.head(5))

print(df.salary.where(df.sex=="Female").dropna().head(5))

salary=df['salary']

print(type(salary))
print(salary.head(5))

print(df_sub.loc[10:20,['rank', 'sex', 'salary']])

print(df_sub.iloc[10:20, [0,3,4,5]])

df_sorted=df.sort_values(by='service')
print(df_sorted.head())

df.sort_index(axis=0, ascending= False, inplace=False)
print(df.head())

