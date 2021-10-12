from KNearestNeighbour import KNearestNeighbour
import json
from Fuzzy import Fuzzy
class SkillPredictor:
    def __init__(self, user_record):
        self.user_record = user_record
        self.knn = KNearestNeighbour(self.user_record)
        self.fuzzy = Fuzzy()
        
    def predictSkill(self):
        f = open('BayesianData.json',)
        self.data = json.load(f)
        
        for i in self.data['concepts']:
            if i["terminal"] == 1:
                level = self.knn.predict(i["id"])
                known = self.encodeSkillLevel(level)
                i['probability_true'] = [known]
                false = round((1 - known), 2)
                i['probability_false'] = [false]


        with open('BayesianDataOut.json', 'w') as outfile:
            json.dump(self.data, outfile)
        return self.knn.getSkill()

    def encodeSkillLevel(self, level):
        if level == 'novice':
            return 0
        elif level == 'beginner':
            return 0.33
        elif level == 'intermediate':
            return 0.66
        else:
            return 1