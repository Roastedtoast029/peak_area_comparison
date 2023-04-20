import pandas as pd
import matplotlib.pyplot as plt

test_data = pd.read_csv("test_data.csv",index_col=0)

df = test_data.apply(lambda x:x/x.sum()*100,axis=1)[::-1]

#カラーマップを利用
color = plt.get_cmap("Blues")

fig, ax = plt.subplots()
ax.barh(df.iloc[:,0].index, df.iloc[:,0],label=df.columns[0],color=color(255//len(df)))
stack=df.iloc[:,0]
for column in range(1,len(df)):
    ax.barh(df.index, df.iloc[:,column],left=stack, label=df.columns[column],color=color(255//len(df)*(column+1)))
    stack += df.iloc[:,column]

#もろもろの設定
fig.legend(bbox_to_anchor=(1.1, 0.9),loc="upper right")
ax.set_xlim(0,100)
ax.set_xlabel("Peak Area Percentage (%)")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()