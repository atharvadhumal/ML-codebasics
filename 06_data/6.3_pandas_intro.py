import csv

def calculate_rating_stats(data, industry=None):
    ratings = []
    for row in data:
        if row[3] != 'NULL' and (not industry or row[1].strip() == industry):
            ratings.append(float(row[3]))
            

    max_rating = max(ratings)
    min_rating = min(ratings)
    avg_rating = round(sum(ratings) / len(ratings), 2)
    return max_rating, min_rating, avg_rating

with open("movies.csv") as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:]

max_rating, min_rating, avg_rating = calculate_rating_stats(data)
print(f"All records: Min rating = {min_rating}, Max Rating = {max_rating}, Avg Rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Bollywood")
print(f"Bollywood: Min rating = {min_rating}, Max Rating = {max_rating}, Avg rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Hollywood")
print(f"Hollywood: Min Rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

#movies ananlysis using pandas
import pandas as pd

df = pd.read_csv("movies.csv")
#print(df) #prints all the things from csv
print(df.head(2)) #prints 2 rows > from the csv means index 0 and 1 from top

print(df.tail(3)) #prints 3 rows > from the csv : bottom

print(df.sample(4)) #prints 4 rows > from the csv : randomly index

print(df[2:6]) #slicing in dataframe

print(df["imdb_rating"])
#can be done in this way also
print(df.imdb_rating)

print(df.imdb_rating.min(), df.imdb_rating.max(), df.imdb_rating.mean())

df_h = df[df.industry=="Hollywood"]
print(df_h)