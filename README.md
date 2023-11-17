# An Evolutionary View on The Making of Good Films 🎬

## Abstract

The impact of historical events on the influence of movies is undeniable. During periods of societal changes, films often reflect prevailing sentiments, collective values and historical events. As cultural norms shift with time, so do audience preferences and tastes in films. This influence reflects directly on the audience ratings of the stories that movie-makers seek to tell, giving us a unique lens to examine how people's perception of "a good film" has evolved over time. 


## Research Questions 🔎

In our analysis, our objective is to evaluate the shift in the audience's perception of good films over time. We do this by focusing on the following key perspectives and answering their related research questions:

Genre and Runtime 
- Which genres and/or combination of genres are the most appreciated and supported by higher ratings? Did any particular genre stand out in the test of time? Did any genre have a meteoric rise that symbolizes a turning point in movie history? 

- Are there any sweet spots or patterns in the length of top-rated films over the years? Is there a significant difference in the length of good movies across genres?

Ethnic, Gender and Language Diversity
- How has the global actor demographics changed over time in terms of ethnic background, gender and languages spoken? Does the demographic shift translate to more ethnically, gender and linguistically diverse movies produced over the years? More importantly, is a more ethnically, gender and linguistically diverse cast appreciated by the audience and directly contribute to higher movie ratings?

Stars
- Does star power translate to higher ratings? How has the impact of stars evolved over time in movie ratings?

## Additional Datasets 📈
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - We measure movie-goers' perception of film quality directly by movie ratings. A dataset from IMDb is extracted to complement the movie dataset with rating information that includes the `average rating` and `number of votes` for each film.


## Methods 🔤
When dealing with the time-series movie dataset, we first break down our features of interest by decade, and then apply the following methodologies to carry out the analyses:

### T-tests
When examining the diverse genres within the dataset, we observe a high number of different genres, with certain genres covering only an insignificant number of movies.
Consequently, we opt to filter out genres that contain fewer than 500 movies.
We assume that the most "likeable" movies genres lie within the most common (with the most number of movies).
To validate this assumption and assess the potential impact of this bias on our subsequent results, we will conduct a T-test.
//// We simulate the t-tests 10 000 times to calculate the statistical power, and we use bootstrap with 10 000 draws to compute the 95% CI. We have been able to use t-tests without normality because of the central limit theorem. 

### Linear Regression
We performed linear regression to see the correlation between the time duration of movies and decades. Nevertheless, we plan to investigate other suitable methodologies in milestone 3 to improve our research approach

## Proposed timeline ⏳
```
.
├── 1 Décembre : Homework 2 Deadline
├── 10 Décembre 2023: Create an initial draft for the data story
├── 15 Décembre 2023: Complete the code implementations and visualizations
├── 20 Décembre 2023: Finalize the data story
├── 22 Décembre 2023: Deadline for Milestone 3
.

```



