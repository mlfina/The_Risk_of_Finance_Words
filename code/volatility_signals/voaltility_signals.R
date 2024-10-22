## Preamble: set working directory
rm(list = ls())

## packages
require(tibble)
require(dplyr)
require(readr)
require(lfe)
require(stargazer)
require(DescTools)
require(tm)
require(slam)
require(ggplot2)
require(ggthemes)
require(Matrix)
require(fixest)
require(openxlsx)

############################################
## Function to compute words frequency
############################################

## compute sentiment
computeFrequency <- function(
    dict,
    dtm,
    normalize = T, 
    winsorize = T
){
  ## compute sentiment
  sent <- row_sums(dtm[, colnames(dtm) %in% dict], na.rm=T) / row_sums(dtm)
  
  ## normalize
  if(normalize){sent <- sent/sd(sent)}
  
  ## winsorize
  if(winsorize){sent <- DescTools::Winsorize(sent, probs = c(0.01, 0.99))}
  
  ## output
  return(sent)
}

##########################################
# Function to format (round) output
##########################################

print_dec <- function(r,n){
  res <- format(round(r, n), nsmall=n, big.mark = ",")
  res[is.na(r)] <- ""
  res}

############################################################
# Calculate the volatility signals for Earnings calls
############################################################

## Load data
meta_iv <- read.csv("data/input/regression_iv.csv")
meta_rv <- read.csv("data/input/regression_ttlvol.csv")
meta_standardized_iv <- read.csv("data/input/regression_standardized_iv.csv")
meta_idvol <- read.csv("data/input/regression_idvol.csv")
meta_sysvol <- read.csv("data/input/regression_sysvol.csv")

load("data/input/dtm_unigram.RData")
dtmUni <- dtm
rm(dtm)

## LM return dictionaries
LM_pos <- readLines("data/output/dictionaries/LM_pos.txt")
LM_neg <- readLines("data/output/dictionaries/LM_neg.txt")
LM_Uncertainty <- readLines("data/output/dictionaries/LM_uncertainty.txt")
LM_Litigious <- readLines("data/output/dictionaries/LM_Litigious.txt")
LM_Strong_Modal <- readLines("data/output/dictionaries/LM_Strong_Modal.txt")
LM_Weak_Modal <- readLines("data/output/dictionaries/LM_Weak_Modal.txt")
LM_Constraining <- readLines("data/output/dictionaries/LM_Constraining.txt")
LM_Complexity <- readLines("data/output/dictionaries/LM_Complexity.txt")

## color dictionary
color_pos_uni <- readLines("data/output/dictionaries/color_positive_dictionary.txt")
color_neg_uni <- readLines("data/output/dictionaries/color_negative_dictionary.txt")

## volatility dictionaries
vol_pos_uni <- readLines("data/output/dictionaries/volatility_positive_dictionary_2005_2020.txt")
vol_neg_uni <- readLines("data/output/dictionaries/volatility_negative_dictionary_2005_2020.txt")

## Compute words frequency
meta_iv$color_pos_uni <- computeFrequency(color_pos_uni, dtmUni)
meta_iv$color_neg_uni <- computeFrequency(color_neg_uni, dtmUni)
meta_iv$LM_pos <- computeFrequency(LM_pos, dtmUni)
meta_iv$LM_neg <- computeFrequency(LM_neg, dtmUni)
meta_iv$vol_pos_uni <- computeFrequency(vol_pos_uni, dtmUni)
meta_iv$vol_neg_uni <- computeFrequency(vol_neg_uni, dtmUni)

meta_iv$LM_Uncertainty <- computeFrequency(LM_Uncertainty, dtmUni)
meta_iv$LM_Litigious <- computeFrequency(LM_Litigious, dtmUni)
meta_iv$LM_Strong_Modal <- computeFrequency(LM_Strong_Modal, dtmUni)
meta_iv$LM_Weak_Modal <- computeFrequency(LM_Weak_Modal, dtmUni)
meta_iv$LM_Constraining <- computeFrequency(LM_Constraining, dtmUni)
meta_iv$LM_Complexity <- computeFrequency(LM_Complexity, dtmUni)

# ###########################
meta_rv$color_pos_uni <- computeFrequency(color_pos_uni, dtmUni)
meta_rv$color_neg_uni <- computeFrequency(color_neg_uni, dtmUni)
meta_rv$LM_pos <- computeFrequency(LM_pos, dtmUni)
meta_rv$LM_neg <- computeFrequency(LM_neg, dtmUni)
meta_rv$vol_pos_uni <- computeFrequency(vol_pos_uni, dtmUni)
meta_rv$vol_neg_uni <- computeFrequency(vol_neg_uni, dtmUni)

