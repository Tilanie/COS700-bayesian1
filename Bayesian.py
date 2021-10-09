

from Concepts import Concepts
import numpy as np
import json
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

class Bayesian:
    def __init__(self):
        self.network = []
        self.cpd_list = []
        
        self.bayesNet = BayesianModel()
        f = open('BayesianData.json',)
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
                # if d < 2:
                #     v = [i["probability_true"]]
                # else:
                v = [i["probability_true"], i["probability_false"]]

               
                cpd_val = TabularCPD(i["description"], c, values=v,
                   evidence=children, evidence_card=i["dimensions"])
                self.cpd_list.append(cpd_val)
            else:
                v = [i["probability_true"], i["probability_false"]]
                cpd_val = TabularCPD(variable=i["description"], variable_card=c, values=v)  
       
                self.cpd_list.append(cpd_val)
       
        
             
        for k in self.cpd_list:
            # print(k)
            self.bayesNet.add_cpds(k)
            
            
        self.bayesNet.check_model()
        self.solver = VariableElimination(self.bayesNet)
      
        
    

        f.close()

    def predictConcept(self, concept):
        result = self.solver.query(variables=[concept])
        
        return result.values



        


# bayesNet.check_model()

# solver = VariableElimination(bayesNet)

# result = solver.query(variables=['slope'])
# print("R", result['R'].values[1])
# print(result.values[1])
# print("============================================")
# print(result)
# print("============================================")