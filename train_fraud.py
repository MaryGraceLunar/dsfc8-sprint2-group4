from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

df = pd.read_csv('fraud_data_features.csv')
X = xgdf_sample.iloc[:, xgdf.columns != 'is_fraud']
y = xgdf_sample.is_fraud
columns = X.columns.tolist()

decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2)
decision_tree = decision_tree.fit(X, y)

r = export_text(decision_tree, feature_names=columns)
print(r)

from joblib import dump

dump(decision_tree, "model.joblib")
