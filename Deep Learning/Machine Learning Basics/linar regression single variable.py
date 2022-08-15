import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model



df = pd.read_csv("area_price.csv")
print(df)
"""
plt.scatter(df.area,df.price,color='red',marker='+')
plt.xlabel('Area(sqr ft)')
plt.ylabel('Price(in USD)')
plt.title('Area and Price Graph')
plt.show()

"""

reg = linear_model.LinearRegression()
area=df[['area']].values
price=df.price
#print(area)
#print(price)
reg.fit(area,price)
print(reg.predict([[3300]]))
"""
#y=mx+b
#where
#m is slope
#x and y are x and y coefficient (x:area,y:price)
#b is y intercept

print(reg.coef_) #gives slope
print(reg.intercept_) #gives intercept

#y=m*x+b
print(reg.coef_ * 3300 + reg.intercept_)
"""

d = pd.read_csv("areas.csv")
print(d)
print(d.head(3))
print(reg.predict(d))
d['prices'] = reg.predict(d)
d.to_csv("prediction.csv",index=False)

plt.scatter(df.area,df.price,color='red',marker='+')
plt.xlabel('Area(sqr ft)')
plt.ylabel('Price(in USD)')
plt.title('Area and Price Graph')
plt.plot(df.area,reg.predict(df[['area']].values),color='blue')
plt.show()

