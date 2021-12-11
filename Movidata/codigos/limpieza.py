# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import pandas as pd
import numpy as np
import psycopg2
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

start_time = time.time()

naValues=["#ERROR","#NODATA","N/I","N/A","?",]

df = pd.read_excel("moviedata.xlsx", encoding = "utf-8", na_values = naValues)

number_of_rows1 = len(df.index)

listaNan = df.columns[df.isna().any()].tolist() #obtiene una lista con el nombre de las columnas que tienen algun valor NaN

for name in listaNan: #por cada columna
    df[name].fillna(value=np.nan, inplace=True) #reemplazar NaN




df["content_rating"].replace({"?":"Unrated","Approved":"G","GP":"PG","M":"PG","Not Rated":"Unrated","Passed":"PG-13","X":"NC-17"},inplace=True)

df["aspect_ratio"].replace({1.18:1.37, 2.24:2.39, 4:1.33, 16:1.78, 1.77:1.78}, inplace=True)

df["title_year"].replace({0:None},inplace=True)

df["budget"].replace({-1:None},inplace=True)

df["plot_keywords"].replace({None:"Null"},inplace=True)

df["movie_title"] = df['movie_title'].str[:-2]

df = df.dropna(axis=0, subset=["movie_imdb_link"])

df = df.drop_duplicates(subset=["movie_imdb_link"], keep=False)

cantidadNulls = df.isnull().any(axis=1).sum()

number_of_rows2 = len(df.index)

print("Resultado:")
print(df)
print("Cantidad de filas eliminadas:", number_of_rows1 - number_of_rows2)
print("Cantidad de filas con null:", cantidadNulls)

conn = psycopg2.connect(host="localhost",
                        port=5432,
                        user="postgres",
                        password="postgres",
                        database="moviedata")

print("Conectado a la base de datos")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS pelicula cascade")
cursor.execute("DROP TABLE IF EXISTS peliculaGenero cascade")
cursor.execute("DROP TABLE IF EXISTS peliculaKeywords cascade")
cursor.execute("DROP TABLE IF EXISTS personaPeliculaRol cascade")

conn.commit()

######################################

sql ='''CREATE TABLE pelicula(
	color varchar,
	num_critic_for_reviews varchar,
	duration varchar,
	gross varchar,
	movie_title varchar,
	num_voted_users varchar,
	cast_total_facebook_likes varchar,
	facenumber_in_poster varchar,
	movie_imdb_link varchar,
	num_user_for_reviews varchar,
	language varchar,
	country varchar,
	content_rating varchar,
	budget varchar,
	title_year varchar,
	imdb_score float,
	aspect_ratio float,
	movie_facebook_likes varchar,
	primary key(movie_imdb_link)
)'''

cursor.execute(sql)

sql ='''CREATE TABLE peliculaGenero(
	movie_imdb_link varchar,
	genreName varchar,
	primary key(movie_imdb_link, genreName),
	foreign key(movie_imdb_link) references pelicula(movie_imdb_link)
)'''

cursor.execute(sql)

sql ='''CREATE TABLE peliculaKeywords(
	movie_imdb_link varchar,
	plotKeywords varchar,
	primary key(movie_imdb_link, plotKeywords),
	foreign key(movie_imdb_link) references pelicula(movie_imdb_link)
)'''

cursor.execute(sql)

sql ='''CREATE TABLE personaPeliculaRol(
	personName varchar,
	movie_imdb_link varchar,
	roleName varchar,
	facebook_likes varchar,
	primary key(personName, movie_imdb_link, roleName),
	foreign key(movie_imdb_link) references pelicula(movie_imdb_link)
)'''

cursor.execute(sql)

conn.commit()

######################################

df = df.reset_index(drop=True)
dfOriginal = df

######################################

dfPeliculas = df.drop_duplicates(subset=["movie_imdb_link"]) 
dfPeliculas = dfPeliculas.reset_index(drop=True)

dfPeliculas["aspect_ratio"].astype(np.float64)
dfPeliculas["imdb_score"].astype(np.float64)

add_peliculas = "INSERT INTO pelicula (color,num_critic_for_reviews,duration, gross, movie_title, num_voted_users, cast_total_facebook_likes, facenumber_in_poster, movie_imdb_link, num_user_for_reviews, language, country, content_rating, budget, title_year, imdb_score, aspect_ratio, movie_facebook_likes) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) ON CONFLICT DO NOTHING"

for i in dfPeliculas.index:
    data_datosPeliculas = (dfPeliculas["color"].tolist()[i], dfPeliculas["num_critic_for_reviews"].tolist()[i], dfPeliculas["duration"].tolist()[i],
                           dfPeliculas["gross"].tolist()[i], dfPeliculas["movie_title"].tolist()[i], dfPeliculas["num_voted_users"].tolist()[i],
                           dfPeliculas["cast_total_facebook_likes"].tolist()[i], dfPeliculas["facenumber_in_poster"].tolist()[i], dfPeliculas["movie_imdb_link"].tolist()[i],
                           dfPeliculas["num_user_for_reviews"].tolist()[i], dfPeliculas["language"].tolist()[i], dfPeliculas["country"].tolist()[i],
                           dfPeliculas["content_rating"].tolist()[i], dfPeliculas["budget"].tolist()[i], dfPeliculas["title_year"].tolist()[i],
                           dfPeliculas["imdb_score"].tolist()[i], dfPeliculas["aspect_ratio"].tolist()[i], dfPeliculas["movie_facebook_likes"].tolist()[i])
    cursor.execute(add_peliculas, data_datosPeliculas)

