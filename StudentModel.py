from StaticKnowledge import StaticKnowledge
from DynamicKnowledge import DynamicKnowledge
import json
import random
import csv
import pandas as pd

class StudentModel:
    def __init__(self, name, id, username, password, email, language, city, country, seed, method):
        self.seed = seed
        self.id = id
        self.method = method
        self.static_knowledge = StaticKnowledge(name, id, username, password, email, language, city, country)
        self.dynamic_knowledge = DynamicKnowledge(id, method)

    def predictStudentKnowledge(self, concept):
        vals = self.dynamic_knowledge.predictStudentKnowledge(concept)
        
        return vals

    def getNextConcept(self):
        concept = self.dynamic_knowledge.getNextConcept()
        return concept

    def learn(self):
        concept = self.getNextConcept()
        print(concept)
        concept = self.learnConcept(concept)
        print(concept)
        self.updateTestScores(concept)

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
                i['learnt'] = i['learnt'] + 1
               

        with open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json', 'w') as outfile:
            json.dump(self.knowledge, outfile)
            
        f.close()
        f = open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json',)
        self.knowledge = json.load(f)
      
            
        for i in self.knowledge['concepts']: 
            
            if str(i['id']) == str(concept['id']):
                
           
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

    def updateTestScores(self, concept):
     
    
        self.dataset = pd.read_csv('TestData/student' + str(self.id), delimiter=',', header=None)
        f = open('TestData/student' + str(self.id), 'w', newline='')
        writer = csv.writer(f)
        for row in self.dataset.values:
           
            if int(row[3]) == int(concept['id']): #value found to replace
                test1 = row[0] + self.increase
                test2 = row[1] + self.increase
                test3 = row[2] + self.increase

                        
                sequence = concept['sequence']
        
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