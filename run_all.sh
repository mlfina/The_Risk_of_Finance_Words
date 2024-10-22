## First process data and get all the variables.
## Split raw data and get control variables.
python ./code/data_processing/data_preprocessing.py > ./data/output/data_processing/data_preprocessing.log.txt
## Get implied volatility from day -20 to day 20 around earnings call events or the filiing dates of 10-Ks or WSJs.
python ./code/data_processing/data_iv.py > ./data/output/data_processing/data_iv.log.txt
## Get standardized implied volatility from day -20 to day 20 around earnings call events.
python ./code/data_processing/data_standardized_iv.py > ./data/output/data_processing/data_standardized_iv.log.txt
## Get  idiosyncratic volatility and systemic volatility from day -20 to day 20 around earnings call events.
python ./code/data_processing/data_beta.py > ./data/output/data_processing/data_beta.log.txt
python ./code/data_processing/data_idvol_sysvol.py > ./data/output/data_processing/data_idvol_sysvol.log.txt


## Step1: estimate robust MNIR and structure output 
Rstript ./code/dictionaries/unigrams.R > ./data/output/dictionaries/unigrams.log.txt

## Step2: set cutoff and construct volatility dictionareis
Rstript ./code/dictionaries/construct_dictionaries.R

## Step3: calculate volatility signals
Rstript ./code/volatility_signals/volatility_signals.R

## Step4: get all the tables and figures in our paper.
## All tables
## Table 1 
python ./code/top_30_words/top_30_words.py
## Table 2 & Table 3
Rstript ./code/predicting_standardized_iv/predicting_standardized_iv.R
## Table 4 
Rstript ./code/predicting_iv/predicting_iv.R
## Table 5
Rstript ./code/predicting_rv/predicting_rv.R
## Table 6
Rstript ./code/predicting_idvol/predicting_idvol.R
Rstript ./code/predicting_sysvol/predicting_sysvol.R

## All figures
## Figure 1
python ./code/statistic_summary/statistic_summary.py
## Figure 2 and A.5
python ./code/venn_diagrams/venn_diagrams.py
## Figure 3
python ./code/fama_macbeth/fama_macbeth.py
## Figure A.1
python ./code/coeffs_time_series/coeffs_time_series.py

## For all the out-of-sample results in appendices, you can choose year 2005-2015 in ./code/dictionaries/RMNIN_score/unigrams.R
## and generate out-of-sample volatility dictionaries
