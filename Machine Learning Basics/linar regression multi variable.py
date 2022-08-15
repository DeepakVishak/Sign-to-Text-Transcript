import pandas as pd
import numpy as np
from sklearn import linear_model

#call dataframe
df = pd.read_csv('room.csv')
print(df)

#fill missing value of bedrooms
print(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
print(df)

#linear regression for multiple variables
reg = linear_model.LinearRegression()
source=df[['area','bedrooms','age']].values
target=df.price
reg.fit(source,target)
print(reg.coef_)
print(reg.intercept_)
#Predict the prices for the following

#3000 sqrt 3 bedrooms 40 yr old 
print(reg.predict([[3000,3.0,40]]))

#2500 sqrt 4 bedrooms 5 yr old
print(reg.predict([[2500,4.0,5]]))





