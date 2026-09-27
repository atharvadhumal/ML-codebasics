import pandas as pd

df = pd.read_csv("weather_data.csv")
print(df)

import numpy as np
df.replace(-99999, np.nan) #replaces -99999 values with nan

df.replace({ #when there are many values
    -99999: np.nan,
    -88888: np.nan,
    'no event': 'Sunny'
})