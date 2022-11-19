from operator import index
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)
    re = np.convolve(interval, window, 'same')
    return re

file1 = "datadog_impact.csv"
df = pd.read_csv(file1)
df['time'] = pd.to_datetime(df['time'])
# format="%Y/%m/%d")
df = df.set_index('time')
# df = df.resample('M').count().to_period('M')
# print(df)
# print(df)
# df.index = pd.to_datetime(df.time,format="%b-%y")
# ym_mean = df.groupby([df.index.year, df.index.month]).mean()
# print(ym_mean)
# ym_agg = df.groupby([df.index.year, df.index.month]).agg({'0':['mean'],'1':['mean'],'2':['mean'],'3':['mean']})
#print('ym_agg:',ym_agg)
path = "datadog_impact.csv"
# print(ym_mean.index)
# ym_mean.to_csv(path,sep=',',index=True,header=True)
df.insert(loc=len(df.columns), column='0', value=moving_average(df['Installation and Configuration'],6))
df.insert(loc=len(df.columns), column='1', value=moving_average(df['Data Collection'],6))
df.insert(loc=len(df.columns), column='2', value=moving_average(df['Data Processing'],6))
df.insert(loc=len(df.columns), column='3', value=moving_average(df['Monitoring and Operations'],6))
figure,axes=plt.subplots(nrows=4,ncols=1,figsize=(8,8))
df[(df.index>'2018-10-01') & (df.index < '2021-09-01')]['Installation and Configuration'].plot(ax=axes[0], title="Installation and Configuration")
df[(df.index>'2018-10-01') & (df.index < '2021-09-01')]['0'].plot(ax=axes[0], title="Installation and Configuration", linewidth=3)
axes[0].set_xlabel(' ')
axes[0].get_xaxis().set_visible(False)
axes[0].set_yticks([0.2,0.4])
df[(df.index>'2018-10-01' )& (df.index < '2021-09-01')]['Data Collection'].plot(ax=axes[1], title="Data Collection")
df[(df.index>'2018-10-01' )& (df.index < '2021-09-01')]['1'].plot(ax=axes[1], title="Data Collection",linewidth=3)
axes[1].set_xlabel(' ')
axes[1].get_xaxis().set_visible(False)
# axes[1].set_yticks([0.25,0.5,0.75])
df[(df.index>'2018-10-01' )& (df.index < '2021-09-01')]['Data Processing'].plot(ax=axes[2], title="Data Processing")
df[(df.index>'2018-10-01' )& (df.index < '2021-09-01')]['2'].plot(ax=axes[2], title="Data Processing",linewidth=3)
axes[2].set_xlabel(' ')
axes[2].get_xaxis().set_visible(False)
# axes[2].set_yticks([0.25,0.5,0.75])
df[(df.index>'2018-10-01' )& (df.index < '2021-09-01')]['Monitoring and Operations'].plot(ax=axes[3], title="Monitoring and Operations")
df[(df.index>'2018-10-01' )& (df.index < '2021-09-01')]['3'].plot(ax=axes[3], title="Monitoring and Operations",linewidth=3)
axes[3].set_xlabel(' ')
# axes[3].get_xaxis().set_visible(False)
# axes[3].set_xticks([])
# axes[3].set_yticks([0.1,0.2,0.3])
font1 = {'weight' : 'bold',
'size': 20
}
# lines  = axes[0].get_legend_handles_labels()
# figure.legend( loc = 'lower center',ncol = 2,prop=font1,bbox_to_anchor=(0.5,-0.025))
plt.show()

plt.savefig("splunk_impact.pdf")


# font1 = {'weight' : 'bold',
# }
# df.plot(linewidth=3,figsize =(6.55,7))
# # df['Operation and Maintenance'].plot(linewidth=3)
# # plt.title('Phase impact of elastic')
# plt.yticks( size=15,weight='bold')
# plt.xticks( size=15,weight='bold')
# plt.xlabel('year',fontsize = 15,fontweight='bold')
# plt.ylabel('phase impact',fontsize = 15,fontweight='bold')
# plt.legend(loc='upper left',bbox_to_anchor=(-0.015,1.1),ncol = 2,prop=font1)
# # plt.grid()
# plt.show()






