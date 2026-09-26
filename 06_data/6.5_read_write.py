import pandas as pd

# df = pd.read_csv("stock_data.csv", skiprows=1) #can skip row how much ever rows we want l;ike 2 3
# print(df)

# #can be also done using header
# df = pd.read_csv("stock_data.csv", header=1) #can skip row how much ever rows we want l;ike 2 3
# print(df)

# df = pd.read_csv("stock_data.csv", header=1, names=["stock_symol", "eps", "revenue", "price", "people"]) #we can change the names of the column
# print(df)

# df = pd.read_csv("stock_data.csv", header=1, nrows=2) #only rows we want to access
# print(df)

# df = pd.read_csv("stock_data.csv", header=1 , na_values={
#     'eps': ["not available"], 
#     'revenue': [-1],
#     'people':['not available', 'n.a']
#     }) #using na_values we can put NaN to not avaiable values
# print(df)

# df = pd.read_csv("stock_data.csv", header=1 , na_values=['not available', -1, 'n.a.']) #using na_values we can put NaN to not avaiable values
# print(df)

# df['pe'] = df['price']/df['eps'] #price to earning ratio
# print(df)


#reading excel files
df_movies = pd.read_excel("movies_db.xlsx", "movies") #movies is a page in excel sheet
print(df_movies.head(4))

df_movies = pd.read_excel("movies_db.xlsx", "financials")
print(df_movies.head(5))