import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

dataset = pd.read_csv(
    'LogisticRegression/Social_Network_Ads.csv')

# dataset.isnull().sum()

X = dataset[['Age', 'EstimatedSalary']]
Y = dataset['Purchased']


sc = StandardScaler()
X = sc.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

model.score(X_test, y_test)
score = accuracy_score(y_test, y_pred)
cf_matrix = confusion_matrix(y_test, y_pred)
print(cf_matrix)


def plot(X, y, mset):
    p = ['Not Purchased', 'Purchased']
    X1, X2 = np.meshgrid(np.arange(start=X[:, 0].min() - 1, stop=X[:, 0].max() + 1,   step=0.01),
                         np.arange(start=X[:, 1].min() - 1, stop=X[:, 1].max() + 1, step=0.01))

    # To plot boundaries
    # In general, the space is divided into decision boundaries
    plt.figure(figsize=(8, 6))
    plt.contourf(X1, X2, model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('#F1674F', '#BEDDB7')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())

    for i, j in enumerate(set(y)):
        plt.scatter(X[y == j, 0], X[y == j, 1],
                    c=['#F84C51', '#23807A'][i], label=p[j])
    plt.title('Logistic Regression ('+mset+')')
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()


y_pred = model.predict(X_train)
plot(X_train, y_pred, 'Training Set')

y_pred = model.predict(X_test)
plt.show(plot(X_test, y_pred, 'Test Set'))


'''we scale the values using standardscaler, this is done for better model performance , The mean should be near to 0 and standard deviation should be near 1 before training the model which is ensured by this.'''
