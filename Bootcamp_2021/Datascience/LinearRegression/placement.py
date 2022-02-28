from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(
    'LinearRegression/placement.csv')

plt.figure(figsize=(9, 8))
plt.scatter(dataset['cgpa'], dataset['package'])
plt.xlabel('CGPA')
plt.ylabel('Package (LPA)')


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(9, 8))
plt.scatter(dataset['cgpa'], dataset['package'])
plt.plot(X_train, model.predict(X_train), color='red')
plt.xlabel('CGPA')
plt.ylabel('Package (LPA)')
plt.show()

coef = model.coef_
inter = model.intercept_
print(coef, inter)
