
# THIRD EXAMPLE
from simpful import *
# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object
class Fuzzy:
    def __init__(self):
        self.FS = FuzzySystem()
        # Define fuzzy sets and linguistic variables
        S_1 = FuzzySet(points=[[0., 1.], [14.3, 1.], [28.6, 0.]], term="novice")
        S_2 = FuzzySet(points=[[14.3, 0.], [28.6, 1.], [42.9, 1.], [57.2, 0.]], term="beginner")
        S_3 = FuzzySet(points=[[42.9, 0.], [57.2, 1.], [71.5, 1.], [85.8, 0.]], term="intermediate")
        S_4 = FuzzySet(points=[[71.5, 0.], [85.8, 1.], [100., 1.]], term="advanced")

        self.FS.add_linguistic_variable("stereotype", LinguisticVariable([S_1, S_2, S_3, S_4], concept="Stereotype Prediction"))

        self.FS.set_crisp_output_value("low", 0.33)
        self.FS.set_crisp_output_value("medium", 0.50)
        self.FS.set_crisp_output_value("high", 0.66)
        self.FS.set_crisp_output_value("advanced", 1)

        # Define fuzzy rules
        R1 = "IF (stereotype IS novice) THEN (Performance IS low)"
        R2 = "IF (stereotype IS beginner) THEN (Performance IS medium)"
        R3 = "IF (stereotype IS intermediate) THEN (Performance IS high)"
        R4 = "IF (stereotype IS advanced) THEN (Performance IS advanced)"

        self.FS.add_rules([R1, R2, R3, R4])
        self.FS.set_variable("stereotype", 34)


    def predict(self, variable):
        self.FS.set_variable("stereotype", variable)

        print(self.FS.Sugeno_inference(["Performance"])['Performance'])
        return self.FS.Sugeno_inference(["Performance"])['Performance']
