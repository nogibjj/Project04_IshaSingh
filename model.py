import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

dataset = pd.read_csv('/Users/isingh/Desktop/salary.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

dataset.head()
# convert salary to double
dataset['Salary'] = dataset['Salary'].astype(float)
dataset.head()

# get rid of rows that have missing values
dataset.dropna(inplace=True)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#save our object regressor to the file named model.pkl
pickle.dump(regressor, open('model.pkl','wb'))
#load the model from the file
model = pickle.load(open('model.pkl','rb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1.8]]))


logmodel.fit(X_train,y_train)



