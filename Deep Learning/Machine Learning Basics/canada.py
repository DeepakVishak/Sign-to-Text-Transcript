import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


reg = linear_model.LinearRegression()
year=df[['year']].values
pci=df.pci
#print(area)
#print(price)
reg.fit(year,pci)
print(reg.predict([[2022]]))


df = pd.read_csv('canada.csv')
plt.scatter(df.year,df.pci,color='red',marker='+')
plt.xlabel('Year')
plt.ylabel('Per capita income(in USD)')
plt.title('Year and Per Capita income of Canada Graph')
plt.plot(df.year,reg.predict(df[['year']].values),color='green')
plt.show()


