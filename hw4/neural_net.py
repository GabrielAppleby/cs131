import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin


class NeuralNet(BaseEstimator, ClassifierMixin):
    """
    A bare bones inflexible neural network classifier.
    """

    def __init__(self):
        """
        Initializes the weights and intermediate outputs to None. Also sets the
        alpha (learning rate), and the number of iterations.
        """
        self.__weights1: np.array = None
        self.__weights2: np.array = None
        self.__hidden_layer: np.array = None
        self.__output_layer: np.array = None
        self.__alpha: float = .01
        self.__iterations: int = 10000

    def fit(self, x: np.array, y: np.array) -> None:
        """
        Fits the neural network using the given dataset.
        :param x: The array of feature values.
        :param y: The array of labels.
        :return: Nothing
        """
        x, y = NeuralNet.__preproccess(x, y)
        self.__weights1 = np.random.rand(x.shape[1], 4)
        self.__weights2 = np.random.rand(4, 3)
        for i in range(self.__iterations):  # type: int
            y_hat: np.array = self.__inner_predict(x)
            d_error_mul_sigmoid_output: np.array = \
                NeuralNet.__deriv_of_error(y, y_hat) *\
                NeuralNet.__deriv_of_sigmoid(self.__output_layer)
            d_weights2: np.array = \
                np.dot(
                    self.__hidden_layer.T,
                    d_error_mul_sigmoid_output)
            d_weights1: np.array = \
                np.dot(x.T,
                       (np.dot(d_error_mul_sigmoid_output, self.__weights2.T) *
                        NeuralNet.__deriv_of_sigmoid(self.__hidden_layer)))
            self.__weights1 += self.__alpha * d_weights1
            self.__weights2 += self.__alpha * d_weights2

    def predict(self, x: np.array):
        """
        Makes a prediction given an array of feature values. Do not call before
        calling predict.
        :param x: The array of feature values, which require a prediction.
        :return: The predicted labels.
        """
        x = NeuralNet.__preprocess_x(x)
        return self.__inner_predict(x)

    def score(self, x: np.array, y: np.array, sample_weight=None):
        """
        Makes a prediction using the array of feature values, then calculates
        the accuracy of the prediction using the array of corresponding labels.
        :param x: The array of feature values.
        :param y: The array of corresponding labels.
        :param sample_weight: Ignored.
        :return: The accuracy of the predictions this classifier makes using
        the given feature values.
        """
        y = self.__preproccess_y(y)
        raw_predictions: np.array = self.predict(x)
        highest_activity = np.argmax(raw_predictions, axis=1)
        y_hat = np.zeros(raw_predictions.shape)
        y_hat[np.arange(y_hat.shape[0]), highest_activity] = 1
        num_correct_predictions: np.array = np.sum((y == y_hat).all(axis=1))
        return num_correct_predictions / x.shape[0]

    def __inner_predict(self, x: np.array) -> np.array:
        """
        Makes a prediction given an array of feature values. Do not call before
        calling predict. This function assumes the x array has already been
        preprocessed.
        :param x: The array of feature values, which require a prediction.
        :return: The predicted labels.
        """
        self.__hidden_layer = NeuralNet.__sigmoid(np.dot(x, self.__weights1))
        self.__output_layer = NeuralNet.__sigmoid(
            np.dot(self.__hidden_layer, self.__weights2))
        return self.__output_layer

    @staticmethod
    def __preproccess(x: np.array, y: np.array):
        """
        Preprocesses the data.
        :param x: The array of feature values to preprocess.
        :param y: The array of labels to preprocess.
        :return: The preprocessed data.
        """
        return NeuralNet.__preprocess_x(x), NeuralNet.__preproccess_y(y)

    @staticmethod
    def __preproccess_y(y: np.array):
        """
        Preprocesses the labels by turning them into dummy variables for each
        category.
        :param y: The array of labels to preprocess.
        :return: The array of dummy variables.
        """
        return pd.get_dummies(y).values

    @staticmethod
    def __preprocess_x(x: np.array):
        """
        Preprocesses the feature values by appending an array of ones to
        represent the bias.
        :param x: The array of feature values to append the column of ones to.
        :return: The array of feature values with the column of ones for bias.
        """
        return np.append(x, np.ones((x.shape[0], 1)), axis=1)

    @staticmethod
    def __sigmoid(x: np.array):
        """
        The sigmoid function.
        :param x: The array to perform element-wise sigmoid on.
        :return: The array after being passed through the sigmoid function.
        """
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def __deriv_of_sigmoid(sigmoid_of_x: np.array):
        """
        The derivative of the sigmoid function.
        :param sigmoid_of_x: The array to perform element-wise sigmoid
        derivative one.
        :return: The array after being passed through the derivative of the
        sigmoid function.
        """
        return sigmoid_of_x * (1 - sigmoid_of_x)

    @staticmethod
    def error_function(y: np.array, y_hat: np.array):
        """
        The error function.
        :param y: The actual labels of the instances.
        :param y_hat: The predicted labels of the instances.
        :return: The sum of the actual minus predicted squared and divided by
        2.
        """
        return np.sum(((y - y_hat) ** 2) / 2)

    @staticmethod
    def __deriv_of_error(y: np.array, y_hat: np.array):
        """
        The derivative of the error function.
        :param y: The actual labels of the instances.
        :param y_hat: THe predicted labels of the instances.
        :return: The difference between the actual and the predicted.
        """
        return y - y_hat
