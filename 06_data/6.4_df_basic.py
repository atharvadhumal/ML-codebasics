import pandas as pd

df = pd.read_csv("movies.csv")
df.head(3)

df.shape #rows anmd column of the csv

df.columns #prints all the columns

print(df.industry.unique()) #check for the industry types in csv file

df.language.unique()
#can be also written as
df['language'].unique()

df.industry.value_counts() #checks for movies count of hollywood and bollywood\
    
df.language.value_counts() #tells movies by languages count

df_new = df[["title", "imdb_rating", "industry"]] #gives only these three columns
print(df_new)

df_2010 = df[df.release_year >=2000] #movies release after year 2000
print(df_2010)

df_btwn = df[(df.release_year >=2000) & (df.release_year<=2010)] #movies releease after 2000 but before 2010
print(df_btwn)

#df[[df.studios=='Marvel Studios']] #prints only movies from marvel studios

desc = df.describe() #all stats like min max etc means all the numerical things
print(desc)

#df[(df.imdb_rating==df.imdb_rating_max()) | (df.imdb_rating==df.imdb_rating_min())] #gives the fuill row of the highest imdb rating movie

age_movie = df['age'] = df['release_year'].apply(lambda x: 2023 - x)
print(age_movie)