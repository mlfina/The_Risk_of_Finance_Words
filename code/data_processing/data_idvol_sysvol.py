import pandas as pd
import numpy as np

regression = pd.read_csv(r'data/input/regression.csv')
meta_ivol = pd.read_csv(r'data/input/regression_idvol.csv')
meta_tvol = pd.read_csv(r'data/input/regression_ttlvol.csv')

ivol =  meta_ivol[["Dbefore20", "Dbefore19", "Dbefore18", "Dbefore17",
        "Dbefore16", "Dbefore15", "Dbefore14", "Dbefore13",
        "Dbefore12", "Dbefore11", "Dbefore10", "Dbefore9",
        "Dbefore8", "Dbefore7", "Dbefore6", "Dbefore5",
        "Dbefore4", "Dbefore3", "Dbefore2", "Dbefore1", "D00",
        'D01', 'D02', 'D03', 'D04', 
        'D05', 'D06', 'D07', 'D08', 
        'D09', 'D10', 'D11', 'D12', 
        'D13', 'D14', 'D15', 'D16', 
        'D17', 'D18', 'D19', 'D20']]

tvol = meta_tvol[["Dbefore20", "Dbefore19", "Dbefore18", "Dbefore17",
        "Dbefore16", "Dbefore15", "Dbefore14", "Dbefore13",
        "Dbefore12", "Dbefore11", "Dbefore10", "Dbefore9", 
        "Dbefore8", "Dbefore7", "Dbefore6", "Dbefore5",
        "Dbefore4", "Dbefore3", "Dbefore2", "Dbefore1", "D00",
        'D01', 'D02', 'D03', 'D04', 
        'D05', 'D06', 'D07', 'D08', 
        'D09', 'D10', 'D11', 'D12', 
        'D13', 'D14', 'D15', 'D16', 
        'D17', 'D18', 'D19', 'D20']]
print(ivol.describe())
print(tvol.describe())

def percent_to_float(percentage_str):
    try:
        return float(percentage_str.strip('%')) / 100
    except:
        return np.nan
    
tvol = tvol.applymap(percent_to_float)
ivol = ivol.applymap(percent_to_float)

sysvol = tvol - ivol
meta_sysvol = pd.concat([regression, sysvol], axis=1)
meta_sysvol.to_csv(r'data/input/regression_sysvol.csv', index=False)
meta_ivol = pd.concat([regression, ivol], axis=1)
meta_ivol.to_csv(r'data/input/regression_idvol.csv', index=False)
meta_tvol = pd.concat([regression, tvol], axis=1)
meta_tvol.to_csv(r'data/input/regression_ttlvol.csv', index=False)

print(meta_sysvol.describe())
print(meta_ivol.describe())
print(meta_tvol.describe())
