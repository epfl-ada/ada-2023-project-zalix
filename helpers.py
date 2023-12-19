# imports
import os
import ast
import math
import json
import requests
import numpy as np
import pandas as pd
import networkx as nx
import seaborn as sns
import ipywidgets as widgets

import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


from scipy import stats
from datetime import datetime as dt
from ipywidgets import interact, interactive, fixed, interact_manual

from IPython.display import HTML
from statsmodels.stats.multicomp import pairwise_tukeyhsd



def import_movies_data(data_path):
    colnames_movies = [
    "wikipedia_movie_ID",
    "freebase_movie_ID",
    "movie_name",
    "movie_release_date",
    "movie_box_office_revenue",
    "movie_runtime",
    "movie_languages",
    "movie_countries",
    "movie_genres",
]

    colnames_character = [
        "wikipedia_movie_ID",
        "freebase_movie_ID",
        "last_update",
        "character_name",
        "actor_DOB",
        "actor_gender",
        "actor_height",
        "actor_ethnicity",
        "actor_name",
        "actor_age_at_movie_release",
        "freebase_character/actor_map_ID",
        "freebase_character_ID",
        "freebase_actor_ID",
    ]




    movies = pd.read_csv(data_path+"/CMU/movie.metadata.tsv",sep="\t",names=colnames_movies,header=None)

    characters = pd.read_csv(
        data_path+"/CMU/character.metadata.tsv", sep="\t", names=colnames_character, header=None
    )



    imdb_movies = pd.read_table(
        data_path+"/IMDB/title.basics.tsv",
        sep="\t",
        usecols=["tconst", "originalTitle", "startYear", "runtimeMinutes"],
    )
    imdb_ratings = pd.read_table(data_path+"/IMDB/title.ratings.tsv", sep="\t")
    movies["year_released"] = pd.to_datetime(
    movies["movie_release_date"], infer_datetime_format=True, errors="coerce"
    ).dt.year


    movies = movies[~movies["year_released"].isna()]

    imdb_movies = imdb_movies.rename(

        columns={
            "startYear": "year_released",
            "originalTitle": "movie_name",
            "runtimeMinutes": "movie_runtime",
        }
    )

    # converting '\\N' values to np.nan

    imdb_movies.loc[imdb_movies["year_released"] == "\\N", "year_released"] = np.nan
    imdb_movies.loc[imdb_movies["movie_runtime"] == "\\N", "movie_runtime"] = np.nan

    # removing all rows containing np.nan
    imdb_movies = imdb_movies[imdb_movies["year_released"].notna()]


    # converting year released to 'int64'
    movies["year_released"] = movies["year_released"].astype("int64")
    imdb_movies["year_released"] = imdb_movies["year_released"].astype("int64")

    # converting runtime to 'float64'
    imdb_movies["movie_runtime"] = imdb_movies["movie_runtime"].astype(
        "float64", errors="ignore"
    )


    # removing rows with duplicate of ('movie_name', 'release_year', 'movie_runtime') in movies
    movies = movies.drop_duplicates(subset=["movie_name", "year_released", "movie_runtime"])
    imdb_movies = imdb_movies.drop_duplicates(
        subset=["movie_name", "year_released", "movie_runtime"]
    )



    # merge 'imdb_movies' with 'imdb_ratings'
    imdb_movies = pd.merge(left=imdb_movies, right=imdb_ratings, on="tconst")

    # merge 'movies' with 'imdb_movies' + 'imdb_ratings'
    movies = pd.merge(
        left=movies,
        right=imdb_movies,
        how="left",
        on=["movie_name", "year_released", "movie_runtime"],
    )


    # filtering out movies without rating and 
    movies = movies[~movies["averageRating"].isna()]
    
    #plot summary
    
    plot_summaries = pd.read_csv(data_path+"CMU/plot_summaries.txt", sep="\t", header=None)
    plot_summaries = plot_summaries.rename(columns={0: "MovieID", 1: "PlotSummary"})
    plot_summaries = plot_summaries.dropna(subset=['PlotSummary'])


    return movies,characters,plot_summaries
