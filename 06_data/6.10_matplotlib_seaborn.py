import pandas as pd

df_sales = pd.read_excel("linechart.xlsx")
df_sales.head

from matplotlib import pyplot as plt
print(plt.plot(df_sales["Quarter"], df_sales["Fridge"]))
print(plt.plot(df_sales["Quarter"], df_sales["Dishwasher"]))
print(plt.plot(df_sales["Quarter"], df_sales["Washing Machine"]))

plt.title("Product Sales") #adds title to the graph
plt.ylabel("Revenue mln $") #adds label on the y axis
plt.xlabel("Financial Quarter") #adds label on the x axis
  