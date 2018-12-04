import numpy as np
import pandas as pd

from typing import Tuple
from neural_net import NeuralNet
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline


def main():
    x: np.array
    y: np.array
    x, y = read_in_data()

    pipeline: Pipeline = make_pipeline(
        StandardScaler(), NeuralNet())

    scores: np.array = cross_validate(pipeline, x, y=y, cv=5, return_train_score=True)
    print("Train score: " + str(np.mean(scores['train_score'])))
    print("Test score: " + str(np.mean(scores['test_score'])))


def read_in_data() -> Tuple[np.array, np.array]:
    """
    Reads in the iris dataset and splits it into features and labels.
    :return: A tuple where the first element is the array of feature values,
    and the second element is the array of labels.
    """
    df: pd.DataFrame = pd.read_csv('resources/iris.csv',
                                   names=['sepal length',
                                          'sepal width',
                                          'petal length',
                                          'petal width',
                                          'label'])
    x: np.array = df.iloc[:, 0:4].values
    y: np.array = df.iloc[:, 4].values
    return x, y


if __name__ == "__main__":
    main()
