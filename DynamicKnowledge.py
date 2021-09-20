from StudentKnowledge import StudentKnowledge

class DynamicKnowledge:
    def __init__(self):
        self.StudentKnowledge = StudentKnowledge()

    def predictStudentKnowledge(self, concept):
        vals = self.StudentKnowledge.predictKnowledge(concept)
        return vals