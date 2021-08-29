import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score



class KNearestNeighbour:
    def __init__(self):
        self.stereotypeModel = self.StereotypeInitializor()    
       
    def StereotypeInitializor(self):
        dataset = pd.read_csv('Resources/Social_Network_Ads.csv')
        X = dataset.iloc[:, [1, 2, 3, 4, 5]].values
        y = dataset.iloc[:, 6].values
            
            
        print(X)
        print(y)
        le = LabelEncoder()
        X[:,0] = le.fit_transform(X[:,0])
        X[:,0] = le.fit_transform(X[:,3])
            
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
            
        classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        classifier.fit(X_train, y_train)
            
        y_pred = classifier.predict(X_test)
            
            
        cm = confusion_matrix(y_test, y_pred)
        ac = accuracy_score(y_test,y_pred)
            
        print(cm)
        print(ac)        
            
            
   