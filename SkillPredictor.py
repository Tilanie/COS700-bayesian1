from KNearestNeighbour import KNearestNeighbour
import json
from Fuzzy import Fuzzy
import copy
class SkillPredictor:
    def __init__(self, id):
        self.id = id
        self.knn = KNearestNeighbour()
        self.fuzzy = Fuzzy()
        
    def predictSkill(self):
        f = open('BayesianData.json',)
        data = json.load(f)
        
        for i in range(0, len(data['concepts'])):
            if data['concepts'][i]["terminal"] == 1:
                level = self.knn.predict(self.getUserData(data['concepts'][i]["id"]), self.id)
              
                known = self.encodeSkillLevel(level)
            
                data['concepts'][i]['probability_true'] = copy.deepcopy([known])
                false = round((1 - known), 2)
                data['concepts'][i]['probability_false'] = [false]
     
       
    
        with open('StudentKnowledge/knowledgeMapLearnt' + str(self.id) + '.json', 'w') as outfile:
            json.dump(data, outfile)
     
    
    def getUserData(self, id):
  
        f = open('StudentKnowledge/knowledgeMap' + str(self.id) + '.json',)
        self.data = json.load(f)
            
        for i in self.data['concepts']:
            if int(i['id']) == int(id):
                concept =id
                gender = i['gender']
                age = i['age']
                degree_careful = i['degreeCarefull']
                class_id = i['classID'] 
                proficiency = i['proficiency']
                return [concept, gender, age, class_id, degree_careful, proficiency]

    def encodeSkillLevel(self, level):
        if level == 'novice':
            return 0
        elif level == 'beginner':
            return 0.33
        elif level == 'intermediate':
            return 0.66
        else:
            return 1