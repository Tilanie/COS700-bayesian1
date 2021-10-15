import json
import copy
import random
import csv

class StudentSimulator:
    def __init__(self, seed = 1):
        self.knowledge = None   
        self.seed = seed
        random.seed(self.seed)
        # self.studentIds = ['1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011', '1012', '1013', '1014', '1015', '1016']
        self.studentIds = ['9000', '9001']
        self.studentKnowledge = []
        

    def createTestData(self):
        self.studentIds = ['9000', '9001', '9002', '9003', '9004', '9005', '9006', '9007', '9008', '9009', '9010', '9011', '9012', '9013', '9014', '9015', '9016', '9017', '9018', '9019', '9020']
        self.generateStudentKnowledge()
        self.generateTestData()

    def generateStudentData(self):
        self.studentIds = ['1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011']
        self.generateStudentKnowledge()
        self.generateTestData()

    def generateStudentKnowledge(self):
        for sid in self.studentIds:
            f = open('BayesianData.json',)
            self.data = json.load(f)
            self.knowledge = copy.deepcopy(self.data)
            self.knowledge = self.prepareStudentKnowledge()
            self.knowledgeInternal = copy.deepcopy(self.data)

            for i in self.knowledge['concepts']: # set all the terminal nodes
                if i['terminal'] == 1: #no dependancies
                    i['known'] = self.generateKnown()
                
            for i in self.knowledge['concepts']:
                if i['terminal'] == 0:
                    known = self.percentageChildrenKnown(i['children'])
                    i['known'] = self.generateKnownPercentage(known)
                i['learnt'] = 0
                
            for i in self.knowledgeInternal['concepts']: 
                i['known'] = 0
                i['learnt'] = 0

            with open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json', 'w') as outfile:
                json.dump(self.knowledge, outfile)

            with open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json', 'w') as outfile:
                json.dump(self.knowledgeInternal, outfile)
            
            self.studentKnowledge.append(self.knowledge)

    def percentageChildrenKnown(self, children):
        num_children = len(children)
        num_known = 0
        for c in children:
            for i in self.knowledge['concepts']: # set all the terminal nodes
                if i['id'] == c['id'] and i['terminal'] == 1: #no dependancies
                    num_known = num_known + 1

        return float(num_known) / num_children

    def prepareStudentKnowledge(self):
        for i in self.knowledge['concepts']:
            i['known'] = 0

        return self.knowledge

    def generateKnown(self):
        self.seed = self.seed + 1
        random.seed(self.seed)
        known = random.randint(0, 1)
        return known

    def generateKnownPercentage(self, chance):
        self.seed = self.seed + 1
        random.seed(self.seed)
        choice = random.uniform(0, chance)
        return choice

    def generateTestData(self):
        # open the file in the write mode

        index = 0
        for sid in self.studentIds:
            f = open('TestData/student' + sid, 'w', newline='')

            # create the csv writer
            writer = csv.writer(f)
            for i in self.studentKnowledge[index]['concepts']:
                
                test1 = self.generateTestScore(i['known'], i['sequence'])
                test2 = self.generateTestScore(i['known'], i['sequence'])
                test3 = self.generateTestScore(i['known'], i['sequence'])

                
                sequence = i['sequence']
                concept = i['id']

                chance_known = self.generateChanceKnown(test1, test2, test3)
                test1 = test1 / 100
                test2 = test2 / 100
                test3 = test3 / 100
                chance_known = chance_known / 100
                
                row = []
                row.append(test1)
                row.append(test2)
                row.append(test3)
                row.append(concept)
                row.append(sequence)
                row.append(chance_known)
            # write a row to the csv file
        
                writer.writerow(row)

            # close the file
            f.close()
            index = index + 1

    def generateChanceKnown(self, test1, test2, test3):
        self.seed = self.seed + 1 
        random.seed(self.seed)
        average = (test1 + test2 + test3) / 3
        variance_value = random.uniform(-1 * (0.15 * average), 0.15 * average)
        test_value = average + variance_value

        return test_value

    def generateTestScore(self, known, sequence):
        self.seed = self.seed + 1
        random.seed(self.seed)

        if known == 1: #concept is known
            score = 50 + random.randint(0, (27 - sequence)) + random.randint(0, 23)
        else:
            score = random.randint(0, (27 - sequence)) + random.randint(0, 23)

        return score


    
