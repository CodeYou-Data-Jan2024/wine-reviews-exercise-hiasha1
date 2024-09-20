import pandas as pd
import os
wine = pd.read_csv("data\winemag-data-130k-v2.csv")
wine =wine.groupby('country').points.agg(['count',('points','mean')]).sort_values('count',ascending= False)
#print(wine)
wine['points'] = wine.points.round(1)
print(wine)
wine = wine.to_csv("data/reviews-per-country.csv",index = True)