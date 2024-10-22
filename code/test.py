import pandas as pd
import os 
import numpy as np
import matplotlib.pyplot as plt


# list_dir = os.listdir(r'data/input/crsp_d')
# print(list_dir)

# data = pd.DataFrame(columns=['bidlo', 'askhi', 'openprc'])
# print(data)

# for dir in list_dir[:2]:
#     df_temp = pd.read_csv(r'data/input/crsp_d/{}'.format(dir))
#     df = pd.DataFrame()
#     df['bidlo'] = df_temp['bidlo'] / abs(df_temp['prc'])
#     df['askhi'] = df_temp['askhi'] / abs(df_temp['prc'])
#     df['openprc'] = df_temp['openprc'] / abs(df_temp['prc'])
#     print(df)
#     data = pd.concat([data, df])
# data.to_csv(r'data/input/histgram.csv', index=False)


# data = pd.read_csv(r'data/input/histgram.csv')
# for col in data.columns:

#     plt.hist(data[col].dropna(), bins=100, density=True, alpha=0.6, color='b')
#     plt.xlabel(col)
#     plt.ylabel('freq')
#     plt.title('histgram')
#     plt.show()


# data = pd.read_csv(r'data/input/histgram.csv')
# for col in data.columns:
#     print(col)
#     data_temp = data[col].dropna()
#     percentiles = [0.01, 0.1, 1, 99, 99.9, 99.99] 
#     percentile_values = np.percentile(data_temp, percentiles)
#     count_values = [np.sum(data_temp >= p) for p in percentile_values]

#     for percentile, value, count in zip(percentiles, percentile_values, count_values):
#         print(f"{percentile}th percentile: {value:.2f}")
#         print(f"{percentile}th percentile: {count} values")

# list_dir = os.listdir(r'data/input/crsp_d_WSJ')
# for dir in list_dir:
#     print(dir)
#     data = pd.read_csv(r'data/input/crsp_d_WSJ/{}'.format(dir))
#     data['bidlo_adj'] = np.where(data['bidlo'] / abs(data['prc']) < 0.53, np.nan, data['bidlo'])
#     data['askhi_adj'] = np.where(data['askhi'] / abs(data['prc']) > 1.61, np.nan, data['askhi'])
#     data.to_csv(r'data/input/crsp_d_WSJ/{}'.format(dir), index=False)


# reg_data = pd.read_csv(r'data/input/regression_meta_gkvol.csv', usecols=['permno', 'gvkey', 'datadate', 'fyearq', 'callDate', 'date', 'mon', \
#                       'me', 'bm', 'turn', 'sue', 'exchcd', 'sic', 'nasdaq', 'ffi49', 'quarter'])
# reg_data.to_csv(r'data/input/regression_v2.csv', index=False)

# list_dir = os.listdir(r'data/input/crsp_d')
# for dir in list_dir:
#     data = pd.read_csv(r'data/input/crsp_d/{}'.format(dir))
#     if 'AAPL' in data['ticker'].unique():
#         print(dir)

# meta = pd.read_csv(r'data/input/regression_meta_ivol.csv')
# meta = meta[meta['permno'] == 14593]
# print(meta)
# meta = meta[(meta['date'] >= '2008-01-01') & (meta['date'] <= '2010-12-31')]
# print(meta)

# data = pd.read_csv(r'data/input/crsp_d/crsp_d_14593.csv')
# data = data[(data['date'] >= '2008-01-01') & (data['date'] <= '2010-12-31')]


# ivolc = data[['date', 'ivolc']].dropna(axis=0)
# print(ivolc)

# plt.figure(figsize=(15, 8))
# plt.plot(ivolc['date'], ivolc['ivolc'])
# special_point_x = meta['date'].to_list()
# print(special_point_x)
# print(ivolc[ivolc['date'].isin(special_point_x)]['ivolc'])
# plt.scatter(special_point_x, ivolc[ivolc['date'].isin(special_point_x)]['ivolc'], color='red', s = 30)
# plt.xticks(ivolc['date'][::50], rotation=45)
# plt.show()

# meta = pd.read_csv(r'data/input/regression_meta_ivol.csv')
# meta['ivolc_delata_D0'] = meta['ivolC_D0'] - meta['ivolC_Dbefore1']
# meta['ivolc_delata_D1'] = meta['ivolC_D1'] - meta['ivolC_D0']
# meta.to_csv(r'data/input/regression_meta_ivol.csv', index=False)


# iv = pd.read_csv(r'data/input/regression_iv_v2.csv')
# columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-21, 21)]
# data = iv.loc[:, columns]
# iv_delta = pd.DataFrame()

# for i in range(1, data.shape[1]):
#     iv_delta[i - 1] = data.iloc[:, i] - data.iloc[:, i - 1]

