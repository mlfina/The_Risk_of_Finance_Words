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

###################################################################################
# Table  predicting idiosyncratic volatility with ivol dictionaries for Earnings calls
###################################################################################

## Load data
meta <- read.csv("data/output/volatility_signals/regression_idvol.csv")

# drop null
meta <- na.omit(meta)
print(cat(ncol(meta), nrow(meta)))

## Winsorize all variables used in the regression
for(var in c('D01', 'D02', 'D03', 'D04', 
             'D05', 'D06', 'D07', 'D08', 
             'D09', 'D10', 'D11', 'D12', 
             'D13', 'D14', 'D15', 'D16', 
             'D17', 'D18', 'D19', 'D20', 
             "me", "bm", "turn", "sue", "rvar_capm")){
  meta[[var]] <- DescTools::Winsorize(meta[[var]], probs = c(0.01, 0.99))
}

## take out data used for training
# ix <- meta$callDate > "2015-12-31"
# meta <- meta[ix,]

for(var in c('D01', 'D02', 'D03', 'D04', 
             'D05', 'D06', 'D07', 'D08', 
             'D09', 'D10', 'D11', 'D12', 
             'D13', 'D14', 'D15', 'D16', 
             'D17', 'D18', 'D19', 'D20' 
             )){
  meta[[var]] <- meta[[var]] * 100
}

## regression for predicting realized volatility
reg <- list()

reg[[1]] <- felm(
  D01 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
  | ffi49+ quarter | 0 | ffi49 + quarter,
  data = filter(meta))

reg[[2]] <- felm(
D02 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[3]] <- felm(
D03 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[4]] <- felm(
D04 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[5]] <- felm(
D05 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[6]] <- felm(
D06 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[7]] <- felm(
D07 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[8]] <- felm(
D08 ~
    + vol_pos_uni + vol_neg_uni
    + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[9]] <- felm(
D09 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[10]] <- felm(
D10 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[11]] <- felm(
D11 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[12]] <- felm(
D12 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[13]] <- felm(
D13 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[14]] <- felm(
D14 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[15]] <- felm(
D15 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[16]] <- felm(
D16 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[17]] <- felm(
D17 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[18]] <- felm(
D18 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[19]] <- felm(
D19 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[20]] <- felm(
D20 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg[[21]] <- felm(
D00 ~
    + vol_pos_uni + vol_neg_uni
  + log(me) + log(bm) + log(turn) + sue + nasdaq
| ffi49+ quarter | 0 | ffi49 + quarter,
data = filter(meta))

reg_summary <- stargazer(reg,
          type = "text",
          keep.stat = c("n", "rsq"),
          digits = 2, 
          digits.extra = 0,
          align = T, 
          no.space = T,
          report = "vc*t"
          )

## save the regression results
writeLines(reg_summary, "data/output/predicting_idvol/results.txt")

# save coefficients of predicting
coefficients_df <- data.frame(
                              Model = character(0), 
                              Variable = character(0), 
                              Coefficient = numeric(0),
                              Lower_CI = numeric(0),
                              Upper_CI = numeric(0)
                              )

for (i in 1:length(reg)){
  coefficients <- coef(reg[[i]])
  variable_names <- names(coefficients)
  conf_interval <- confint(reg[[i]])
  lower_ci <- conf_interval[, 1]
  upper_ci <- conf_interval[, 2]

  model_df <- data.frame(
    Model = ifelse(i < 10, paste0("D0", i), paste0("D", i)),
    Variable = variable_names,
    Coefficient = coefficients,
    Lower_CI = lower_ci,
    Upper_CI = upper_ci
  )
  coefficients_df <- rbind(coefficients_df, model_df)
}

write.csv(coefficients_df, file='data/output/predicting_idvol/coeffs.csv', row.names=FALSE)
