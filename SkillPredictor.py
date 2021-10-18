from KNearestNeighbour import KNearestNeighbour
import json
from Fuzzy import Fuzzy
import copy
import os.path
class SkillPredictor:
    def __init__(self, id):
        self.id = id
        self.user_id = id
  
        self.knn = KNearestNeighbour()
        self.fuzzy = Fuzzy()
        
    def predictSkill(self):
        file_exists = os.path.exists('StudentKnowledge/KnowledgeMapLearnt' + str(self.user_id) + '.json')
        if file_exists == True:
            f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.user_id) + '.json',)
        else:
            f = open('BayesianData.json',)
   
        data = json.load(f)
        
        for i in range(0, len(data['concepts'])):
            if data['concepts'][i]["terminal"] == 1:
                level = self.knn.predict(self.getUserData(data['concepts'][i]["id"]), data['concepts'][i]["id"])
              
                known = self.encodeSkillLevel(level)
            
                data['concepts'][i]['probability_true'] = copy.deepcopy([known])
                data['concepts'][i]['known'] = known
                false = round((1 - known), 2)
                data['concepts'][i]['probability_false'] = [false]
            else: #not terminal, knowledge needs to be updates
                level = self.knn.predict(self.getUserData(data['concepts'][i]["id"]), data['concepts'][i]["id"])
                # print(self.getUserData(data['concepts'][i]["id"]))
                # print(data['concepts'][i]["id"])
                # print(level)
                known = self.encodeSkillLevel(level)
                # print(known)
                data['concepts'][i]['known'] = copy.deepcopy(known)
    
        with open('StudentKnowledge/knowledgeMapLearnt' + str(self.user_id) + '.json', 'w') as outfile:
            json.dump(data, outfile)
     
    
    def getUserData(self, id):
     
        f = open('StudentKnowledge/knowledgeMap' + str(self.user_id) + '.json',)
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