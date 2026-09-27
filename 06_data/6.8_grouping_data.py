import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df)

df[df.city=="new york"].temperature.max() #gives max temp in new york

g = df.groupby("city")
for city, data in g:
    print("city", city)
    print("/n")
    print("data", data.temperature.max())
    
g.max() #max temperature all city wise