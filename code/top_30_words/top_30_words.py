import pandas as pd

## load data 
RMNIR_score = pd.read_csv(r'data/output/dictionaries/ML_score_unigram_2005_2020.csv')

## calculate Cov measured in basis points
RMNIR_score['Cov'] = RMNIR_score['freq'].apply(lambda x: x / RMNIR_score['freq'].sum() * 10000)
## filter words
pos_words_delta_D0 = RMNIR_score[(RMNIR_score['positive'] - RMNIR_score['negative'] >= 0.95)]
neg_words_delta_D0 = RMNIR_score[(RMNIR_score['negative'] - RMNIR_score['positive'] >= 0.95)]

## sorted by freq and select top 30 pos words
pos_words_delta_D0 = pos_words_delta_D0.sort_values(by='Cov', ascending=False)
neg_words_delta_D0 = neg_words_delta_D0.sort_values(by='Cov', ascending=False)
top_pos_words_delta_D0 = pos_words_delta_D0[['word', 'Cov', 'positive', 'negative']].head(30)
top_neg_words_delta_D0 = neg_words_delta_D0[['word', 'Cov', 'positive', 'negative']].head(30)

## adjust the format
top_pos_words_delta_D0['Cov'] = top_pos_words_delta_D0['Cov'].round(1)
top_pos_words_delta_D0['positive'] = (top_pos_words_delta_D0['positive'] * 100).round(1)
top_pos_words_delta_D0['negative'] = (top_pos_words_delta_D0['negative'] * 100).round(1)

top_neg_words_delta_D0['Cov'] = top_neg_words_delta_D0['Cov'].round(1)
top_neg_words_delta_D0['positive'] = (top_neg_words_delta_D0['positive'] * 100).round(1)
top_neg_words_delta_D0['negative'] = (top_neg_words_delta_D0['negative'] * 100).round(1)

## save data 
top_pos_words_delta_D0.to_csv(r'data/output/top_30_words/top_pos_words.csv', index=False)
top_neg_words_delta_D0.to_csv(r'data/output/top_30_words/top_neg_words.csv', index=False)
