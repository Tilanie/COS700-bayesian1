from KNearestNeighbour import KNearestNeighbour
import json

class SkillPredictor:
    def __init__(self, user_record):
        self.user_record = user_record
        self.knn = KNearestNeighbour(self.user_record)

    def predictSkill(self, data):
        f = open('BayesianData.json',)
        self.data = json.load(f)
        
        for i in self.data['concepts']:
            if i["terminal"] == 1:
                self.knn.getSkill(i["id"])

        with open('BayesianDataOut.txt', 'w') as outfile:
            json.dump(self.data, outfile)
        return self.knn.getSkill()