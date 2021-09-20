from StaticKnowledge import StaticKnowledge
from DynamicKnowledge import DynamicKnowledge

class StudentModel:
    def __init__(self):
        self.id = 0
        self.static_knowledge = StaticKnowledge()
        self.dynamic_knowledge = DynamicKnowledge()

    def predictStudentKnowledge(self, concept):
        vals = self.dynamic_knowledge.predictStudentKnowledge(concept)
        
        return vals