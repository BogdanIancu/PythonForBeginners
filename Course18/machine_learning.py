import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import joblib

# movie_data = pd.read_csv("cleared_data.csv")
#
# X = movie_data.drop(columns=["movie_name"])
# y = movie_data["movie_name"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# model = DecisionTreeClassifier()
# model.fit(X_train.values, y_train)
# predictions = model.predict(X_test.values)
# score = accuracy_score(y_test, predictions)
# print(score)

# joblib.dump(model, "movie_recommender.joblib")
model = joblib.load("movie_recommender.joblib")
predictions = model.predict([[32, 1, 19, 8], [25, 0, 17, 9]])
print(predictions)

# tree.export_graphviz(model, "movie_recommender.dot",
#                      feature_names=["age", "gender", "hour", "IMDB_rating"],
#                      label="all", rounded=True, filled=True)


