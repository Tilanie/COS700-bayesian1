
from NeuralNetwork import NeuralNetwork
from BugLibrary import BugLibrary
from Bayesian import Bayesian
from FuzzyKnowledgePredictor import FuzzyKnowledgePredictor

class StudentKnowledge:
    def __init__(self):
        self.Bayesian = Bayesian()
        self.NeuralNetwork = NeuralNetwork()
        self.FuzzyKnowledgePredictor = FuzzyKnowledgePredictor()
    # Could implemented as either a Bayesian or a Neural Network