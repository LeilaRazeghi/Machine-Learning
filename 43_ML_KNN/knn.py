import numpy as np 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class KNN :
    def __init__(self , k ) :
        self.k = k 

    # KNN training stage 
    def fit(self , X , Y): 
        self.X_train = X
        self.Y_train = Y


    # predict & GIVE NEW FRUIT label (y), gets fruits FEATURE
  
    def predict(self , list_of_new_datas): 
        Y_list = []
        for x in list_of_new_datas :
            
            distances = []
            for x_train in self.X_train :
                d = self.euclidean_distance(x , x_train) # euclidean_distance between new data & each of the TRAIN DATA
                distances.append(d)

            nearest_neighbour = np.argsort(distances)[0 : self.k]
            result = np.bincount(self.Y_train[nearest_neighbour])
            y = np.argmax(result)
            Y_list.append(y)

            
        # we must return a list of y's ,, not only a one y 
        return Y_list 



    def euclidean_distance(self , x1 , x2) :
        return np.sqrt(np.sum((x1 - x2)**2 ))
    
    # goal = comparing  our answers ,, with their true results 
    def evaluate(self , X , Y ) : 

        Y_predicted = self.predict(X)     # our answers     # COMPARE ((( Y == real answer))) and  (((( Y_predicted == our prediction)))
        accuracy = np.sum(Y_predicted == Y)  / len(Y)               # CHECK "how many" of (((Y_predicted))) are equal to  (((( Y ))))
        return accuracy
    


if __name__ == "__main__" :

    iris = load_iris()
    X = iris.data   # features of flowers
    Y = iris.target 

    print(X.shape)
    print(Y.shape)
  
    # split dataset 
    X_train , X_test , Y_train , Y_test = train_test_split(X , Y  , test_size= 0.2 ) # each time split randomly 

    print("x , y train :" , X_train.shape , Y_train.shape)
    print("x , y test: " , X_test.shape , Y_test.shape)

    # create object from above KNN class
    knn = KNN(3)
    # fit on train data
    knn.fit(X_train , Y_train)
    # give test data to evaluate function
    accuracy = knn.evaluate(X_test , Y_test)
    print("accuracy" , accuracy)


    knn_sklearn = KNeighborsClassifier(n_neighbors=3)
    knn_sklearn.fit(X_train , Y_train)
    accuracy_sklearn = knn_sklearn.score(X_test , Y_test)
    print(accuracy_sklearn)