meta_rv$LM_Uncertainty <- computeFrequency(LM_Uncertainty, dtmUni)
meta_rv$LM_Litigious <- computeFrequency(LM_Litigious, dtmUni)
meta_rv$LM_Strong_Modal <- computeFrequency(LM_Strong_Modal, dtmUni)
meta_rv$LM_Weak_Modal <- computeFrequency(LM_Weak_Modal, dtmUni)
meta_rv$LM_Constraining <- computeFrequency(LM_Constraining, dtmUni)
meta_rv$LM_Complexity <- computeFrequency(LM_Complexity, dtmUni)

# ###########################

meta_standardized_iv$color_pos_uni <- computeFrequency(color_pos_uni, dtmUni)
meta_standardized_iv$color_neg_uni <- computeFrequency(color_neg_uni, dtmUni)
meta_standardized_iv$LM_pos <- computeFrequency(LM_pos, dtmUni)
meta_standardized_iv$LM_neg <- computeFrequency(LM_neg, dtmUni)
meta_standardized_iv$vol_pos_uni <- computeFrequency(vol_pos_uni, dtmUni)
meta_standardized_iv$vol_neg_uni <- computeFrequency(vol_neg_uni, dtmUni)

meta_standardized_iv$LM_Uncertainty <- computeFrequency(LM_Uncertainty, dtmUni)
meta_standardized_iv$LM_Litigious <- computeFrequency(LM_Litigious, dtmUni)
meta_standardized_iv$LM_Strong_Modal <- computeFrequency(LM_Strong_Modal, dtmUni)
meta_standardized_iv$LM_Weak_Modal <- computeFrequency(LM_Weak_Modal, dtmUni)
meta_standardized_iv$LM_Constraining <- computeFrequency(LM_Constraining, dtmUni)
meta_standardized_iv$LM_Complexity <- computeFrequency(LM_Complexity, dtmUni)

# ###########################

meta_idvol$color_pos_uni <- computeFrequency(color_pos_uni, dtmUni)
meta_idvol$color_neg_uni <- computeFrequency(color_neg_uni, dtmUni)
meta_idvol$LM_pos <- computeFrequency(LM_pos, dtmUni)
meta_idvol$LM_neg <- computeFrequency(LM_neg, dtmUni)
meta_idvol$vol_pos_uni <- computeFrequency(vol_pos_uni, dtmUni)
meta_idvol$vol_neg_uni <- computeFrequency(vol_neg_uni, dtmUni)

meta_idvol$LM_Uncertainty <- computeFrequency(LM_Uncertainty, dtmUni)
meta_idvol$LM_Litigious <- computeFrequency(LM_Litigious, dtmUni)
meta_idvol$LM_Strong_Modal <- computeFrequency(LM_Strong_Modal, dtmUni)
meta_idvol$LM_Weak_Modal <- computeFrequency(LM_Weak_Modal, dtmUni)
meta_idvol$LM_Constraining <- computeFrequency(LM_Constraining, dtmUni)
meta_idvol$LM_Complexity <- computeFrequency(LM_Complexity, dtmUni)

# ###########################

meta_sysvol$color_pos_uni <- computeFrequency(color_pos_uni, dtmUni)
meta_sysvol$color_neg_uni <- computeFrequency(color_neg_uni, dtmUni)
meta_sysvol$LM_pos <- computeFrequency(LM_pos, dtmUni)
meta_sysvol$LM_neg <- computeFrequency(LM_neg, dtmUni)
meta_sysvol$vol_pos_uni <- computeFrequency(vol_pos_uni, dtmUni)
meta_sysvol$vol_neg_uni <- computeFrequency(vol_neg_uni, dtmUni)

meta_sysvol$LM_Uncertainty <- computeFrequency(LM_Uncertainty, dtmUni)
meta_sysvol$LM_Litigious <- computeFrequency(LM_Litigious, dtmUni)
meta_sysvol$LM_Strong_Modal <- computeFrequency(LM_Strong_Modal, dtmUni)
meta_sysvol$LM_Weak_Modal <- computeFrequency(LM_Weak_Modal, dtmUni)
meta_sysvol$LM_Constraining <- computeFrequency(LM_Constraining, dtmUni)
meta_sysvol$LM_Complexity <- computeFrequency(LM_Complexity, dtmUni)

write.csv(meta_iv, file='data/output/volatility_signals/regression_iv.csv', row.names=FALSE)
write.csv(meta_rv, file='data/output/volatility_signals/regression_ttlvol.csv', row.names=FALSE)
write.csv(meta_standardized_iv, file='data/output/volatility_signals/regression_standardized_iv.csv', row.names=FALSE)
write.csv(meta_idvol, file='data/output/volatility_signals/regression_idvol.csv', row.names=FALSE)
write.csv(meta_sysvol, file='data/output/volatility_signals/regression_sysvol.csv', row.names=FALSE)
