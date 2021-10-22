from Concepts import Concepts

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import json
import csv
class NeuralNetwork:
    def __init__(self, id, fuzzy = False):
        self.student_id = id
        self.concepts = []
      
        # load the dataset
        dataset = dataset = pd.read_csv('TestData/studentTestData.csv', delimiter=',')
        # To remove the scientific notation from numpy arrays
        np.set_printoptions(suppress=True)
        
        X=dataset.values[:,0:5]
        y=dataset.values[:,5:6]
        
        ### Sandardization of data ###
        
        PredictorScaler=StandardScaler()
        self.TargetVarScaler=StandardScaler()
       
        # Storing the fit object for later reference
        self.PredictorScalerFit=PredictorScaler.fit(X)
        self.TargetVarScalerFit=self.TargetVarScaler.fit(y)
        
        # Generating the standardized values of X and y
        X=self.PredictorScalerFit.transform(X)
        y=self.TargetVarScalerFit.transform(y)
        
        # Split the data into training and testing set
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
   
        # create ANN model
        self.model = Sequential()
        
        # Defining the Input layer and FIRST hidden layer, both are same!
        self.model.add(Dense(units=5, input_dim=5, kernel_initializer='normal', activation='relu'))
        # Defining the Second layer of the model
        self.model.add(Dense(units=5, kernel_initializer='normal', activation='tanh'))
        
        # Since we will be predicting a single number
        self.model.add(Dense(1, kernel_initializer='normal'))
        
        # Compiling the model
        self.model.compile(loss='mean_squared_error', optimizer='adam')
        
        # Fitting the ANN to the Training set
        self.model.fit(X_train, y_train ,batch_size = 20, epochs = 50, verbose=0)
        Predictions=self.model.predict(X_test)
     
        # Scaling the predicted Price data back to original price scale
        Predictions=self.TargetVarScalerFit.inverse_transform(Predictions)

        # Scaling the y_test Price data back to original price scale
        y_test_orig=self.TargetVarScalerFit.inverse_transform(y_test)
        
        # Scaling the test data back to original scale
        Test_Data=self.PredictorScalerFit.inverse_transform(X_test)
        Predictors = ['test1', 'test2', 'test3', 'concept', 'sequence']
        TestingData=pd.DataFrame(data=Test_Data, columns=Predictors)
        TestingData['Known']=y_test_orig
        TestingData['PredictedKnown']=Predictions

        APE=100*(abs(TestingData['Known']-TestingData['PredictedKnown'])/TestingData['Known'])
        TestingData['APE']=APE
    

        

    def predict(self, value):
        Xnew = np.array([value])
        Xnew= self.PredictorScalerFit.transform(Xnew)
        ynew= self.model.predict(Xnew)
        #invert normalize
        ynew = self.TargetVarScaler.inverse_transform(ynew) 
        Xnew = self.PredictorScalerFit.inverse_transform(Xnew)
        score = ynew[0][0]
     
        return score

    def getConcept(self):
        available_concepts = self.getNextConcepts()
        next_concept = available_concepts[0]
        next_concept['score'] = 0
        for c in available_concepts:
            score = self.getConceptValue(c['id'])
        
            if score > next_concept['score']:
                next_concept = c
                next_concept['score'] = score
                next_concept['known'] = score

    
        return next_concept


    def getNextConcepts(self):

        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.student_id) + '.json',)
        self.data = json.load(f)
        self.concepts = []
        for i in self.data['concepts']:
            if i['known'] < 1:
                self.concepts.append(i)

    
        return self.concepts

    def getConceptValue(self, concept_id):
       
        with open('TestData/student' + str(self.student_id)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
              
                if int(float(row[3])) == int(concept_id):
                    row.pop(len(row) - 1)
                    level = self.predict(row)
                    return level

    def levelConceptsNotLearnt(self, level):
        for i in self.data['concepts']:
            if i['sequence'] == level and i['learnt'] == 0:
                return True

        return False