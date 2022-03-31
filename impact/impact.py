from operator import index
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
file1 = "datadog_impact.csv"
df = pd.read_csv(file1)
df['time'] = pd.to_datetime(df['time'],format="%b-%y")
# format="%Y/%m/%d")
df = df.set_index('time')
# df.index = pd.to_datetime(df.time,format="%b-%y")
# ym_mean = df.groupby([df.index.year, df.index.month]).mean()
# print(ym_mean)
# ym_agg = df.groupby([df.index.year, df.index.month]).agg({'0':['mean'],'1':['mean'],'2':['mean'],'3':['mean']})
#print('ym_agg:',ym_agg)
path = "datadog_impact.csv"
# print(ym_mean.index)
# ym_mean.to_csv(path,sep=',',index=True,header=True)

df.plot(linewidth=3,figsize =(6.55,6))
# df['Operation and Maintenance'].plot(linewidth=3)
# plt.title('Phase impact of elastic')
plt.xlabel('year')
plt.ylabel('phase impact')
plt.legend(loc='upper left',bbox_to_anchor=(-0.015,1.15),ncol = 2)
# plt.grid()
plt.show()