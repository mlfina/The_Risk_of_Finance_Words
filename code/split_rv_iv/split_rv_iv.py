import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

###############################
#    trend of implied volatility 
###############################

data = pd.read_csv('data/output/volatility_signals/regression_iv.csv')
data['vol_net'] = data['vol_pos_uni'] - data['vol_neg_uni']
data['Group'] = pd.qcut(data['vol_net'], q=5, labels=['low', '2', '3', '4','high'])

labels=['low', '2', '3', '4','high']
colors = ['royalblue', 'orange', 'green', 'indianred', 'purple']

plt.figure(figsize=(15, 8))
x = [i for i in range(-20, 21)]
columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
for i, lable in enumerate(labels):
    data_temp = data[data['Group'] == lable].loc[:, columns]
    # data_temp = data_temp.apply(lambda row: row / row[0], axis=1)
    data_temp = data_temp.mean(axis=0)
    plt.plot(x, data_temp, label=lable,color=colors[i])

plt.xticks([i for i in range(-20, 21, 2)])
plt.xlabel('Days from events')
plt.ylabel('Average normalized implied Volatility')
plt.grid(True)
plt.legend()
plt.savefig('data/output/split_rv_iv/Group_5_iv.pdf', bbox_inches='tight')
plt.show()

###############################
#    trend of realized volatility 
###############################

data = pd.read_csv('data/output/volatility_signals/regression_ttlvol.csv')
data['vol_net'] = data['vol_pos_uni'] - data['vol_neg_uni']
data['Group'] = pd.qcut(data['vol_net'], q=5, labels=['low', '2', '3', '4','high'])

labels=['low', '2', '3', '4','high']
colors = ['royalblue', 'orange', 'green', 'indianred', 'purple']

plt.figure(figsize=(15, 8))
x = [i for i in range(-20, 21)]
columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
for i, lable in enumerate(labels):
    data_temp = data[data['Group'] == lable].loc[:, columns]
    # data_temp = data_temp.apply(lambda row: row / row[0], axis=1)
    data_temp = data_temp.mean(axis=0)
    plt.plot(x, data_temp, label=lable,color=colors[i])

plt.xticks([i for i in range(-20, 21, 2)])
plt.xlabel('Days from events')
plt.ylabel('Average normalized implied Volatility')
plt.grid(True)
plt.legend()
plt.savefig('data/output/split_rv_iv/Group_5_rv.pdf', bbox_inches='tight')
plt.show()