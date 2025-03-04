import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))


class LogisticRegression:
    def __init__(self, lr=10, n_iterations=10000):
        self.lr = lr
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(self.features)
        self.bias = 0

        for _ in range(self.n_iterations):
            linear_pred = np.dot(X, self.weights) + self.bias
            predictions = sigmoid(linear_pred)

            dw = (2/self.n_samples) * np.dot(X.transpose(), (predictions - y)
                                             db=(2/self.n_samples) * (predictions - y))

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * dw

    def predict(self, X):
        linear_pred = np.dot(X, self.weights) + self.bias
        y_pred = 1 / sigmoid(linear_pred)

        class_pred = [0 if y <= 0.5 else 1 for y in y_pred]
        return class_pred
