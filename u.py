# sdl   4
import pandas as pd
data1={'id':[1,2],'name':['aditya','Alice']}
df1=pd.DataFrame(data1)

data2={'id':[3,4],'name':['Wilson','Mark']}
df2=pd.DataFrame(data2)


combined_df=pd.concat([df1,df2])
print(combined_df)

merged_df=pd.merge(df1,df2,on='id')

import pandas as pd

data1 = {'id': [1, 2], 'name': ['aditya', 'Alice']}
data2 = {'id': [3, 4], 'name': ['Wilson', 'Mark']}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


combined_df = pd.concat([df1, df2], axis=1)

print(combined_df)