# columns = ["delta_D0" + str(i) if 0 <= i < 10 else "delta_D" + str(i) if i >= 10 else "delta_Dbefore" + str(abs(i)) for i in range(-20, 21)]
# iv_delta.columns = columns
# reg = pd.read_csv(r'data/input/regression.csv')
# iv_delta = pd.concat([reg, iv_delta], axis=1)
# iv_delta.to_csv(r'data/input/regression_iv_delta.csv', index=False)



# iv_delta = pd.read_csv(r'data/input/regression_iv_delta.csv')
# for i in [5, 10, 20]:
#     columns = ["delta_D0" + str(i) if 0 <= i < 10 else "delta_D" + str(i) if i >= 10 else "delta_Dbefore" + str(abs(i)) for i in range(-i, 0)]
#     new_columns = ['delta_Dbefore{}ToDbefore1'.format(str(i))]
#     temp = iv_delta.loc[:, columns].mean(axis=1)
#     iv_delta = pd.concat([iv_delta, temp], axis=1)
#     iv_delta.rename(columns={0:new_columns[0]}, inplace=True)
# iv_delta.to_csv(r'data/input/regression_iv_delta.csv', index=False)


# iv_delta = pd.read_csv(r'data/input/regression_iv_delta.csv')
# for i in [5, 10, 20]:
#     columns = ["delta_D0" + str(i) if 0 <= i < 10 else "delta_D" + str(i) if i >= 10 else "delta_Dbefore" + str(abs(i)) for i in range(2, i + 1)]
#     new_columns = ['delta_D02ToD0'+ str(i) if 0 <= i < 10 else "delta_D02ToD" + str(i)]
#     temp = iv_delta.loc[:, columns].mean(axis=1)
#     iv_delta = pd.concat([iv_delta, temp], axis=1)
#     iv_delta.rename(columns={0:new_columns[0]}, inplace=True)
# iv_delta.to_csv(r'data/input/regression_iv_delta.csv', index=False)

# iv_delta = pd.read_csv(r'data/output/volatility_signals/regression_rv.csv')
# iv_delta['iv_net_uni_delta_D0'] = iv_delta['iv_pos_uni_delta_D0'] - iv_delta['iv_neg_uni_delta_D0']
# iv_delta['iv_net_uni_delta_D1'] = iv_delta['iv_pos_uni_delta_D1'] - iv_delta['iv_neg_uni_delta_D1']
# iv_delta['rv_net_uni_delta_D0'] = iv_delta['rv_pos_uni_delta_D0'] - iv_delta['rv_neg_uni_delta_D0']
# iv_delta['rv_net_uni_delta_D1'] = iv_delta['rv_pos_uni_delta_D1'] - iv_delta['rv_neg_uni_delta_D1']
# iv_delta.to_csv(r'data/output/volatility_signals/regression_rv.csv', index=False)

# rv = pd.read_csv("data/input/cmqpjeeootfag390.csv")
# rv.columns = rv.columns.str.lower()
# rv['date'] = rv['date'].apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
# meta_rv = pd.read_csv("data/input/regression_rv_30.csv")
# rv.rename(columns={'':''}, inplace=True)
# meta_rv = pd.merge(meta_rv, rv[['permno', 'date', 'b_mkt', 'ivol', 'tvol']], on=['permno', 'date'], how='left')
# columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-21, 22)]
# for i in columns:
#     meta_rv[i] = meta_rv[i] * np.sqrt(252)
# meta_rv.to_csv("data/input/regression_rv_30_v2.csv", index=False)

# meta_rv = pd.read_csv("data/input/regression_rv_30_v2.csv")
# meta_iv = pd.read_csv("data/input/regression_iv_v2.csv")
# meta_rv.describe().to_csv("data/output/regression_rv_describe.csv")
# meta_iv.describe().to_csv("data/output/regression_iv_describe.csv")

# meta_rv = pd.read_csv("data/input/cmqpjeeootfag390.csv")
# meta_rv['tvol'] = meta_rv['tvol'].str.rstrip('%').astype('float64') / 100.0
# meta_rv['ivol'] = meta_rv['ivol'].str.rstrip('%').astype('float64') / 100.0
# print(meta_rv['ivol'].dtype)
# print(meta_rv['tvol'].dtype)
# meta_rv['ivol'] = meta_rv['ivol'] * np.sqrt(252)
# meta_rv['tvol'] = meta_rv['tvol'] * np.sqrt(252)
# meta_rv.columns = meta_rv.columns.str.lower()
# meta_rv['date'] = meta_rv['date'].apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
# meta_rv.to_csv("data/input/cmqpjeeootfag390_v.csv", index=False)

