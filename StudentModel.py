from StaticKnowledge import StaticKnowledge
from DynamicKnowledge import DynamicKnowledge
import json
import random
import csv
import pandas as pd
from Fuzzy import Fuzzy

class StudentModel:
    def __init__(self, name, id, username, password, email, language, city, country, seed, method, stereotype = False, fuzzy = False):
        self.seed = seed
        self.id = id
        self.method = method
        self.static_knowledge = StaticKnowledge(name, id, username, password, email, language, city, country)
        self.dynamic_knowledge = DynamicKnowledge(id, method, stereotype)
        self.starting_knowledge = 0
        self.setTotalKnowledge()
        self.fuzzy_used = fuzzy
        if self.fuzzy_used == True:
            self.fuzzy = Fuzzy()

    def setTotalKnowledge(self):
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.id) + '.json',)
        data = json.load(f)
        total_data = 0
        learnt_knowledge = 0
        for i in data['concepts']:
            total_data = total_data + i['known']
            

        self.starting_knowledge = total_data
        f.close()

    def finalTotalKnowledge(self, method):
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.id) + '.json',)
        data = json.load(f)
        total_data = 0
        if method == 0: # total improvement across all concepts
            for i in data['concepts']:
                total_data = total_data + i['known']
            return total_data - self.starting_knowledge
        elif method == 1: # percentage improvement
            for i in data['concepts']:
                total_data = total_data + i['known']
            return (total_data - self.starting_knowledge) / self.starting_knowledge
       
        f.close()

    def predictStudentKnowledge(self, concept):
        vals = self.dynamic_knowledge.predictStudentKnowledge(concept)
        
        return vals

    def getNextConcept(self):
        concept = self.dynamic_knowledge.getNextConcept()
        return concept

    def learn(self):
        
        concept = self.getNextConcept()
    
        # wait = input("before learning")
        concept = self.learnConcept(concept)
     
        actual_concept = self.findConceptFromBayesianConcept(concept)
        self.updateTestScores(concept, actual_concept)
        # wait = input("after learning")

    def findConceptFromBayesianConcept(self, concept):
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.id) + '.json',)
        knowledge = json.load(f)
        for i in knowledge['concepts']:
            if i['id'] == concept['id']:
                return i

    def learnConcept(self, concept):
     
        sid = self.id
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json',)
        self.knowledge = json.load(f)
      
        increase = self.levelOfIncrease(concept['known'])
        self.increase = increase
        concept['known'] = concept['known'] + increase
        concept['learnt'] = concept['learnt'] + 1

        for i in self.knowledge['concepts']: 
      
            if str(i['id']) == str(concept['id']):
                
                
                i['known'] = i['known'] + increase
           
                # i['probability_true'] = i['known']
                # i['probability_false'] = 1 - i['probability_true']
                i['learnt'] = i['learnt'] + 1
  

        with open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json', 'w') as outfile:
            json.dump(self.knowledge, outfile)
            
        f.close()
        f = open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json',)
        self.knowledge = json.load(f)
      
            
        for i in self.knowledge['concepts']: 
            
            if str(i['id']) == str(concept['id']):
                
                # i['probability_true'] = i['known']
                # i['probability_false'] = 1 - i['probability_true']
                i['known'] = i['known'] + increase
                i['learnt'] = i['learnt'] + 1
              
        with open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json', 'w') as outfile:
            json.dump(self.knowledge, outfile)
        f.close()

        return concept
            
    def levelOfIncrease(self, currentKnowledge):
        self.seed = self.seed + 1
        random.seed(self.seed)
        range_ = 1 - currentKnowledge
        number = random.uniform(currentKnowledge, currentKnowledge*1.5)
        if number + currentKnowledge > 1:
            number  = 1 - currentKnowledge
        return number

    def updateTestScores(self, concept, actual_concept):
     
        self.dataset = pd.read_csv('TestData/student' + str(self.id), delimiter=',', header=None)
        f = open('TestData/student' + str(self.id), 'w', newline='')
        writer = csv.writer(f)
        for row in self.dataset.values:
           
            if int(row[3]) == int(concept['id']): #value found to replace
                test1 = row[0] + self.increase
                test2 = row[1] + self.increase
                test3 = row[2] + self.increase

                        
                sequence = actual_concept['sequence']
        
                test1 = test1 * 100
                test2 = test2 * 100
                test3 = test3 * 100
                chance_known = self.generateChanceKnown(test1, test2, test3)
                test1 = test1 / 100
                test2 = test2 / 100
                test3 = test3 / 100
                chance_known = chance_known / 100
                        
                new_row = []
                new_row.append(test1)
                new_row.append(test2)
                new_row.append(test3)
                new_row.append(int(concept['id']))
                new_row.append(sequence)
                new_row.append(chance_known)
          
                writer.writerow(new_row)
                    # close the file
                
            else: #write existing data
                writer.writerow(row)
        f.close()


    def generateChanceKnown(self, test1, test2, test3):
        self.seed = self.seed + 1 
        random.seed(self.seed)
        average = (test1 + test2 + test3) / 3
        variance_value = random.uniform(-1 * (0.15 * average), 0.15 * average)
        test_value = average + variance_value

        return test_value

    def generateTestScore(self, known, sequence):
        self.seed = self.seed + 1
        random.seed(self.seed)

        if known == 1: #concept is known
            score = 50 + random.randint(0, (27 - sequence)) + random.randint(0, 23)
        else:
            score = random.randint(0, (27 - sequence)) + random.randint(0, 23)

        return score