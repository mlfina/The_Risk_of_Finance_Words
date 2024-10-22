import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def data_split(meta, days_before, days_after):

    permno = meta['permno']
    print(permno)
    meta = pd.DataFrame(meta).T
    data_crsp = pd.read_csv(r'data/input/beta/beta_{}.csv'.format(permno))
    meta['sig'] = 1
    data_crsp = pd.merge(data_crsp, meta[['permno', 'date', 'sig']], on=['permno', 'date'], how='left')
    data_crsp['b_mkt'] = data_crsp['b_mkt'].shift(-21)
    data_crsp['ivol'] = data_crsp['ivol'].shift(-21)
    data_crsp['tvol'] = data_crsp['tvol'].shift(-21)

    sig_df = data_crsp[data_crsp['sig'] == 1]

    ## get data before and after event
    if sig_df.empty:
        return sig_df
    
    else:
        index_eventday = sig_df.index[0]
        start_index = max(0, index_eventday - days_before)
        end_index = min(len(data_crsp) - 1, index_eventday + days_after)
        selected_data = data_crsp.iloc[start_index:end_index + 1]
        selected_data = selected_data.fillna(np.nan)
        selected_data = selected_data.reset_index(drop=True)

        return selected_data

def get_data(meta, days_before, days_after):

    ## get splited data 
    selected_data = data_split(meta, days_before, days_after)

    if selected_data.empty:
        return None, None
    
    else:
        ## cal rv
        center_index = selected_data[selected_data['sig'] == 1].index[0]
        num_rows_before = max(0, 20 - center_index)
        num_rows_after = max(0, 20 - (len(selected_data) - 1 - center_index))
        empty_rows = pd.DataFrame(columns=selected_data.columns, index=range(num_rows_before + num_rows_after))
        selected_data = pd.concat([empty_rows.iloc[:num_rows_before], selected_data, empty_rows.iloc[num_rows_before:]], ignore_index=True)
        selected_data.reset_index(drop=True, inplace=True)

        data_beta = selected_data['b_mkt'].to_list()
        data_ivol = selected_data['ivol'].to_list()
        data_tvol = selected_data['tvol'].to_list()

        return data_beta, data_ivol, data_tvol

if __name__ == '__main__':

    ## load data
    meta = pd.read_csv(r'data/input/regression.csv')

    ## save rv data and iv data
    columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
    data_beta = pd.DataFrame(columns=columns)
    data_ivol = pd.DataFrame(columns=columns)
    data_tvol = pd.DataFrame(columns=columns)

    for index, meta_temp in meta.iterrows():
        data_beta_temp, data_ivol_temp, data_tvol_temp = get_data(meta_temp, 20, 20)
        data_beta.loc[len(data_beta)] = data_beta_temp
        data_ivol.loc[len(data_ivol)] = data_ivol_temp
        data_tvol.loc[len(data_tvol)] = data_tvol_temp

    ## merge data 
    regression_beta = pd.concat([meta, data_beta], axis=1)
    regression_ivol = pd.concat([meta, data_ivol], axis=1)
    regression_tvol = pd.concat([meta, data_tvol], axis=1)

    ## save data 
    regression_beta.to_csv(r'data/input/regression_beta.csv', index=False)
    regression_ivol.to_csv(r'data/input/regression_idvol.csv', index=False)
    regression_tvol.to_csv(r'data/input/regression_ttlvol.csv', index=False)
