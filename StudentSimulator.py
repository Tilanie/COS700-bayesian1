import json
import copy
import random

class StudentSimulator:
    def __init__(self, seed = 1):
        self.knowledge = None   
        self.seed = seed
        random.seed(self.seed)

    def generateStudentKnowledge(self):
        f = open('BayesianData.json',)
        self.data = json.load(f)
        self.knowledge = copy.deepcopy(self.data)
        self.knowledge = self.prepareStudentKnowledge()
        
        for i in self.knowledge['concepts']: # set all the terminal nodes
            if i['terminal'] == 1: #no dependancies
                i['known'] = self.generateKnown()
        

        with open('KnowledgeMap' + str(self.id) + '.json', 'w') as outfile:
            json.dump(self.data, outfile)

    def percentageChildrenKnown(self, children):
        pass

    def prepareStudentKnowledge(self):
        for i in self.knowledge['concepts']:
            i['known'] = 0

        return self.knowledge

    def generateKnown(self):
        self.seed = self.seed + 1
        known = random.randint(0, 1)
        return known

    def generateKnownPercentage(self, chance):
        self.seed = self.seed + 1
        random.seed(self.seed)
        choice = random.randint(0, 100)
        if (choice / 100) < chance:
            return 1
        else:
            return 0
