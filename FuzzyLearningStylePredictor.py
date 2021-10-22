from simpful import *

class FuzzyLearningStylePredictor:
    def __init__(self):
        self.fuzzy_predictor = FuzzyPredictor()
    
    def FuzzyPredictor(self):
        FS = FuzzySystem()
        # Define fuzzy sets and linguistic variables
        S_1 = FuzzySet(points=[[0., 1.], [35., 1.], [65., 0.]], term="less")
        S_2 = FuzzySet(points=[[35., 0.], [65., 1.], [100., 1.]], term="more")
        
        FS.add_linguistic_variable("mousemove", LinguisticVariable([S_1, S_2], concept="Mouse Movements"))
        
        
        S_3 = FuzzySet(points=[[0., 1.], [35., 1.], [65., 0.]], term="less")
        S_4 = FuzzySet(points=[[35., 0.], [65., 1.], [100., 1.]], term="more")
        
        FS.add_linguistic_variable("doclentime", LinguisticVariable([S_3, S_4], concept="Document Length Time"))
        
        S_5 = FuzzySet(points=[[0., 1.], [35., 1.], [65., 0.]], term="less")
        S_6 = FuzzySet(points=[[35., 0.], [65., 1.], [100., 1.]], term="more")
        
        FS.add_linguistic_variable("imagedoclen", LinguisticVariable([S_5, S_6], concept="Image Document Length"))
        
        S_7 = FuzzySet(points=[[0., 1.], [35., 1.], [65., 0.]], term="less")
        S_8 = FuzzySet(points=[[35., 0.], [65., 1.], [100., 1.]], term="more")
        
        FS.add_linguistic_variable("visitsdoc", LinguisticVariable([S_9, S_10, S_11, S_12, S_13], concept="Visit Document"))
        
        
        FS.set_crisp_output_value("not_enough", 0)
        FS.set_crisp_output_value("enough", 1)
        
        
        # Define fuzzy rules
        R1 = "IF (mousemove IS more) AND (doclentime IS more) AND (imagedoclen IS more) AND (visitsdoc IS more) THEN (student IS reflective)"
        R2 = "IF (mousemove IS less) AND (doclentime IS less) AND (imagedoclen IS less) AND (visitsdoc IS less) THEN (student IS active)"
        R3 = "IF (mousemove IS less) AND (doclentime IS less) AND (imagedoclen IS less) AND (visitsdoc IS more) THEN (student IS mactive)"
        R4 = "IF (mousemove IS less) AND (doclentime IS less) AND (imagedoclen IS more) AND (visitsdoc IS less) THEN (student IS mactive)"
        R5 = "IF (mousemove IS less) AND (doclentime IS more) AND (imagedoclen IS less) AND (visitsdoc IS less) THEN (student IS mactive)"
        R6 = "IF (mousemove IS more) AND (doclentime IS less) AND (imagedoclen IS less) AND (visitsdoc IS less) THEN (student IS mactive)"
        R7 = "IF (mousemove IS more) AND (doclentime IS more) AND (imagedoclen IS more) AND (visitsdoc IS less) THEN (student IS mreflective)"
        R8 = "IF (mousemove IS more) AND (doclentime IS more) AND (imagedoclen IS less) AND (visitsdoc IS more) THEN (student IS mreflective)"
        R9 = "IF (mousemove IS more) AND (doclentime IS less) AND (imagedoclen IS more) AND (visitsdoc IS more) THEN (student IS mreflective)"
        R10 = "IF (mousemove IS less) AND (doclentime IS more) AND (imagedoclen IS more) AND (visitsdoc IS more) THEN (student IS mreflective)"
        
        R11 = "IF (mousemove IS less) AND (doclentime IS less) THEN (student IS active)"
        R12 = "IF (imagedoclen IS less) AND (visitsdoc IS less) THEN (student IS active)"
        R13 = "IF (mousemove IS less) AND (doclentime IS more) THEN (student IS reflective)"
        R14 = "IF (imagedoclen IS more) AND (visitsdoc IS less) THEN (student IS reflective)"
        R15 = "IF (mousemove IS more) AND (doclentime IS more) THEN (student IS mreflective)"
        R16 = "IF (mousemove IS more) AND (doclentime IS more) THEN (student IS rmactive)"
        R17 = "IF (imagedoclen IS more) AND (visitsdoc IS less) THEN (student IS mactive)"
        R18 = "IF (imagedoclen IS less) AND (visitsdoc IS more) THEN (student IS mreflective)"
        
        R19 = "IF (mousemove IS less) AND (doclentime IS less) AND (imagedoclen IS more) AND (visitsdoc IS more) THEN (student IS mreflective)"
        R20 = "IF (mousemove IS more) AND (doclentime IS less) AND (imagedoclen IS more) AND (visitsdoc IS more) THEN (student IS mreflective)"
        R21 = "IF (mousemove IS more) AND (doclentime IS more) AND (imagedoclen IS less) AND (visitsdoc IS more) THEN (student IS mactive)"
        R22 = "IF (mousemove IS less) AND (doclentime IS more) AND (imagedoclen IS more) AND (visitsdoc IS less) THEN (student IS mactive)"
        
        R23 = "IF (mousemove IS less) AND (visitsdoc IS less) THEN (student IS active)"
        R24 = "IF (mousemove IS less) AND (visitsdoc IS more) THEN (student IS mreflective)"
        R25 = "IF (mousemove IS more) AND (visitsdoc IS less) THEN (student IS mactive)"
        R26 = "IF (mousemove IS more) AND (visitsdoc IS more) THEN (student IS reflective)"
        R27 = "IF (doclentime IS less) AND (imagedoclen IS less) THEN (student IS mreflective)"
        R28 = "IF (doclentime IS more) AND (imagedoclen IS more) THEN (student IS mactive)"
        R29 = "IF (doclentime IS more) AND (imagedoclen IS less) THEN (student IS active)"
        R30 = "IF (doclentime IS less) AND (imagedoclen IS more) THEN (student IS reflective)"

        FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30])
        
        FS.set_variable("mousemove", 40)

        FS.set_variable("doclentime", 75)
        
        FS.set_variable("imagedoclen", 40)

        FS.set_variable("visitsdoc", 75)

        # Perform Sugeno inference and print output
     
        
        
  