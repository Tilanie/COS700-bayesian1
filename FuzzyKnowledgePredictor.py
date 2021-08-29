from simpful import *

class FuzzyKnowledgePredictor:
    def __init__(self):
        self.fuzzy_predictor = self.FuzzyPredictor()
    
    def FuzzyPredictor(self):
        FS = FuzzySystem()
        # Define fuzzy sets and linguistic variables
        S_1 = FuzzySet(points=[[0., 1.], [15., 1.], [25., 0.]], term="very_easy")
        S_2 = FuzzySet(points=[[15., 0.], [25., 1.], [35., 1.], [45., 0.]], term="easy")
        S_3 = FuzzySet(points=[[35., 0.], [45., 1.], [55., 1.], [65., 0.]], term="middle")
        S_4 = FuzzySet(points=[[55., 0.], [65., 1.], [75., 1.], [85., 0.]], term="difficult")
        S_5 = FuzzySet(points=[[75., 0.], [85., 1.], [100., 0.]], term="very_difficult")
        
        FS.add_linguistic_variable("test_difficulty", LinguisticVariable([S_1, S_2, S_3, S_4, S_5], concept="Test Difficulty"))
        
        # S_6 = FuzzySet(points=[[0., 1.], [15., 1.], [25., 0.]], term="short")
        # S_7 = FuzzySet(points=[[15., 0.], [25., 1.], [35., 1.], [45., 0.]], term="middle")   "@NEED DATA FOR THIS"
        # S_8 = FuzzySet(points=[[35., 0.], [45., 1.], [55., 1.], [65., 0.]], term="long")
        
        # FS.add_linguistic_variable("test_duration", LinguisticVariable([S_6, S_7, S_8], concept="Test Duration"))
        
        S_9 = FuzzySet(points=[[0., 1.], [45., 1.], [50., 0.]], term="bad")
        S_10 = FuzzySet(points=[[45., 0.], [50., 1.], [60., 1.], [65., 0.]], term="not_bad")
        S_11 = FuzzySet(points=[[60., 0.], [65., 1.], [75., 1.], [80., 0.]], term="good")
        S_12 = FuzzySet(points=[[75., 0.], [80., 1.], [90., 1.], [95., 0.]], term="very_good")
        S_13 = FuzzySet(points=[[90., 0.], [95., 1.], [100., 0.]], term="excellent")
        
        FS.add_linguistic_variable("test_success", LinguisticVariable([S_9, S_10, S_11, S_12, S_13], concept="Test Success"))
        
        
        FS.set_crisp_output_value("not_enough", 0)
        FS.set_crisp_output_value("enough", 1)
        
        
        # Define fuzzy rules
        R1 = "IF (test_difficulty IS very_easy) AND (test_success IS bad) THEN (Knowledge IS not_enough)"
        R2 = "IF (test_difficulty IS very_easy) AND (test_success IS not_bad) THEN (Knowledge IS not_enough)"
        R3 = "IF (test_difficulty IS very_easy) AND (test_success IS good) THEN (Knowledge IS not_enough)"
        R4 = "IF (test_difficulty IS very_easy) AND (test_success IS very_good) THEN (Knowledge IS enough)"
        R5 = "IF (test_difficulty IS very_easy) AND (test_success IS excellent) THEN (Knowledge IS enough)"
        R6 = "IF (test_difficulty IS easy) AND (test_success IS bad) THEN (Knowledge IS not_enough)"
        R7 = "IF (test_difficulty IS easy) AND (test_success IS not_bad) THEN (Knowledge IS not_enough)"
        R8 = "IF (test_difficulty IS easy) AND (test_success IS good) THEN (Knowledge IS enough)"
        R9 = "IF (test_difficulty IS easy) AND (test_success IS very_good) THEN (Knowledge IS enough)"
        R10 = "IF (test_difficulty IS easy) AND (test_success IS excellent) THEN (Knowledge IS enough)"
        R11 = "IF (test_difficulty IS middle) AND (test_success IS bad) THEN (Knowledge IS not_enough)"
        R12 = "IF (test_difficulty IS middle) AND (test_success IS not_bad) THEN (Knowledge IS not_enough)"
        R13 = "IF (test_difficulty IS middle) AND (test_success IS good) THEN (Knowledge IS enough)"
        R14 = "IF (test_difficulty IS middle) AND (test_success IS very_good) THEN (Knowledge IS enough)"
        R15 = "IF (test_difficulty IS middle) AND (test_success IS excellent) THEN (Knowledge IS enough)"
        R16 = "IF (test_difficulty IS difficult) AND (test_success IS bad) THEN (Knowledge IS not_enough)"
        R17 = "IF (test_difficulty IS difficult) AND (test_success IS not_bad) THEN (Knowledge IS not_enough)"
        R18 = "IF (test_difficulty IS difficult) AND (test_success IS good) THEN (Knowledge IS enough)"
        R19 = "IF (test_difficulty IS difficult) AND (test_success IS very_good) THEN (Knowledge IS enough)"
        R20 = "IF (test_difficulty IS difficult) AND (test_success IS excellent) THEN (Knowledge IS enough)"
        R21 = "IF (test_difficulty IS very_difficult) AND (test_success IS bad) THEN (Knowledge IS not_enough)"
        R22 = "IF (test_difficulty IS very_difficult) AND (test_success IS not_bad) THEN (Knowledge IS enough)"
        R23 = "IF (test_difficulty IS very_difficult) AND (test_success IS good) THEN (Knowledge IS enough)"
        R24 = "IF (test_difficulty IS very_difficult) AND (test_success IS very_good) THEN (Knowledge IS enough)"
        R25 = "IF (test_difficulty IS very_difficult) AND (test_success IS excellent) THEN (Knowledge IS enough)"
        
        

        FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25])
        FS.set_variable("test_difficulty", 40)

        FS.set_variable("test_success", 75)

        # Perform Sugeno inference and print output
        print(FS.Sugeno_inference(["Knowledge"]))
        
        
        
        
    
    def Fuzzyfier(self):
        
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