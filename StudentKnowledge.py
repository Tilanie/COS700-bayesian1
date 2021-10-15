
from NeuralNetwork import NeuralNetwork
from BugLibrary import BugLibrary
from Bayesian import Bayesian
from FuzzyKnowledgePredictor import FuzzyKnowledgePredictor
import json

class StudentKnowledge:
    def __init__(self, id, method = 0):
        self.student_id = id
        self.level = 0
        self.data = None
        self.concepts = []
        if method == 0: 
            self.predictor = Bayesian(self.student_id)
  
        elif method == 1: 
            self.predictor = NeuralNetwork(self.student_id)
      
        else:
            self.predictor = StandardPredictor(self.student_id)
            
        self.FuzzyKnowledgePredictor = FuzzyKnowledgePredictor()

    def getNextConcept(self):
        concept =  self.predictor.getConcept()
       
        return concept

    def predictKnowledge(self, concept):
        vals = self.predictor.getConcept()
        return vals

    def updateStudentLevel(self):
        pass


class StandardPredictor:
    def __init__(self, id):
        self.student_id = id
        self.level = 0
        self.concepts = []

    def getConcept(self):
        self.concepts = self.getNextConcepts()
        nextConcept = self.concepts[0]
        for c in self.concepts:
            if c['known'] > nextConcept['known']:
                nextConcept = c
    
        return nextConcept


    def getNextConcepts(self):
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.student_id) + '.json',)
        self.data = json.load(f)
        self.level = self.findAvailableLevel()
        for i in self.data['concepts']:
            if self.level < 27:
                if i['sequence'] == self.level + 1 and i['learnt'] == 0:
                    self.concepts.append(i)
            else:
                if i['sequence'] == self.level and i['learnt'] == 0:
                    self.concepts.append(i)

        return self.concepts

    def findAvailableLevel(self):
        if self.level == 27:
            return 27
        else:
            found = False
            while found == False and self.level < 27:
                if self.levelConceptsNotLearnt(self.level) == True:
                    return self.level
                else:
                    self.level = self.level + 1
        return self.level

    def levelConceptsNotLearnt(self, level):
        for i in self.data['concepts']:
            if i['sequence'] == level and i['learnt'] == 0:
                return True

        return False
        

