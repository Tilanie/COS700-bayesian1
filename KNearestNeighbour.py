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
    def __init__(self, user_record):
        self.user_record = user_record
        self.skill = self.StereotypeInitializor()  

    def  getSkill(self):
        return self.skill
       
    def StereotypeInitializor(self):
        dataset = pd.read_csv('Resources/Student_Level.csv')
        X = dataset.iloc[:, [1, 2, 3, 4, 5, 6]].values
        y = dataset.iloc[:, 7].values

        
        le = LabelEncoder()
   
        X[:,1] = le.fit_transform(X[:,1])
        # X[:,0] = le.fit_transform(X[:,3])
            
        
        predict_X = self.user_record
        print("self.user_record")
        print(self.user_record)

        predict_X[1] = le.fit_transform([predict_X[1]])[0]
        # predict_X[0] = le.fit_transform([predict_X[3]])[0]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            
      
        sc = StandardScaler()
    

        X_train = sc.fit_transform(X_train)

        
        predict_X = sc.transform([predict_X])[0]
        X_test = sc.transform(X_test)
            
        classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        classifier.fit(X_train, y_train)
            
        y_pred = classifier.predict([predict_X])

        print("--------")
        print(predict_X)  
        print(y_pred[0])
        return y_pred[0]
        # print(cm)
        # print(ac)        
            
    def predict(self, predict_x):
        pass
            
   