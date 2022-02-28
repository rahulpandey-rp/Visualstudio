from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(
    '/home/rahul/Visualstudio/Bootcamp_2021/Datascience/LinearRegression/Salary_Data.csv')

plt.figure(figsize=(12,6))
plt.scatter(dataset['YearsExperience'],dataset['Salary'])
plt.xlabel('Years')
plt.ylabel('Salary')
plt.title('Salary Prediction')
plt.show()


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, model.predict(X_train), color='blue')
plt.title('Experience vs Salary')
plt.xlabel('Experience in years')
plt.ylabel('Salary')
plt.show()

coef = model.coef_
inter = model.intercept_
print(coef, inter)