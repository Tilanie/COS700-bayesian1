

from Concepts import Concepts
import numpy as np
import json
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from SkillPredictor import SkillPredictor

class Bayesian:
    def __init__(self, id, stereotype = False):
 

        self.skillPredictor = SkillPredictor(id)
        if stereotype == True:
            self.skillPredictor.predictSkill()
        else:
            self.skillPredictor.predictSkillStandard()
        # wait = input("knowledge iunitialised")
        self.student_id = id
        self.network = []
        self.cpd_list = []
        self.concepts = []
        self.bayesNet = BayesianModel()
        f = open('StudentKnowledge/knowledgeMapLearnt' + str(id) + '.json',)
        self.data = json.load(f)
        
        for i in self.data['concepts']:
            # concept = Concept()
            children = []
            self.network.append(i)
            self.bayesNet.add_node(i["description"])
            for j in i["children"]:
                self.bayesNet.add_edge(j["description"], i["description"])
                children.append(j["description"])
        
            c = len(i["children"])
            d = len(i["dimensions"])
            
            c = 2
            if i["terminal"] == 0:
                v = [i["probability_true"], i["probability_false"]]
           
                cpd_val = TabularCPD(i["description"], c, values=v,
                   evidence=children, evidence_card=i["dimensions"])
                self.cpd_list.append(cpd_val)
            else:
                v = [i["probability_true"], i["probability_false"]]
                cpd_val = TabularCPD(variable=i["description"], variable_card=c, values=v)  
       
                self.cpd_list.append(cpd_val)
       
        
        for k in self.cpd_list:
            
            self.bayesNet.add_cpds(k)
            
            
        self.bayesNet.check_model()
        self.solver = VariableElimination(self.bayesNet)
      
        f.close()

    def updateNetwork(self):
        self.network = []
        self.cpd_list = []
        self.concepts = []
        self.bayesNet = BayesianModel()
        f = open('StudentKnowledge/knowledgeMapLearnt' + str(self.student_id) + '.json',)
        self.data = json.load(f)
        
        for i in self.data['concepts']:
            # concept = Concept()
            children = []
            self.network.append(i)
            self.bayesNet.add_node(i["description"])
            for j in i["children"]:
                self.bayesNet.add_edge(j["description"], i["description"])
                children.append(j["description"])
        
            c = len(i["children"])
            d = len(i["dimensions"])
            
            c = 2
            if i["terminal"] == 0:
                v = [i["probability_true"], i["probability_false"]]

               
                cpd_val = TabularCPD(i["description"], c, values=v,
                   evidence=children, evidence_card=i["dimensions"])
                self.cpd_list.append(cpd_val)
            else:
                v = [i["probability_true"], i["probability_false"]]
                cpd_val = TabularCPD(variable=i["description"], variable_card=c, values=v)  
       
                self.cpd_list.append(cpd_val)
       
        
        for k in self.cpd_list:
     
            self.bayesNet.add_cpds(k)
            
            
        self.bayesNet.check_model()
        self.solver = VariableElimination(self.bayesNet)
      
        f.close()

    def predictConcept(self, concept):
        result = self.solver.query(variables=[concept])
        
        return result.values

    def getConcept(self):
        self.updateNetwork()
        self.concepts = self.getNextConcepts()
        concept_values = []
        for c in self.concepts:
            new_concept_value = self.predictConcept(c['description'])
            concept_values.append({
                "description": c['description'],
                "id": c['id'],
                "values": new_concept_value,
                "learnt": c['learnt'],
                "children": c["children"].copy(),
                "dimensions": c['dimensions'],
                "terminal": c['terminal'],
                "probability_true": c['probability_true'],
                "probability_false": c['probability_false'],
                "known": c['known']
            })

        # find the best option
        best_concept = concept_values[0]
        for c in concept_values:
            if c['values'][0] > best_concept['values'][0]:
                best_concept = c

        return best_concept

    def getNextConcepts(self):
        f = open('StudentKnowledge/KnowledgeMapLearnt' + str(self.student_id) + '.json',)
        data = json.load(f)
        concepts = []
        for i in data['concepts']:
           

            if i['known'] < 1:
                concepts.append(i)

        return concepts

    def findAvailableLevel(self):
        pass

    def levelConceptsNotLearnt(self, level):
        for i in self.data['concepts']:
            if i['sequence'] == level and i['learnt'] == 0:
                return True

        return False
    
    



        