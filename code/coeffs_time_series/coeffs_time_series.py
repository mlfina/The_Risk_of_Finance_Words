import pandas as pd
import matplotlib.pyplot as plt


##########################################
#   coefficients of predicting IV
##########################################
## load data
regression_results_DictD0 = pd.read_csv(r'data/output/predicting_iv/coeffs.csv')

## get coffes
coffes_DictD0 = regression_results_DictD0.pivot(index='Model', columns='Variable', values='Coefficient')
coffes_DictD0 = coffes_DictD0.sort_index()
## get lower confidence inveral
lower_ci_DictD0 = regression_results_DictD0.pivot(index='Model', columns='Variable', values='Lower_CI')
lower_ci_DictD0 = lower_ci_DictD0.sort_index()
## get upper confidence inveral
upper_ci_DictD0 = regression_results_DictD0.pivot(index='Model', columns='Variable', values='Upper_CI')
upper_ci_DictD0 = upper_ci_DictD0.sort_index()

## plot time series of pos dict coeffs
plt.figure(figsize=(15, 8), dpi=200)
x = [str(i) for i in range(1, 21)]
plt.plot(x, coffes_DictD0['vol_pos_uni'], label='Time series coefficients for positive signals', color='indianred')
plt.plot(x, coffes_DictD0['vol_neg_uni'], label='Time series coefficients for negative signals', color='green')
plt.fill_between(x, lower_ci_DictD0['vol_pos_uni'], upper_ci_DictD0['vol_pos_uni'], color='lightgray')
plt.fill_between(x, lower_ci_DictD0['vol_neg_uni'], upper_ci_DictD0['vol_neg_uni'], color='lightgray')
plt.xticks([str(i) for i in range(1, 21)])
plt.legend()
plt.grid(True)
plt.savefig('data/output/coeffs_time_series/coeffs_predicting_iv.pdf', bbox_inches='tight')
plt.show()


###############################################
#  coefficients of predicting RV
###############################################
## load data
regression_results_DictD0 = pd.read_csv(r'data/output/predicting_rv/coeffs.csv')

## get coffes
coffes_DictD0 = regression_results_DictD0.pivot(index='Model', columns='Variable', values='Coefficient')
coffes_DictD0 = coffes_DictD0.sort_index()
## get lower confidence inveral
lower_ci_DictD0 = regression_results_DictD0.pivot(index='Model', columns='Variable', values='Lower_CI')
lower_ci_DictD0 = lower_ci_DictD0.sort_index()
## get upper confidence inveral
upper_ci_DictD0 = regression_results_DictD0.pivot(index='Model', columns='Variable', values='Upper_CI')
upper_ci_DictD0 = upper_ci_DictD0.sort_index()

## plot time series of pos dict coeffs
plt.figure(figsize=(15, 8), dpi=200)
x = [str(i) for i in range(1, 21)]
plt.plot(x, coffes_DictD0['vol_pos_uni'], label='Time series coefficients for positive signals', color='indianred')
plt.plot(x, coffes_DictD0['vol_neg_uni'], label='Time series coefficients for negative signals', color='green')
plt.fill_between(x, lower_ci_DictD0['vol_pos_uni'], upper_ci_DictD0['vol_pos_uni'], color='lightgray')
plt.fill_between(x, lower_ci_DictD0['vol_neg_uni'], upper_ci_DictD0['vol_neg_uni'], color='lightgray')
plt.xticks([str(i) for i in range(1, 21)])
plt.legend()
plt.grid(True)
plt.savefig('data/output/coeffs_time_series/coeffs_predicting_rv.pdf', bbox_inches='tight')
plt.show()