# crsp_d = pd.read_csv(r'data/input/crsp_d_20230903.csv')
# crsp_d.columns = crsp_d.columns.str.lower()
# meta_rv = pd.read_csv("data/input/cmqpjeeootfag390_v.csv")
# crsp_d = pd.merge(crsp_d, meta_rv[['permno', 'date', 'b_mkt']], on=['permno', 'date'], how='left')
# crsp_d.to_csv(r'data/input/crsp_d_20230903.csv', index=False)


# ## load data
# data_crsp = pd.read_csv(r'data/input/crsp_d_20230903.csv')
# ivol = pd.read_csv(r'data/input/iv_30d.csv')
# ivol.columns = ivol.columns.str.lower()

# ## merge iv calculated using call option
# ivolC = ivol[ivol['cp_flag'] == 'C']
# ivolC['date'] = ivolC['date'].apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
# data_crsp = pd.merge(data_crsp, ivolC[['permno', 'date', 'impl_volatility']], on=['permno', 'date'], how='left')
# data_crsp.rename(columns={'impl_volatility':'ivolc'}, inplace=True)

# ## merge iv calculated using put option
# ivolP = ivol[ivol['cp_flag'] == 'P']
# ivolP['date'] = ivolP['date'].apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
# data_crsp = pd.merge(data_crsp, ivolP[['permno', 'date', 'impl_volatility']], on=['permno', 'date'], how='left')
# data_crsp.rename(columns={'impl_volatility':'ivolp'}, inplace=True)

# data_crsp.to_csv(r'data/input/crsp_d_20230903.csv', index=False)

# regression = pd.read_csv(r'data/input/regression.csv')
# meta_mktvol = pd.read_csv(r'data/input/regression_mktvol.csv')
# meta_beta = pd.read_csv(r'data/input/regression_bmkt.csv')
# meta_rv = pd.read_csv(r'data/input/regression_rv_30.csv')

# beta = meta_beta[["Dbefore20", "Dbefore19", "Dbefore18", "Dbefore17",
#         "Dbefore16", "Dbefore15", "Dbefore14", "Dbefore13",
#         "Dbefore12", "Dbefore11", "Dbefore10", "Dbefore9", 
#         "Dbefore8", "Dbefore7", "Dbefore6", "Dbefore5",
#         "Dbefore4", "Dbefore3", "Dbefore2", "Dbefore1", "D00",
#         'D01', 'D02', 'D03', 'D04', 
#         'D05', 'D06', 'D07', 'D08', 
#         'D09', 'D10', 'D11', 'D12', 
#         'D13', 'D14', 'D15', 'D16', 
#         'D17', 'D18', 'D19', 'D20']]

# mktvol =  meta_mktvol[["Dbefore20", "Dbefore19", "Dbefore18", "Dbefore17",
#         "Dbefore16", "Dbefore15", "Dbefore14", "Dbefore13",
#         "Dbefore12", "Dbefore11", "Dbefore10", "Dbefore9", 
#         "Dbefore8", "Dbefore7", "Dbefore6", "Dbefore5",
#         "Dbefore4", "Dbefore3", "Dbefore2", "Dbefore1", "D00",
#         'D01', 'D02', 'D03', 'D04', 
#         'D05', 'D06', 'D07', 'D08', 
#         'D09', 'D10', 'D11', 'D12', 
#         'D13', 'D14', 'D15', 'D16', 
#         'D17', 'D18', 'D19', 'D20']]

# rv = meta_rv[["Dbefore20", "Dbefore19", "Dbefore18", "Dbefore17",
#         "Dbefore16", "Dbefore15", "Dbefore14", "Dbefore13",
#         "Dbefore12", "Dbefore11", "Dbefore10", "Dbefore9", 
#         "Dbefore8", "Dbefore7", "Dbefore6", "Dbefore5",
#         "Dbefore4", "Dbefore3", "Dbefore2", "Dbefore1", "D00",
#         'D01', 'D02', 'D03', 'D04', 
#         'D05', 'D06', 'D07', 'D08', 
#         'D09', 'D10', 'D11', 'D12', 
#         'D13', 'D14', 'D15', 'D16', 
#         'D17', 'D18', 'D19', 'D20']]

# meta_sysvol = beta * beta * (mktvol ** 2)

# meta_sysvol_1 = meta_sysvol ** 0.5
# print(meta_sysvol_1.describe())

# meta_idvol = (rv ** 2) - meta_sysvol
# meta_idvol_1 = meta_idvol ** 0.5
# print(meta_idvol_1.describe())
# regression_sysvol = pd.concat([regression, meta_sysvol_1], axis=1)
# regression_sysvol.to_csv(r'data/input/regression_sysvol.csv', index=False)
# print(regression_sysvol.describe())
# regression_idvol = pd.concat([regression, meta_idvol_1], axis=1)
# regression_idvol.to_csv(r'data/input/regression_idvol.csv', index=False)
# print(regression_idvol.describe())

