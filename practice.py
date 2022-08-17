import pandas as pd
import numpy as np

data={
    'apples':[3,2,0,1],
    'oranges':[0,3,7,2]
}

purchases=pd.DataFrame(data)
print(purchases)

purchases=pd.DataFrame(data,index=['june','jay','jolly','new'])
print(purchases)

df=pd.read_csv('Price.csv')
print(df)
print(df.iloc[3]) #toprint only one row

s1=pd.Series([-3,-1,2,3,4,10])
print(s1)
s2=pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(s2)

tup=pd.Series((1,2,3))
print(tup)
print(type(tup))

dict1=pd.Series({1:'one',2:'two',3:'three',4:'four'},index=['a','b','c','d','e'])
print(dict1)

s3=pd.Series(data)
print(s3[1:3])
print(s3[[2,3,0]])
# Creating A Data Frame
d=pd.DataFrame({'Name':pd.Series(['Alice','Bulb','Chris']),'Age':pd.Series([21,56,76])})
print(d)
# Adding A New Column In The Data Frame
d['roll no']=pd.Series([1,2,3,4])
print(d)
