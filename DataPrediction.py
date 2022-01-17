import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('C:/Users/patel/Downloads/manhattan.csv')

df = pd.DataFrame(data)

df.head()

y = df['rent']

y.head()

x = df[['bathrooms', 'size_sqft', 'floor', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

x.head()

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size = 0.8, test_size = 0.2, random_state = 6)

mlr = LinearRegression()

mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

print(y_predict)

print(y_test)

x_axis = y_test

y_axis = y_predict

plt.scatter(x_axis, y_axis, alpha = 0.4)

guy1 = [[1, 620, 1, 3, 1, 1, 1, 1, 0, 1, 1]]                 #CODE FOR DATA PREDICTION BASED ON INFO ABOVE

guy1_predict = mlr.predict(guy1)                             #CODE FOR DATA PREDICTION BASED ON INFO ABOVE

print('guy1_predict =', guy1_predict)                        #CODE FOR DATA PREDICTION BASED ON INFO ABOVE
