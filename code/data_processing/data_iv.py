import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def data_split(meta, days_before, days_after):

    permno = meta['permno']
    print(permno)
    meta = pd.DataFrame(meta).T
    data_crsp = pd.read_csv(r'data/input/crsp_d/crsp_d_{}.csv'.format(permno))
    meta['sig'] = 1
    data_crsp = pd.merge(data_crsp, meta[['permno', 'date', 'sig']], on=['permno', 'date'], how='left')
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

def get_rv_iv(meta, days_before, days_after):

    ## get splited data 
    selected_data = data_split(meta, days_before, days_after)

    if selected_data.empty:
        return None, None
    
    else:
        center_index = selected_data[selected_data['sig'] == 1].index[0]
        num_rows_before = max(0, 20 - center_index)
        num_rows_after = max(0, 49 - (len(selected_data) - 1 - center_index))
        empty_rows = pd.DataFrame(columns=selected_data.columns, index=range(num_rows_before + num_rows_after))
        selected_data = pd.concat([empty_rows.iloc[:num_rows_before], selected_data, empty_rows.iloc[num_rows_before:]], ignore_index=True)
        selected_data.reset_index(drop=True, inplace=True)

        ## iv 
        iv_data = selected_data['ivolc'][:41].to_list()

        return iv_data

if __name__ == '__main__':

    ## load data
    meta = pd.read_csv(r'data/input/regression.csv')
    
    ## save rv data and iv data
    columns = ["D0" + str(i) if 0 <= i < 10 else "D" + str(i) if i >= 10 else "Dbefore" + str(abs(i)) for i in range(-20, 21)]
    rv_data = pd.DataFrame(columns=columns)
    iv_data = pd.DataFrame(columns=columns)
    
    for index, meta_temp in meta.iterrows():
        iv_data_temp = get_rv_iv(meta_temp, 20, 50)
        iv_data.loc[len(iv_data)] = iv_data_temp

    ## merge data 
    regression_iv = pd.concat([meta, iv_data], axis=1)

    ## save data 
    regression_iv.to_csv(r'data/input/regression_iv.csv', index=False)
