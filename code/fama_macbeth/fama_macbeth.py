import pandas as pd
import numpy as np
import scipy.stats
import os
import statsmodels.api as sm
import matplotlib.pyplot as plt

def NWttest_1var(Y, L):

    Y = np.array(Y)
    mean = Y.mean()
    e = Y - mean
    T = len(Y)

    S = 0
    for l in range(1, L + 1):
        w_l = 1 - l / (L + 1)
        for t in range(l + 1, T + 1):
            S += w_l * e[t - 1] * e[t - 1 - l] * 2
    S = S + (e * e).sum()
    S = S / (T - 1)

    se = np.sqrt(S / T)
    tstat = mean / se
    pval = scipy.stats.t.sf(np.abs(tstat), T - 1) * 2

    return mean, se, tstat, pval

def getOLS(group, x_var, y_var):
    
    X = group[x_var]
    y = group[y_var]
    
    X = X.assign(const=1)
    res = sm.OLS(y, X).fit()
    
    return res.params

#################################
#  fama_macbeth with whole sample 
#################################
meta = pd.read_csv(r'data/output/volatility_signals/regression_standardized_iv.csv')
# whole sample
meta = meta[meta['quarter'] <= '2020-09']
df_temp = meta[['D00', 'vol_pos_uni', 'vol_neg_uni', 'me', 'bm', 'turn', 'sue', 'nasdaq', 'rvar_capm','quarter']]
df_temp = df_temp.dropna()
columns = ['me', 'bm', 'turn', 'rvar_capm']
df_temp[columns] = np.log(df_temp[columns])

res = df_temp.groupby(['quarter']).apply(getOLS, ['vol_pos_uni', 'vol_neg_uni', 'me', 
                                                  'bm', 'turn', 'sue', 'rvar_capm', 'nasdaq'], 'D00')
L = int(round(4 * (len(res) / 100)** (2 / 9), 0))
print(L)

nw = pd.DataFrame(columns=['mean', 'se', 'tstat', 'pval'])
for index, columns in enumerate(res.columns):
    mean, se, tstat, pval  = NWttest_1var(res[columns], L)
    nw.loc[index] = [mean, se, tstat, pval]
nw.loc[:, 'variables'] = res.columns
group_sizes = df_temp.groupby('quarter').size()
res['numbers'] = group_sizes
res.to_csv(r'data/output/fama_macbeth/res.csv')
nw.to_csv(r'data/output/fama_macbeth/nw.csv', index=False)

confidence_level = 0.95
sample_size = len(res)
t_critical = scipy.stats.t.ppf((1 + confidence_level) / 2, sample_size - 1)

res['lower_bound_pos'] = res['vol_pos_uni'] - t_critical * nw['se'][0]
res['upper_bound_pos'] = res['vol_pos_uni'] + t_critical * nw['se'][0]

res['lower_bound_neg'] = res['vol_neg_uni'] - t_critical * nw['se'][1]
res['upper_bound_neg'] = res['vol_neg_uni'] + t_critical * nw['se'][1]

plt.figure(figsize=(15, 8))
plt.plot(res.index, res['vol_pos_uni'], label='positive signals',  color='indianred')
plt.plot(res.index, res['vol_neg_uni'], label='negative signals', color='green')
plt.fill_between(res.index, res['lower_bound_pos'], res['upper_bound_pos'], color='lightgray')
plt.fill_between(res.index, res['lower_bound_neg'], res['upper_bound_neg'], color='lightgray')

plt.xticks(res.index[::2],  rotation=45)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.legend()
plt.grid()
plt.savefig('data/output/fama_macbeth/FM.pdf', bbox_inches='tight')
plt.show()