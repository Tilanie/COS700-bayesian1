from keras.engine.training import concat
from StudentKnowledge import StudentKnowledge
from Fuzzy import Fuzzy

class DynamicKnowledge:
    def __init__(self, id, method,stereotype = False, fuzzy = False):
        self.student_id = id
        self.fuzzy_used = fuzzy
      
        self.StudentKnowledge = StudentKnowledge(self.student_id, method, stereotype, self.fuzzy_used)

    def getNextConcept(self):
        concept =  self.StudentKnowledge.getNextConcept()
        
        return concept


    def predictStudentKnowledge(self, concept):
        vals = self.StudentKnowledge.predictKnowledge(concept)
        return vals