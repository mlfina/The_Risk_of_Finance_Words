###################################################
# ESTIMATE ROBUST MNIR AND STRUCTURE OUTPUT       #
###################################################
rm(list = ls())

## Number of iterations for the robust MNIR algorithm
no.iterations <- 500

## Load packages
require(tibble)
require(dplyr)
require(readr)
require(parallel)
require(textir)
require(tm)
require(slam)
require(DescTools)
require(Matrix)

#########################################
# Function to estimate MNIR 
#########################################

getMnirLoadings <- function(meta = meta, # Data with Y variable
                            filter = T, # Additional filter
                            dtm =  dtm,  # Document term Matrix
                            n.terms = 2^16, # number of terms used
                            nr.clusters = 20 # number of clusters used for MNIR implementation
){

  ## This function just needs a meta object
  ## with a filing.period.excess.return variable.
  ## The PERMNO+ information provided in the repository 
  ## should make this easily available to many researchers.
  ## But we note this function will not run without an updated
  ## metadata file (relative to what we share in the repository).
    
  ## initiate cluster
  cl <- makeCluster(nr.clusters)
 
  ## only take the top X terms
  if(ncol(dtm) > n.terms){dtm <- dtm[,1:n.terms]}
  
  ## Filter 1: limit with provided filter
  meta <- meta[filter, ]
  dtm <- dtm[filter, ]
  
  ## Filter 2: take out empty documents
  filter2 <- row_sums(dtm) != 0
  meta <- meta[filter2, ]
  dtm <- dtm[filter2, ]
  
  ## Filter 3: take out empty terms
  filter3 <- col_sums(dtm) != 0
  dtm <- dtm[, filter3]
  
  ## Winsorize at 1-99%
  meta$D00 <- Winsorize(meta$D00, probs = c(0.01, 0.99))
  
  ## Fit the MNIR model
  fits <- dmr(cl,
              meta$D00,
              dtm,
              bins = NULL,
              gamma = 0,
              nlambda = 10,
              verb = 2)
  
  ## Extract MNIR coefs
  mnir.coef <- sort(coef(fits)[2,])
  
  ## end cluster
  stopCluster(cl)
  
  ## output
  return(mnir.coef)
}


##########################################
## Function to structure robust MNIR ouput
##########################################

structureRobustMnirOutput <- function(MNIRest = MNIRest, # output of function getMnirLoadings
                                      wordCount, # word count 
                                      filePath = NULL # output destination
){
  
  # Adjust colname
  names(MNIRest) <- 1:length(MNIRest)
  
  # make into a tibble
  lapply(names(MNIRest), function(cn){
    temp <- tibble(word = names(MNIRest[[cn]]))
    temp[[cn]] <- 0
    temp[[cn]][0 > as.vector(MNIRest)[[cn]]] <- -1
    temp[[cn]][0 < as.vector(MNIRest)[[cn]]] <- 1
    temp
  }) -> MNIRest
  
  # aggregate
  out <- MNIRest[[1]]
  for(i in 2:length(MNIRest)){out <- full_join(out, MNIRest[[i]])}
  MNIRest <- out
  rm(out) 
  
  # summarise 
  MNIRest[,-1] %>% 
    apply(., 1, function(x){
      c(positive = sum(x == 1, na.rm=T), 
        negative = sum(x == -1, na.rm=T), 
        missing = sum(is.na(x)))
    }) %>% 
    t() %>% 
    as_tibble() %>% 
    mutate(word = MNIRest[,1]) -> MNIRest
  MNIRest$word <- unlist(MNIRest$word)
  names(MNIRest$word) <- NULL
  
  # Add information 
  MNIRest %>%
    left_join(wordCount) %>%
    arrange(-(positive-negative)) %>%
    mutate(positive = positive / no.iterations) %>%
    mutate(negative = negative / no.iterations) %>%
    select(word, positive, negative, freq) -> MNIRest
  
  # save
  write.csv(MNIRest, file = filePath, row.names = F)
  
  # end
  return(NULL)}

#######################################################
## Estimate Robust MNIR: top 16K unigrams, pre 2016
#######################################################

## load data
meta = read.csv("data/input/regression_standardized_iv.csv")
load("data/input/dtm_unigram.RData")

MNIRest <- list()
## Transforming the document-term-matrix
dtm <- Matrix::as.matrix(dtm)

# ## limit to pre 2016
# ix <- meta$callDate <= as.Date("2015-12-31")
# meta <- meta[ix, ]
# dtm <- dtm[ix, ]

## drop nan in implied volatility
selected_columns <- meta[c("D00")]
ix <- apply(selected_columns, 1, function(row) any(is.na(row)))
ix <- !ix
meta <- meta[ix, ]
dtm <- dtm[ix, ]

## estimate robust MNIR
for(i in 1:no.iterations){
    cat("Iteration", i, "\n")

    # randomly select 5000 observations for each iteration
    filter.sample <- (1:nrow(meta)) %in% (sample(1:nrow(meta), 5000))

    # Call getMnirLoadings function
    MNIRest[[i]] <- getMnirLoadings(meta = meta,
                                    filter = filter.sample,
                                    dtm =  dtm,
                                    n.terms = 2^14,
                                    nr.clusters = 20)
}

## Get word counts
load("data/input/dtm_unigram.RData")
wordCount <- tibble(word = colnames(dtm), freq = col_sums(dtm))

## structure and save
structureRobustMnirOutput(MNIRest = MNIRest,
                          wordCount = wordCount,
                          filePath = "data/output/dictionaries/ML_score_unigram_2005_2020.csv")

