import pandas as pd
import numpy as np
data={'apple':[3,2,1,0],'orange':[0,3,7,2], 'grapes':[4,7,5,9]}
fruits=pd.DataFrame(data)
print(fruits)
type(fruits)

print(fruits.iloc[2:3,[2]])

