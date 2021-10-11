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
        self.classifier = self.StereotypeInitializor()  
        self.skill = 0

    def  getSkill(self):
        return self.skill
       
    def StereotypeInitializor(self):
        dataset = pd.read_csv('Resources/Student_Level.csv')
        X = dataset.iloc[:, [1, 2, 3, 4, 5, 6]].values
        y = dataset.iloc[:, 7].values

        
        self.le = LabelEncoder()
   
        X[:,1] = self.le.fit_transform(X[:,1])
   
        
        predict_X = self.user_record

        predict_X[1] = self.le.fit_transform([predict_X[1]])[0]
      
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            
      
        self.sc = StandardScaler()
    

        X_train = self.sc.fit_transform(X_train)

        
        predict_X = self.sc.transform([predict_X])[0]
        X_test = self.sc.transform(X_test)
            
        self.classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        self.classifier.fit(X_train, y_train)

        
        y_pred = self.classifier.predict([predict_X])

        return self.classifier
             
            
    def predict(self, data):
        predict_X = self.user_record
        predict_X[0] = data

        predict_X[1] = self.le.fit_transform([predict_X[1]])[0]
 
        predict_X = self.sc.transform([predict_X])[0]
        
        y_pred = self.classifier.predict([predict_X])

        return y_pred[0]