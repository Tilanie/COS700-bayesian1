from StaticKnowledge import StaticKnowledge
from DynamicKnowledge import DynamicKnowledge
import json
import random

class StudentModel:
    def __init__(self, name, id, username, password, email, language, city, country, seed):
        self.seed = seed
        self.id = id
        self.static_knowledge = StaticKnowledge(name, id, username, password, email, language, city, country)
        self.dynamic_knowledge = DynamicKnowledge(id)

    def predictStudentKnowledge(self, concept):
        vals = self.dynamic_knowledge.predictStudentKnowledge(concept)
        
        return vals

    def getNextConcept(self):
        concept = self.dynamic_knowledge.getNextConcept()
        return concept

    def learn(self):
        concept = self.getNextConcept()
        self.learnConcept(concept)

    def learnConcept(self, concept):
     
        sid = self.id
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json',)
        self.knowledge = json.load(f)
      
            
        for i in self.knowledge['concepts']: 
      
            if str(i['id']) == str(concept['id']):
                
                increase = self.levelOfIncrease(i['known'])
                i['known'] = i['known'] + increase
                i['learnt'] = i['learnt'] + 1
               

        with open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json', 'w') as outfile:
            json.dump(self.knowledge, outfile)
            
        
        f = open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json',)
        self.knowledge = json.load(f)
      
            
        for i in self.knowledge['concepts']: 
            
            if str(i['id']) == str(concept['id']):
                
                increase = self.levelOfIncrease(i['known'])
                i['known'] = i['known'] + increase
                i['learnt'] = i['learnt'] + 1
              
                

        with open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json', 'w') as outfile:
            json.dump(self.knowledge, outfile)
    
            
    def levelOfIncrease(self, currentKnowledge):
        self.seed = self.seed + 1
        random.seed(self.seed)
        range_ = 1 - currentKnowledge
        number = random.uniform(range_/2.3, range_)
        return number