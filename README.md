# What makes a good film 🎬

## Abstract


## Research Questions 🔎

## Additional Datasets 📈
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - In addition to defining a movie successful in financial terms, we want to make the definition more diverse by measuring success in terms of ratings. We have extracted two datasets from IMDb - one for making the merge with our movie data possible (`movie name,` `release year,` and `runtime`) and one for extracting the `average rating` and `number of votes` received.


## Methods 🔤

### T-tests
We use t-tests to determine if there is a significant difference between the groups' means (`revenue`). We simulate the t-tests 10 000 times to calculate the statistical power, and we use bootstrap with 10 000 draws to compute the 95% CI. We have been able to use t-tests without normality because of the central limit theorem. 

### Linear Regression
We performed linear regression with ordinary least squares (OLS) to see the correlation between various attributes and `revenue.` In our initial analysis, we were particularly interested in R-squared to see how our models explain the revenue made.

### Paired Matching
We used paired matching to check for causlity in observed correlations. To match the two groups we standardized the continuous variables, calculated propensity scores and match based on genre and propensity score with a threshold of >0.95.

## Proposed timeline ⏳
```
.
├── 21.11.22 - TODO

.

```
