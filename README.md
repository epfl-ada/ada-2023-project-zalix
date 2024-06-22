# An Evolutionary View on The Making of Good Films 🎬

## Abstract

The impact of historical events on the influence of movies is undeniable. During periods of societal changes, films often reflect prevailing sentiments, collective values and historical events. As cultural norms shift with time, so do audience preferences and tastes in films. This influence reflects directly on the audience ratings of the stories that movie-makers seek to tell, giving us a unique lens to examine how people's perception of "a good film" has evolved over time. 

Please find our data story [**here**](https://xioz.github.io/ada-zalix-website/).

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


### Filtering of movies
Our attention is directed towards a curated selection of movies that we categorize as likeable.  We choose that a movie earns the designation of being likeable if its rating is 7 or higher.


### Selection of studied genres and T-test
When examining the diverse genres within the dataset, we observe a high number of different genres, with certain genres covering only an insignificant number of movies.
We decide to focus on the top 10 genres that have the largest number of movies and label them as the “main genres”.
Here we make the assumption that the most likable genres lie within the most common, therefore the results of our analysis will not be overly biased.
To validate this assumption and assess the potential impact of this bias on our subsequent results, we will conduct a T-test.

### Log scaling or outliers removal
When visualizing the distribution of movie runtimes, we observe instances where the runtime exceeds 5000 minutes.
 For now, we decide to consider these movies as outliers and filter them out, but we could consider the duration as heavy-tailed data.
Log scaling is also used for the genre vs number of movies plot.

### Linear Regression
We performed linear regression to see the correlation between the time duration of movies and decades. Nevertheless, we plan to investigate other suitable methodologies in milestone 3 to improve our research approach

### Paired Matching
To analyze film ratings from a diversity perspective, the dataset is split into two groups: films with a diverse cast (number of ethnicities higher than 2 among actors) and films with a non-diverse cast. We then use a paired matching approach to compare the ratings of the two groups to see if movies with diverse cast are generally rated higher. Logistic regression is performed for propensity matching on all other relevant attributes. Similarly, the analysis is done for the other diversity features of interest: gender and languages.

### Paired Matching
To analyze film ratings from a diversity perspective, the dataset is split into two groups: films with a diverse cast (number of ethnicities higher than 2 among actors) and films with a non-diverse cast. We then use a paired matching approach to compare the ratings of the two groups to see if movies with diverse cast are generally rated higher. Logistic regression is performed for propensity matching on all other relevant attributes. Similarly, the analysis is done for the other diversity features of interest: gender and languages. 

## Executed Timeline ⏳
```
.
├── November 17, 2023: Deadline for Milestone 2
├── December 1, 2023: Homework 2 Deadline
├── December 10, 2023: Create an initial draft for the data story
├── December 15, 2023: Complete the code implementations and visualizations for each part of the datastroy
├── December 18, 2023: Merging individual parts, first draft of the data story
├── December 20, 2023: Finalize the data story
├── December 22, 2023: Deadline for Milestone 3
.

```

## Organization within the team for Milestone 3 
Imane: Contribution to Topic Analysis

Xiyu: Genres and movies duration analysis 

Zach: Carrying out analysis around impact on ratings by cast ethnic, gender and linguistic diversity, Website layout and UI

Antoine: Actors' related analysis

Lina: Carrying out analysis around topics



