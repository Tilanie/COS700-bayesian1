

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
            children = []
            self.network.append(i)
            self.bayesNet.add_node(i["description"])
            for j in i["children"]:
                self.bayesNet.add_edge(j["description"], i["description"])
                children.append(j["description"])
                
         
            if i["terminal"] == 0:
                cpd_val = TabularCPD(i["description"], 2, values=[i["probability_true"], i["probability_false"]],
                   evidence=children, evidence_card=i["dimensions"])
                self.cpd_list.append(cpd_val)
            else:
                cpd_val = TabularCPD(i["description"], 2, values=[i["probability_true"], i["probability_false"]])  
       
                self.cpd_list.append(cpd_val)
       
        
             
        for k in self.cpd_list:
            print(k)
            self.bayesNet.add_cpds(k)
            
            
        self.bayesNet.check_model()
        f.close()
        


# bayesNet.check_model()

# solver = VariableElimination(bayesNet)

# result = solver.query(variables=['slope'])
# print("R", result['R'].values[1])
# print(result.values[1])
# print("============================================")
# print(result)
# print("============================================")