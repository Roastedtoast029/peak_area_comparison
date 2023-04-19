import pandas as pd
import matplotlib.pyplot as plt

test_data = pd.read_csv("test_data.csv",index_col=0)

df = test_data.apply(lambda x:x/x.sum()*100,axis=1)[::-1]

print(df)
fig, ax = plt.subplots()
ax.barh(df.iloc[:,0].index, df.iloc[:,0],label=df.columns[0])
stack=df.iloc[:,0]
for column in range(1,len(df)):
    ax.barh(df.index, df.iloc[:,column],left=stack, label=df.columns[column])
    stack += df.iloc[:,column]

plt.legend()
plt.show()