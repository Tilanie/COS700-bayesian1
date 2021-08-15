from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

bayesNet = BayesianModel()
# bayesNet.add_node("constantFunctionGraph")
bayesNet.add_node("intercept")
bayesNet.add_node("posIntercept")
bayesNet.add_node("negIntercept")
bayesNet.add_node("linearFunctionGraph")
bayesNet.add_node("slope")
bayesNet.add_node("posSlope")
bayesNet.add_node("zeroSlope")
bayesNet.add_node("negSlope")



bayesNet.add_edge("intercept", "linearFunctionGraph")
bayesNet.add_edge("slope", "linearFunctionGraph")
bayesNet.add_edge("posSlope", "slope")
bayesNet.add_edge("zeroSlope", "slope")
bayesNet.add_edge("negSlope", "slope")
bayesNet.add_edge("posIntercept", "intercept")
bayesNet.add_edge("negIntercept", "intercept")
bayesNet.add_edge("intercept", "constantFunctionGraph")

cpd_PI = TabularCPD('posIntercept', 2, values=[[.95], [.05]])
cpd_NI = TabularCPD('negIntercept', 2, values=[[.85], [.15]])
cpd_PS = TabularCPD('posSlope', 2, values=[[.90], [.10]])
cpd_ZS = TabularCPD('zeroSlope', 2, values=[[.90], [.10]])
cpd_NS = TabularCPD('negSlope', 2, values=[[.90], [.10]])


cpd_LF = TabularCPD('linearFunctionGraph', 2, values=[[0.98, .88, .95, .6], [.02, .12, .05, .40]],
                   evidence=['intercept', 'slope'], evidence_card=[2, 2])

cpd_CF = TabularCPD('constantFunctionGraph', 2, values=[[0.98, .88], [.02, .12]],
                   evidence=['intercept'], evidence_card=[2])

print(cpd_CF)

cpd_I = TabularCPD('intercept', 2, values=[[0.98, .88, .95, .6], [.02, .12, .05, .40]],
                   evidence=['negIntercept', 'posIntercept'], evidence_card=[2, 2])


cpd_S = TabularCPD('slope', 2,
                   values=[[0.96, .86, .94, .82, .24, .15, .10, .05], [.04, .14, .06, .18, .76, .85, .90, .95]],
                   evidence=['posSlope', 'zeroSlope', 'negSlope'], evidence_card=[2, 2,2])





bayesNet.add_cpds(cpd_PS, cpd_ZS, cpd_NS, cpd_S, cpd_PI, cpd_NI, cpd_I, cpd_LF, cpd_CF)

bayesNet.check_model()
print("Model is correct.")

solver = VariableElimination(bayesNet)

result = solver.query(variables=['slope'])
# print("R", result['R'].values[1])
print(result.values[1])