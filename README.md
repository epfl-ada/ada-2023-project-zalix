# An evolutionary view on the making of good films 🎬

## Abstract

The impact of historical events on the influence of movies is undeniable. During periods of societal change, films often reflect prevailing sentiments, offering either escapism or relevant narratives. As cultural norms shift over decades, so too do audience tastes, influencing preferences for certain themes and genres. 

After World War II, for example, there was a desire for stability, optimism, and a sense of normalcy. This shift in societal mood was reflected in the popularity of films that offered a form of escapism and optimism. As a result, genres such as musicals, romantic comedies, and family-friendly dramas gained prominence. These genres provided audiences with a break from the harsh realities of war and offered a more lighthearted and optimistic view of life. 


## Research Questions 🔎

In our analysis, our objective is to evaluate whether the audience's perception of a good movie has undergone any evolution over time. To explore the potential impact of time on audience movie preferences, we have focused on addressing these key research questions:

-Within the 10 most common film genres, which genre and/or combination of genres were the most appreciated and high-rated during each decade ? Did any particular genre stand out and could be symbolizing a historical turning point ? 

-Are there any trends or patterns in the distribution of durations for top-rated films over the years and is there a significant difference in the distribution of durations between different genres among top-rated films?


## Additional Datasets 📈
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - In addition to defining a movie successful in financial terms, we want to make the definition more diverse by measuring success in terms of ratings. We have extracted two datasets from IMDb - one for making the merge with our movie data possible (`movie name,` `release year,` and `runtime`) and one for extracting the `average rating` and `number of votes` received.


## Methods 🔤

### T-tests
When examining the diverse genres within the dataset, we observe a high number of different genres, with certain genres covering only an insignificant number of movies.
Consequently, we opt to filter out genres that contain fewer than 500 movies.
We assume that the most "likeable" movies genres lie within the most common (with the most number of movies).
To validate this assumption and assess the potential impact of this bias on our subsequent results, we will conduct a T-test.
//// We simulate the t-tests 10 000 times to calculate the statistical power, and we use bootstrap with 10 000 draws to compute the 95% CI. We have been able to use t-tests without normality because of the central limit theorem. 

### Linear Regression
We performed linear regression to see the correlation between the time duration of movies and decades. Nevertheless, we plan to investigate other suitable methodologies in milestone 3 to improve our research approach

## Proposed timeline ⏳

1 Décembre : Homework 2 Deadline
10 Décembre 2023: Create an initial draft for the data story
15 Décembre 2023: Complete the code implementations and visualizations
20 Décembre 2023: Finalize the data story
22 Décembre 2023: Deadline for Milestone 3


```
