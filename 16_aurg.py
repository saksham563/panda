import numpy as np 
import pandas as pd 
df=pd.read_csv('https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv')
print(df)
df.info()
print(df.head(10))#to print only 10 lines


df_new=df.rename(columns={
    'discipline':'subject',
    'sex':'gender'
})
print(df_new)
print(type(df))
print(df_new['salary'].dtype)
print(df_new.axes)
print(df_new.shape)
print(df_new.describe())
df_new=df_new.assign(salary_k=lambda x: x.salary/1000)
print(df_new.head(10))