# meta_rv = pd.read_csv(r'data/input/regression_rv.csv')
# meta_iv = pd.read_csv(r'data/input/regression_iv.csv')

# meta_rv = meta_rv.drop(columns=['delta_Dbefore2', 'delta_Dbefore1', 'delta_D0', 'delta_D1', 'delta_D2'])
# meta_iv = meta_iv.drop(columns=['delta_Dbefore2', 'delta_Dbefore1', 'delta_D0', 'delta_D1', 'delta_D2'])

# ## cal iv delta
# meta_iv['delta_Dbefore2'] = meta_iv['Dbefore2'] - meta_iv['Dbefore3']
# meta_iv['delta_Dbefore1'] = meta_iv['Dbefore1'] - meta_iv['Dbefore2']
# meta_iv['delta_D0'] = meta_iv['D00'] - meta_iv['Dbefore1']
# meta_iv['delta_D1'] = meta_iv['D01'] - meta_iv['D00']
# meta_iv['delta_D2'] = meta_iv['D02'] - meta_iv['D01']

# ## cal rv delta 
# meta_rv['delta_Dbefore2'] = meta_rv['Dbefore2'] - meta_rv['Dbefore3']
# meta_rv['delta_Dbefore1'] = meta_rv['Dbefore1'] - meta_rv['Dbefore2']
# meta_rv['delta_D0'] = meta_rv['D00'] - meta_rv['Dbefore1']
# meta_rv['delta_D1'] = meta_rv['D01'] - meta_rv['D00']
# meta_rv['delta_D2'] = meta_rv['D02'] - meta_rv['D01']

# ## save data 
# meta_rv.to_csv(r'data/input/regression_rv.csv', index=False)
# meta_iv.to_csv(r'data/input/regression_iv.csv', index=False)

# meta_ret = pd.read_csv(r'data/output/volatility_signals/regression_ret.csv')
# meta_exret = pd.read_csv(r'data/output/volatility_signals/regression_exret.csv')
# meta_iv = pd.read_csv(r'data/output/volatility_signals/regression_iv.csv')
# meta_rv = pd.read_csv(r'data/output/volatility_signals/regression_rv.csv')

# meta_strategy = meta_rv[["permno", "gvkey", "datadate", "fyearq", "callDate", "date", "mon", "me",
#                     "bm", "turn", "sue", "exchcd", "sic", "nasdaq", "ffi49", "quarter"]]

# meta_strategy['ret_D0'] = meta_ret['D00']
# meta_strategy['exret_D0'] = meta_exret['D00']
# meta_strategy['iv_D0'] = meta_iv['D00']
# meta_strategy['rv_D0'] = meta_rv['D00']

# meta_strategy = pd.concat([meta_strategy, meta_iv[["ret_pos_uni", "ret_neg_uni", "LM_pos", "LM_neg",
#                                         "iv_pos_uni_delta_D0", "iv_neg_uni_delta_D0", "iv_pos_uni_delta_D1",
#                                         "iv_neg_uni_delta_D1", "rv_pos_uni_delta_D0", "rv_neg_uni_delta_D0",
#                                         "rv_pos_uni_delta_D1", "rv_neg_uni_delta_D1"]]], axis=1)
# meta_strategy.to_csv(r'data/output/trading_strategy/meta_strategy.csv', index=False)

# data = pd.read_csv(r'data/input/regression_rvd.csv')
# columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
# for i in columns:
#     data[i] = data[i] * np.sqrt(252)

# data.to_csv(r'data/input/regression_rvd_v2.csv', index=False)

# data = pd.read_csv(r'data/input/regression_iv.csv', usecols=['permno', 'gvkey', 'datadate', 'fyearq', 'callDate', 'date', 'mon',
#        'me', 'bm', 'turn', 'sue', 'exchcd', 'sic', 'nasdaq', 'ffi49',
#        'quarter'])
# data.to_csv(r'data/input/regression.csv', index=False)


data = pd.read_csv(r'data/output/volatility_signals/regression_ret.csv')
meta1 = pd.read_csv(r'data/output/volatility_signals/regression_iv.csv')
meta2 = pd.read_csv(r'data/output/volatility_signals/regression_rv.csv')
meta3 = pd.read_csv(r'data/output/volatility_signals/regression_iv_div_delta.csv')

meta1['quarter'] = data['quarter']
meta2['quarter'] = data['quarter']
meta3['quarter'] = data['quarter']

meta1.to_csv(r'data/output/volatility_signals/regression_iv.csv', index=False)
meta2.to_csv(r'data/output/volatility_signals/regression_rv.csv', index=False)
meta3.to_csv(r'data/output/volatility_signals/regression_iv_div_delta.csv', index=False)
