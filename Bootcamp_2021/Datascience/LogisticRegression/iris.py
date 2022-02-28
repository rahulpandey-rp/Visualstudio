from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from matplotlib.colors import ListedColormap


iris = datasets.load_iris()
X = iris["data"][:, 3:]
y = (iris["target"] == 2).astype(np.int32)

model = LogisticRegression()
model.fit(X, y)
#example = model.predict(([[2.6]]))
#print(example)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_prob = model.predict_proba(X_new)
y_pred = model.predict(X_new)
plt.scatter(X, y)
plt.plot(X_new, y_prob[:, 1], "g-")
plt.show()
