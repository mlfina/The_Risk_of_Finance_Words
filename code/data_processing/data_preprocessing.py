import numpy as np
import pandas as pd
import pyarrow.feather as fr
import pandas_market_calendars as mcal
import matplotlib.pyplot as plt
from Industry import ffi49
import os 

###############################################
##  merge earnings calls data with option data
###############################################

## load data
data_crsp = pd.read_csv(r'data/input/crsp_d_20230903.csv')
ivol = pd.read_csv(r'data/input/iv_30d.csv')

## merge iv calculated using call option
ivolC = ivol[ivol['cp_flag'] == 'C']
ivolC['date'] = ivolC['date'].apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
data_crsp = pd.merge(data_crsp, ivolC[['PERMNO', 'date', 'impl_volatility']], on=['PERMNO', 'date'], how='left')
data_crsp.rename(columns={'impl_volatility':'ivolc'}, inplace=True)

## merge iv calculated using put option
ivolP = ivol[ivol['cp_flag'] == 'P']
ivolP['date'] = ivolP['date'].apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
data_crsp = pd.merge(data_crsp, ivolP[['PERMNO', 'date', 'impl_volatility']], on=['PERMNO', 'date'], how='left')
data_crsp.rename(columns={'impl_volatility':'ivolp'}, inplace=True)

data_crsp.to_csv(r'data/input/crsp_d_20230903.csv', index=False)

#########################################
# event occurs on hoildays or weekends
#########################################

## raw data
meta = pd.read_csv('data/input/meta.csv')
## using the next available trading day for event that occurs on hoildays or weekends
nyse = mcal.get_calendar('XNYS')
results = []
for target_date in meta['callDate']:
    target_date = pd.to_datetime(target_date)
    trading_days = nyse.valid_days(start_date=target_date, end_date=target_date + pd.Timedelta(days=7))[0]
    results.append(trading_days.strftime('%Y-%m-%d'))
meta['date'] = results

## save data 
meta.to_csv(r'data/input/meta.csv', index=False)

############################
##  get control variables
############################

## merge data and get control variables.
chars60_raw_no_impute = fr.read_feather('data/input/chars60_raw_no_impute.feather')
chars60_raw_no_impute['mon'] = chars60_raw_no_impute['date'].apply(lambda x: x.strftime('%Y-%m'))
meta = pd.read_csv('data/input/meta.csv')
meta['mon'] = meta['date'].apply(lambda x: x[:7])
meta = pd.merge(meta, chars60_raw_no_impute[['permno', 'mon', 'me', 'bm', 'turn', 'sue', 'rvar_capm','exchcd', 'sic']], 
                on=['permno', 'mon'], how='left')

## get nasday var
meta['nasdaq'] = np.where(1, meta['exchcd'] == 3, 0)
## get ffi49 industries
meta['ffi49'] = ffi49(meta)
meta['ffi49'] = meta['ffi49'].fillna(49)
meta['ffi49'] = meta['ffi49'].astype(int)
meta['quarter'] = meta['date'].apply(lambda x: x[:7])

## save data 
meta.to_csv(r'data/input/regression.csv', index=False)

######################
#    data split 
######################

## load data
meta = pd.read_csv('data/input/regression.csv')
crsp_d = pd.read_csv(r'data/input/crsp_d.csv')
crsp_d.columns = crsp_d.columns.str.lower()

## process return data 
crsp_d['ret'] = crsp_d[['ret']].replace('[A-Za-z]', 0, regex=True)
crsp_d['ret'] = crsp_d['ret'].astype('float64')
 
# get company related to Earning calls and save
permno = meta.permno.unique().tolist()
# daily data for earnings calls 
for temp_permno in permno:
    print(temp_permno)
    crsp_temp = crsp_d[crsp_d['permno'] == temp_permno]
    path = r'data/input/crsp_d/crsp_d_{}.csv'.format(temp_permno)
    crsp_temp.to_csv(path, index=False)

## load data
meta = pd.read_csv('data/input/regression.csv')
beta = pd.read_csv(r'data/input/beta.csv')
beta.columns = beta.columns.str.lower()

## process return data 
beta['ret'] = beta[['ret']].replace('[A-Za-z]', 0, regex=True)
beta['ret'] = beta['ret'].astype('float64')
 
# get company related to Earning calls and save
permno = meta.permno.unique().tolist()
# daily data for earnings calls 
for temp_permno in permno:
    print(temp_permno)
    crsp_temp = beta[beta['permno'] == temp_permno]
    path = r'data/input/beta/beta_{}.csv'.format(temp_permno)
    crsp_temp.to_csv(path, index=False)
