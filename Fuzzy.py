# from simpful import *

# FS = FuzzySystem()

# TLV = AutoTriangle(3, terms=['poor', 'good', 'excellent'], universe_of_discourse=[0,100])
# FS.add_linguistic_variable("service", TLV)
# FS.add_linguistic_variable("quality", TLV)

# O1 = TriangleFuzzySet(0,0,13,   term="low")
# O2 = TriangleFuzzySet(0,13,25,  term="medium")
# O3 = TriangleFuzzySet(13,25,25, term="high")
# FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,25]))

# FS.add_rules([
# 	"IF (quality IS poor) OR (service IS poor) THEN (tip IS low)",
# 	"IF (service IS average) THEN (tip IS medium)",
# 	"IF (quality IS good) OR (quality IS good) THEN (tip IS high)"
# 	])

# FS.set_variable("quality", 6.5) 
# FS.set_variable("service", 9.8) 

# tip = FS.inference()
# print(tip)

# SECOND EXAMPLE

# from simpful import *
# # A simple fuzzy inference system for the tipping problem

# # Create a fuzzy system object

# FS = FuzzySystem()
# # Define fuzzy sets and linguistic variables

# S_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=5), term="poor")
# S_2 = FuzzySet(function=Triangular_MF(a=0, b=5, c=10), term="good")

# S_3 = FuzzySet(function=Triangular_MF(a=5, b=10, c=10), term="excellent")

# FS.add_linguistic_variable("Service", LinguisticVariable([S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0,10]))


# F_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="rancid")

# F_2 = FuzzySet(function=Triangular_MF(a=0, b=10, c=10), term="delicious")

# FS.add_linguistic_variable("Food", LinguisticVariable([F_1, F_2], concept="Food quality", universe_of_discourse=[0,10]))

# # Define output fuzzy sets and linguistic variable
# T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="small")
# T_2 = FuzzySet(function=Triangular_MF(a=0, b=10, c=20), term="average")
# T_3 = FuzzySet(function=Trapezoidal_MF(a=10, b=20, c=25, d=25), term="generous")
# FS.add_linguistic_variable("Tip", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0,25]))
# # Define fuzzy rules
# R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
# R2 = "IF (Service IS good) THEN (Tip IS average)"
# R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
# FS.add_rules([R1, R2, R3])

# # Set antecedents values
# FS.set_variable("Service", 4)
# FS.set_variable("Food", 8)

# # Perform Mamdani inference and print output
# print(FS.Mamdani_inference(["Tip"]))

# THIRD EXAMPLE
from simpful import *
# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object
FS = FuzzySystem()
# Define fuzzy sets and linguistic variables
S_1 = FuzzySet(points=[[0., 1.], [40., 1.], [50., 0.]], term="poor")
S_2 = FuzzySet(points=[[40., 0.], [50., 1.], [70., 1.], [80., 0.]], term="good")
S_3 = FuzzySet(points=[[70., 0.], [80., 1.], [100., 1.]], term="excellent")

FS.add_linguistic_variable("topicTest", LinguisticVariable([S_1, S_2, S_3], concept="TopicTest grade"))


S_4 = FuzzySet(points=[[0., 1.], [40., 1.], [50., 0.]], term="poor")
S_5 = FuzzySet(points=[[40., 0.], [50., 1.], [70., 1.], [80., 0.]], term="good")
S_6 = FuzzySet(points=[[70., 0.], [80., 1.], [100., 1.]], term="excellent")

FS.add_linguistic_variable("pretest", LinguisticVariable([S_4, S_5, S_6], concept="Pretest grade"))

FS.set_crisp_output_value("low", 0)
FS.set_crisp_output_value("high", 1)

# Define fuzzy rules
R1 = "IF (pretest IS poor) AND (topicTest IS poor) THEN (Performance IS low)"
R2 = "IF (pretest IS poor) AND (topicTest IS good) THEN (Performance IS low)"
R3 = "IF (pretest IS poor) AND (topicTest IS excellent) THEN (Performance IS high)"
R4 = "IF (pretest IS good) AND (topicTest IS poor) THEN (Performance IS low)"
R5 = "IF (pretest IS good) AND (topicTest IS good) THEN (Performance IS high)"
R6 = "IF (pretest IS good) AND (topicTest IS excellent) THEN (Performance IS high)"
R7 = "IF (pretest IS excellent) AND (topicTest IS poor) THEN (Performance IS low)"
R8 = "IF (pretest IS excellent) AND (topicTest IS good) THEN (Performance IS high)"
R9 = "IF (pretest IS excellent) AND (topicTest IS excellent) THEN (Performance IS high)"

FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9])
FS.set_variable("pretest", 40)

FS.set_variable("topicTest", 75)

# Perform Sugeno inference and print output
print(FS.Sugeno_inference(["Performance"]))