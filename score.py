import io
import pickle
import argparse
import numpy as np
import pandas as pd

from azureml.core.model import Model
#from sklearn.linear_model import LogisticRegression

from azureml_user.parallel_run import EntryScript
from sklearn.metrics import confusion_matrix

def init():
    global best_model

    logger = EntryScript().logger
    logger.info("init() is called.")

    parser = argparse.ArgumentParser(description="score")
    parser.add_argument('--model_name', dest="model_name", required=True)
    args, unknown_args = parser.parse_known_args()

    model_path = Model.get_model_path(args.model_name)
    print(model_path)
    best_model = joblib.load(model_path)
    '''
    with open(model_path, 'rb') as model_file:
        best_model = pickle.load(model_file)

    '''


def run(input_data):
    logger = EntryScript().logger
    logger.info("run() is called with: {}.".format(input_data))

    df_test = input_data.to_pandas_dataframe()
    df_test = df_test[pd.notnull(df_test['y'])]

    y_test = df_test['y']
    X_test = df_test.drop(['y'], axis=1)
    
    ypred = best_model.predict(X_test)
    cm = confusion_matrix(y_test, ypred)

    return cm;

