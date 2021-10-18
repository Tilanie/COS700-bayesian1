from keras.engine.training import concat
from StudentKnowledge import StudentKnowledge

class DynamicKnowledge:
    def __init__(self, id, method):
        self.student_id = id
  
        self.StudentKnowledge = StudentKnowledge(self.student_id, method)

    def getNextConcept(self):
        concept =  self.StudentKnowledge.getNextConcept()
        
        return concept


    def predictStudentKnowledge(self, concept):
        vals = self.StudentKnowledge.predictKnowledge(concept)
        return vals