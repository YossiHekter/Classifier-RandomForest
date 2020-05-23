import difflib
import threading

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
from popup import *
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn
from model import Model


my_model = None


def train_model():
    global my_model
    error = False
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
            error = True

        if len(dataset) < 10:
            popup_msg("The file must contains a minimum of 10 records!")
        elif not error:
            accuracy = 0

            # Display progress bar while the model training
            progress_bar_thread = threading.Thread(target=bar)
            progress_bar_thread.start()

            # Create a random forest Classifier.
            # To avoid over fitting or bad classifier we make sure the accurancy of the model is between 0.7-0.9
            while accuracy < 0.7 or accuracy > 0.9:

                # Divide the data to train and test porto ratio (80-20)
                dataset['is_train'] = np.random.uniform(0, 1, len(dataset)) <= 0.8
                train, test = dataset[dataset['is_train'] == 1], dataset[dataset['is_train'] == 0]

                # Covert the target to  0, 1, or 2.
                target = pd.factorize(train['target'])[0]

                # Create a list of the feature column's
                features = dataset.columns[2:26]

                # build the model
                real = normalize_value(test["target"])
                my_model = Model()
                my_model.build_model(train[features], target)
                predict = my_model.predict(test[features])
                sm = difflib.SequenceMatcher(None, real, predict)
                accuracy = sm.ratio()

            progress_bar_thread.join()

            # Create confusion matrix
            conf_mat = confusion_matrix(real, predict)
            df_cm = pd.DataFrame(conf_mat, range(3), range(3))
            sn.set(font_scale=1.4)  # for label size
            sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})  # font size
            plt.show()

            # Present the accuracy
            model_accuracy(str("%.3f" % accuracy))


def classifier_function():
    global my_model
    error = False
    # read the file
    Tk().withdraw()
    filename = askopenfilename()
    if filename == '' or not filename.endswith('csv'):
        popup_msg("Please try again and choose a csv file!")
    else:
        dataset = pd.read_csv(filename)

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
            error = True

        # Create a list of the feature column's names
        features = dataset.columns[2:26]

        if not error and my_model is not None and my_model.is_inited():

            # Apply the Classifier we trained to the test data (which, remember, it has never seen before)
            predict = my_model.predict_proba(dataset[features])
            list_prob_0 = []
            list_prob_1 = []
            list_prob_2 = []
            for index in range(len(predict - 1)):
                list_prob_0.append("%.2f" % predict[index][0])
                list_prob_1.append("%.2f" % predict[index][1])
                list_prob_2.append("%.2f" % predict[index][2])
            dataset["Guide dog"] = list_prob_0
            dataset["Disabled"] = list_prob_1
            dataset["Traumatized"] = list_prob_2
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
