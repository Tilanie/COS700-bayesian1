
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