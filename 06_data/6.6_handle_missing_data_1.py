import pandas as pd

df = pd.read_csv("weather_data.csv", parse_dates=["day"])
print(df)

#df.fillna(0, inplace=True) #replces null values with 0

df.fillna({
    'temperate': df.temperate.mean(), #where ever zero is present it will have mean
    'windspeed': df.windspeed.mean()
})

df.fillna(method="ffill") #based on prev value NaN values are set
df.fillna(method="bfill") #based on below value the upper NaN values are set

df.dropna() #any row which will have a single NaN will be dropped