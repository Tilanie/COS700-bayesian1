
from NeuralNetwork import NeuralNetwork
from BugLibrary import BugLibrary
from Bayesian import Bayesian
from FuzzyKnowledgePredictor import FuzzyKnowledgePredictor
import json
from Fuzzy import Fuzzy
class StudentKnowledge:
    def __init__(self, id, method = 0, stereotype = False, fuzzy = False):
        self.student_id = id
    
        self.level = 0
        self.data = None
        self.concepts = []
        self.fuzzy_used = fuzzy

        if method == 0: 
            self.predictor = Bayesian(self.student_id, stereotype)
  
        elif method == 1: 
            self.predictor = NeuralNetwork(self.student_id, self.fuzzy_used)
      
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
        # for c in self.concepts:
        #     if c['known'] > nextConcept['known']:
        #         nextConcept = c
    
        return nextConcept


    def getNextConcepts(self):
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.student_id) + '.json',)
        self.data = json.load(f)
        self.level = self.findAvailableLevel()
        self.concepts = []
        # use_level = self.level
        # num_tries = 0
        # decreasing = False
        while len(self.concepts) == 0:
            for i in self.data['concepts']:
                if i['learnt'] < 2 and i['known'] < 1:
                        self.concepts.append(i)
                    
            
            # if use_level == 0:
            #     use_level = use_level + 1
            # else:
            #     if use_level == 27:
            #         use_level = 0
            #     else:
            #         use_level = use_level + 1
            # num_tries = num_tries + 1

            # if num_tries > 26:
            #     num_tries = 0
            #     decreasing = not decreasing
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
        

