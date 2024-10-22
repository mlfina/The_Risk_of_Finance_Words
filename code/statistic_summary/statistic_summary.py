import pandas as pd
import matplotlib.pyplot as plt

#################################
# Figure1 statistic summary 
#################################

## load Earnings calls data 
columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
data_ec = pd.read_csv('data/input/regression_iv.csv').loc[:, columns]
data_ec.dropna(axis=0, inplace=True)
## normalized by day -20
data_ec = data_ec.apply(lambda row: row / row[0], axis=1)
Ave_Norvol_ec = data_ec.mean(axis=0)

## load 10-Ks data 
columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
data_10K = pd.read_csv('data/input/regression_10K_iv.csv').loc[:, columns]
data_10K.dropna(axis=0, inplace=True)
## normalized by day -20
data_10K = data_10K.apply(lambda row: row / row[0], axis=1)
Ave_Norvol_10K = data_10K.mean(axis=0)

## load WSJ data 
columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
data_WSJ = pd.read_csv('data/input/regression_WSJ_iv.csv').loc[:, columns]
data_WSJ.dropna(axis=0, inplace=True)
## normalized by day -20
data_WSJ = data_WSJ.apply(lambda row: row / row[0], axis=1)
Ave_Norvol_WSJ = data_WSJ.mean(axis=0)

## plot scatter
x = [str(i) for i in range(-20, 21)]
plt.figure(figsize=(15,8), dpi=200)
plt.plot(x, Ave_Norvol_ec, color='blue', marker='o', linestyle='-', markersize=5, label='Implied Volatility for Earnings calls')
plt.plot(x, Ave_Norvol_10K, color='indianred', label='Implied Volatility for 10-Ks', marker='x')
plt.plot(x, Ave_Norvol_WSJ, color='green', label='Implied Volatility for WSJ', marker='^', fillstyle='none')
plt.xticks(['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'], [str(i) for i in range(-20, 21, 5)])
plt.xlabel('Days from events')
plt.ylabel('Average normalized Implied Volatility')
plt.legend()
plt.savefig('data/output/statistic_summary/statistic_summary.pdf', bbox_inches='tight')
plt.show()