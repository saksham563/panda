import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


df=pd.read_csv('https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv')
#print(df.describe)
#plt.hist(df['salary'],bins=8,density=True)
#plt.show()

#df.groupby(['rank'])['salary'].count().plot(kind="bar")
#plt.show()

#sns.set_style("whitegrid")
#ax=sns.barplot(x='rank',y='salary',data=df, estimator=len)
#plt.show()

#sns.violinplot(x = "salary", data=df)
#plt.show()

#sns.jointplot(x='service', y='salary', data=df)
#plt.show()
#sns.regplot(x='service', y='salary', data=df)
#plt.show()
sns.boxplot(x='rank',y='salary', data=df)
plt.show()