import pandas as pd
import numpy as np
from pandas import DataFrame

# df=DataFrame([[1,2,3],[4,5,6]])
# df=DataFrame(np.random.randint(0, 100, size=(6,3)))
dic={'name':['zzz','dssdf','fedw'], 'salary':[100,200,300]}
df=DataFrame(dic, index=['a','b','v'])
df['name']#可以取单列，可以用显示行索引
df.iloc[0]
df.iloc[[0,2]]#单行或者多行

#iloc隐式索引取行，loc显式索引取行

df[0:2]#切行
df.iloc[:,0:2]#切列
print(df, df.values, df.columns)