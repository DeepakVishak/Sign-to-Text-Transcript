import pandas as pd
import numpy as np
from sklearn import linear_model
from text_to_num import text2num

df = pd.read_csv('hiring.csv')
print(df)

print(df.test_score.median())
df.experience = df.experience.fillna('zero')
df.test_score = df.test_score.fillna(df.test_score.median())
df.experience = df.experience.apply(text2num,lang="en")
print(df)

reg = linear_model.LinearRegression()

source=df[['experience','test_score','interview_score']].values
target=df.salary
reg.fit(source,target)
print(reg.coef_)
print(reg.intercept_)

#Predict the salary of the following

#2yr experience,9 test score,6 interview score
print(reg.predict([[2,9,6]]))

#12yr experience,10 test score,10 interview score
print(reg.predict([[12,10,10]]))
