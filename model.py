from sklearn.ensemble import RandomForestClassifier


class Model:

    model = None

    # Create a random forest Classifier.
    def build_model(self, train, target):
        global model
        model = RandomForestClassifier(n_jobs=1, random_state=0)
        model.fit(train, target)

    # Predict using our model, return the answer as list
    def predict(self, test):
        global model
        return model.predict(test).tolist()

    # predict the probability to each classification using our model
    def predict_proba(self, dataset):
        global model
        return model.predict_proba(dataset)

    def is_inited(self):
        return model is not None

    # Remove the model
    @staticmethod
    def del_model():
        global model
        model = None
