####################################################
## CONSTRUCT DICTIONARIES                          #
####################################################

# Preamble, setting working directory

rm(list = ls())

## packages
require(tibble)
require(dplyr)
require(readr)

## construct and save positive dictionary
read_csv("data/output/dictionaries/ML_score_unigram_2005_2020.csv") %>% 
  filter(positive-negative >= 0.95) %>% 
  pull(word) %>% 
  write_lines(file = "data/output/dictionaries/volatility_positive_dictionary_2005_2020.txt")


## construct and save positive dictionary
read_csv("data/output/dictionaries/ML_score_unigram_2005_2020.csv") %>% 
  filter(negative-positive >= 0.95) %>% 
  pull(word) %>% 
  write_lines(file = "data/output/dictionaries/volatility_negative_dictionary_2005_2020.txt")

