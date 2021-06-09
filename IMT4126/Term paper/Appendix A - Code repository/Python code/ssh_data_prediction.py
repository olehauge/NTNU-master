import pandas as pd
import mglearn
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import precision_recall_fscore_support

RANDOM_STATE = 42

# Data preparation
col_names = [f"interval_{i}" for i in range(1, 11)]

# Read CSV-data and convert to DF
file = "ML_SSH_data_v3.csv"
df = pd.read_csv(file, names=col_names)
df.head()

# Create a scatter matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(df, c=list(df.index), figsize=(6, 6), marker='o', hist_kwds={'bins':20}, s=6, alpha=.8, cmap=mglearn.cm3)
plt.show()
# Not really necessary to store the plot in a variable, it's just to suppress the output.

# Splitting into input and target variables
X = df[df.columns]
y = df.index

# Splitting into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=RANDOM_STATE)
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

### ML Models ###

# KNN Model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
score = knn.score(X_test, y_test)
print(f"KNN score: {score:.3}")

# SVC model
# Find best C value using gridsearch
c_values = np.logspace(-2, 2, 20)
grid = GridSearchCV(estimator=SVC(), param_grid={"C":c_values})
grid.fit(X_train, y_train)
print("Best C =", grid.best_estimator_.C)

svc = SVC(C=grid.best_estimator_.C)
svc.fit(X_train, y_train)
score = svc.score(X_test, y_test)
print(f"Final SVC score: {score:.3}")

# Create confusion matrix from test-results of KNN
class_names = y.unique()
y_predict = knn.predict(X_test)
cm = confusion_matrix(y_test, y_predict, class_names, normalize="true")

f1score = precision_recall_fscore_support(y_test, y_predict, average='macro')
print(f"Final KNN f1score: {f1score}")

df_cm = pd.DataFrame(cm)
sns.set(font_scale=1.4) # for label size
sns.heatmap(df_cm, annot=True, annot_kws={"size": 16}, xticklabels=y.unique(), yticklabels=y.unique())  # font size
plt.show()

# Create confusion matrix from test-results for SVC
class_names = y.unique()
y_predict = svc.predict(X_test)
cm = confusion_matrix(y_test, y_predict, labels=class_names, normalize="true")

df_cm = pd.DataFrame(cm)
sns.set(font_scale=1.4) # for label size
sns.heatmap(df_cm, annot=True, annot_kws={"size": 16}, xticklabels=y.unique(), yticklabels=y.unique())  # font size
plt.show()

f1score = precision_recall_fscore_support(y_test, y_predict, average='macro')
print(f"Final SVC f1score: {f1score}")
