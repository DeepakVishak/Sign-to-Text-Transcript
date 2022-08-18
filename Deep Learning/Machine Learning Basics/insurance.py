import pandas as pd
import matplotlib.pyplot as py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

    

df=pd.read_csv('insurance.csv')
print(df)


x_train,x_test,y_train,y_test=train_test_split(df[['age']].values,df.bought_insurance,train_size=0.8)

model = LogisticRegression()
model.fit(x_train,y_train)
print(model.predict(x_test))
print(model.score(x_test,y_test))
print(model.predict_proba(x_test))



py.scatter(df.age,df.bought_insurance,marker='+',color='red')
py.xlabel('Age')
py.ylabel('Insurance')
py.title('Insurance List')
py.show()
