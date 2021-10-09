from StaticKnowledge import StaticKnowledge
from DynamicKnowledge import DynamicKnowledge

class StudentModel:
    def __init__(self, name, id, username, password, email, language, city, country):
        self.id = 0
        self.static_knowledge = StaticKnowledge(name, id, username, password, email, language, city, country)
        self.dynamic_knowledge = DynamicKnowledge()

    def predictStudentKnowledge(self, concept):
        vals = self.dynamic_knowledge.predictStudentKnowledge(concept)
        
        return vals