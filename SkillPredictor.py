from KNearestNeighbour import KNearestNeighbour

class SkillPredictor:
    def __init__(self, user_record):
        self.user_record = user_record
        self.knn = KNearestNeighbour(self.user_record)

    def predictSkill(self):
        return self.knn.getSkill()