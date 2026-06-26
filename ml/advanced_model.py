from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def train_models(X, y):
    models = {
        "SVM": SVC(kernel='rbf', C=10, gamma='scale', probability=True),
        "RandomForest": RandomForestClassifier(n_estimators=200),
        "LogisticRegression": LogisticRegression(max_iter=1000)
    }

    trained = {}

    for name, model in models.items():
        model.fit(X, y)
        trained[name] = model

    return trained