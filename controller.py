import difflib

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from popup import *
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn

classifier = None


def train_model():
    global classifier
    # read the file
    Tk().withdraw()
    filename = askopenfilename()
    if filename == '' or not filename.endswith('csv'):
        popup_msg("Please try again and choose a csv file!")
    else:
        try:
            dataset = pd.read_csv(filename)
            # Create a data frame with the four feature variables
            dataset.columns = ["dogID", "dogName", "attribute1", "attribute2", "attribute3", "attribute4", "attribute5",
                               "attribute6", "attribute7", "attribute8", "attribute9", "attribute10",
                               "attribute11", "attribute12", "attribute13", "attribute14", "attribute15",
                               "attribute16", "attribute17", "attribute18", "attribute19", "attribute20",
                               "attribute21", "attribute22", "attribute23", "attribute24", "freeText", "date", "target"]
            dataset = dataset.drop(columns=['freeText', 'date'])
        except ValueError:
            popup_format_error("train")

        # View the top 5 rows
        print(dataset.head())

        # Create a new column that for each row, generates a random number between 0 and 1, and
        # if that value is less than or equal to .75, then sets the value of that cell as True
        # and false otherwise. This is a quick and dirty way of randomly assigning some rows to
        # be used as the training data and some as the test data.
        dataset['is_train'] = np.random.uniform(0, 1, len(dataset)) <= 0.8
        train, test = dataset[dataset['is_train'] == 1], dataset[dataset['is_train'] == 0]

        # train['target'] contains the actual classification. Before we can use it,
        # we need to convert each species name into a digit. So, in this case there
        # are three target, which have been coded as 0, 1, or 2.
        target = pd.factorize(train['target'])[0]

        # Create a list of the feature column's
        features = dataset.columns[2:26]

        # Create a random forest Classifier.
        classifier = RandomForestClassifier(n_jobs=2, random_state=0)
        classifier.fit(train[features], target)
        predict = classifier.predict(test[features]).tolist()

        # Create confusion matrix
        real = normalize_value(test["target"])
        conf_mat = confusion_matrix(real, predict)
        df_cm = pd.DataFrame(conf_mat, range(3), range(3))
        sn.set(font_scale=1.4)  # for label size
        sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})  # font size
        plt.show()

        # Measure the accuracy
        sm = difflib.SequenceMatcher(None, real, predict)
        model_accuracy(str("%.3f" % sm.ratio()))



def classifier_function():
    global classifier
    # read the file
    Tk().withdraw()
    filename = askopenfilename()
    if filename == '' or not filename.endswith('csv'):
        popup_msg("Please try again and choose a csv file!")
    else:
        dataset = pd.read_csv(filename)

        if classifier is not None:
            # Create a data frame with the four feature variables
            try:
                dataset = pd.read_csv(filename)
                # Create a data frame with the four feature variables
                dataset.columns = ["dogID", "dogName", "attribute1", "attribute2", "attribute3", "attribute4",
                                   "attribute5",
                                   "attribute6", "attribute7", "attribute8", "attribute9", "attribute10",
                                   "attribute11", "attribute12", "attribute13", "attribute14", "attribute15",
                                   "attribute16", "attribute17", "attribute18", "attribute19", "attribute20",
                                   "attribute21", "attribute22", "attribute23", "attribute24", "freeText", "date"]
                dataset = dataset.drop(columns=['freeText', 'date'])
            except ValueError:
                popup_format_error("classifier")

            # Create a list of the feature column's names
            features = dataset.columns[2:26]

            # Apply the Classifier we trained to the test data (which, remember, it has never seen before)
            predict = classifier.predict_proba(dataset[features])
            list_prob_0 = []
            list_prob_1 = []
            list_prob_2 = []
            for index in range(len(predict - 1)):
                list_prob_0.append("%.2f" % predict[index][0])
                list_prob_1.append("%.2f" % predict[index][1])
                list_prob_2.append("%.2f" % predict[index][2])
            dataset["predict a"] = list_prob_0
            dataset["predict b"] = list_prob_1
            dataset["predict c"] = list_prob_2
            popup_output(dataset)
        else:
            popup_msg("You have to train the model first!")


def normalize_value(target):
    answer = []
    for classification in target:
        if classification == 'a':
            answer.append(0)
        elif classification == 'b':
            answer.append(1)
        else:
            answer.append(2)
    return answer
