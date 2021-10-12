
# THIRD EXAMPLE
from simpful import *
# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object
class Fuzzy:
    def __init__(self):
        FS = FuzzySystem()
        # Define fuzzy sets and linguistic variables
        S_1 = FuzzySet(points=[[0., 1.], [14.3, 1.], [28.6, 0.]], term="novice")
        S_2 = FuzzySet(points=[[14.3, 0.], [28.6, 1.], [42.9, 1.], [57.2, 0.]], term="beginner")
        S_3 = FuzzySet(points=[[42.9, 0.], [57.2, 1.], [71.5, 1.], [85.8, 0.]], term="intermediate")
        S_4 = FuzzySet(points=[[71.5, 0.], [85.8, 1.], [100., 1.]], term="advanced")

        FS.add_linguistic_variable("stereotype", LinguisticVariable([S_1, S_2, S_3, S_4], concept="Stereotype Prediction"))


        # S_4 = FuzzySet(points=[[0., 1.], [40., 1.], [50., 0.]], term="poor")
        # S_5 = FuzzySet(points=[[40., 0.], [50., 1.], [70., 1.], [80., 0.]], term="good")
        # S_6 = FuzzySet(points=[[70., 0.], [80., 1.], [100., 1.]], term="excellent")

        # FS.add_linguistic_variable("pretest", LinguisticVariable([S_4, S_5, S_6], concept="Pretest grade"))

        FS.set_crisp_output_value("low", 0)
        FS.set_crisp_output_value("high", 1)

        # Define fuzzy rules
        R1 = "IF (stereotype IS novice) THEN (Performance IS low)"
        R2 = "IF (stereotype IS beginner) THEN (Performance IS low)"
        R3 = "IF (stereotype IS intermediate) THEN (Performance IS high)"
        R4 = "IF (stereotype IS advanced) THEN (Performance IS high)"

        FS.add_rules([R1, R2, R3, R4])
        FS.set_variable("stereotype", 34)



        # Perform Sugeno inference and print output
        print("\n\nPERFORMACE")
        print(FS.Sugeno_inference(["Performance"]))