print("peliculas OK")


######################################

df = dfOriginal
df = df.reset_index(drop=True)
dfPeliculaGenero = df.drop_duplicates(subset=["movie_imdb_link"])
dfPeliculaGenero = dfPeliculaGenero.reset_index(drop=True)

add_peliculaGenero = "INSERT INTO peliculaGenero (movie_imdb_link, genreName) VALUES(%s, %s) ON CONFLICT DO NOTHING"

for i in dfPeliculaGenero.index:
    #print(i)
    genres = dfPeliculaGenero["genres"].tolist()[i].split("|")
    for j in range(len(genres)):
        #print(genres[j])
        data_peliculaGenero = (dfPeliculaGenero["movie_imdb_link"].tolist()[i], genres[j])
        cursor.execute(add_peliculaGenero, data_peliculaGenero)

print("peliculaGenero OK")

######################################

df = dfOriginal
df = df.reset_index(drop=True)
dfPeliculaKeywords = df.drop_duplicates(subset=["movie_imdb_link"])
dfPeliculaKeywords = dfPeliculaKeywords.reset_index(drop=True)

add_peliculaKeywords = "INSERT INTO peliculaKeywords (movie_imdb_link, plotKeywords) VALUES(%s, %s) ON CONFLICT DO NOTHING"

for i in dfPeliculaKeywords.index:
    words = dfPeliculaKeywords["plot_keywords"].tolist()[i].split("|")
    for j in range(len(words)):
        data_peliculaKeywords = (dfPeliculaKeywords["movie_imdb_link"].tolist()[i], words[j] )
        cursor.execute(add_peliculaKeywords, data_peliculaKeywords)

print("peliculaKeywords OK")

######################################
df = dfOriginal
df = df.reset_index(drop=True)


dfUniqueDirectorNames = df.drop_duplicates(subset=["director_name"])
dfUniqueActor1Names = df.drop_duplicates(subset=["actor_1_name"])
dfUniqueActor2Names = df.drop_duplicates(subset=["actor_2_name"])
dfUniqueActor3Names = df.drop_duplicates(subset=["actor_3_name"])


dfUniqueDirectorNames = dfUniqueDirectorNames.reset_index(drop=True)
dfUniqueActor1Names = dfUniqueActor1Names.reset_index(drop=True)
dfUniqueActor2Names = dfUniqueActor2Names.reset_index(drop=True)
dfUniqueActor3Names = dfUniqueActor3Names.reset_index(drop=True)


add_personaPeliculaRol = "INSERT INTO personaPeliculaRol (personName, movie_imdb_link, roleName, facebook_likes) VALUES(%s, %s, %s, %s) ON CONFLICT DO NOTHING"

for i in dfUniqueDirectorNames.index:
    data_directorPeliculaRol = (dfUniqueDirectorNames["director_name"].tolist()[i], dfUniqueDirectorNames["movie_imdb_link"].tolist()[i],
                               "Director", dfUniqueDirectorNames["director_facebook_likes"].tolist()[i])
    cursor.execute(add_personaPeliculaRol, data_directorPeliculaRol)

for i in dfUniqueActor1Names.index:
    data_actorPeliculaRol = (dfUniqueActor1Names["actor_1_name"].tolist()[i], dfUniqueActor1Names["movie_imdb_link"].tolist()[i],
                               "Actor 1", dfUniqueActor1Names["actor_1_facebook_likes"].tolist()[i])
    cursor.execute(add_personaPeliculaRol, data_actorPeliculaRol)

for i in dfUniqueActor2Names.index:
    data_actorPeliculaRol = (dfUniqueActor2Names["actor_2_name"].tolist()[i], dfUniqueActor2Names["movie_imdb_link"].tolist()[i],
                               "Actor 2", dfUniqueActor2Names["actor_2_facebook_likes"].tolist()[i])
    cursor.execute(add_personaPeliculaRol, data_actorPeliculaRol)

for i in dfUniqueActor3Names.index:
    data_actorPeliculaRol = (dfUniqueActor3Names["actor_3_name"].tolist()[i], dfUniqueActor3Names["movie_imdb_link"].tolist()[i],
                               "Actor 3", dfUniqueActor3Names["actor_3_facebook_likes"].tolist()[i])
    cursor.execute(add_personaPeliculaRol, data_actorPeliculaRol)

print("personaPeliculaRol OK")

######################################

conn.commit()
cursor.close()
conn.close()

print("FIN")
print("--- %s seconds ---" % (time.time() - start_time))



