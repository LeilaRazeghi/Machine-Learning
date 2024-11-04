import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv


class LinearLeastSquare:
    def __init__(self):
        self.w = None
        self.w = self.w

    def fit(self,X_train,Y_train):
        #self.w=inv(X_train.T @ X_train)@ X_train.T @ Y_train
        self.w = np.linalg.pinv(X_train.T @ X_train) @ X_train.T @ Y_train
        if self.w.ndim == 1:
          self.w = self.w.reshape(-1, 1)
        return self.w


    def predict(self,X_test):
        Y_pred = np.dot(X_test, self.w)
        Y_pred= X_test@ self.w
        return Y_pred
    
    def evaluate(self,Y_test,Y_pred,metric):
        if metric== "mae":
            loss = np.sum(np.abs(Y_test-Y_pred))/len(Y_test)
        elif metric == "mse":
            loss = np.sum((Y_test-Y_pred)**2)/len(Y_test)
        elif metric == "rmse":
            loss = np.sqrt(np.sum((Y_test-Y_pred)**2)/len(Y_test))
        return loss