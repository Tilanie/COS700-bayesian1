import json
import copy
import random
import csv
import pandas as pd
import os.path
from SkillPredictor import SkillPredictor
from Fuzzy import Fuzzy

class StudentSimulator:
    def __init__(self, seed = 1, fuzzy = False):
        self.knowledge = None   
        self.seed = seed
        self.fuzzy_used = fuzzy
        random.seed(self.seed)
        # self.studentIds = ['1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011', '1012', '1013', '1014', '1015', '1016']
        self.studentIds = ['9000', '9001']
        self.studentKnowledge = []
        if fuzzy == True:
            self.fuzzy = Fuzzy()
        

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
            

            file_exists = os.path.exists('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json')

            if file_exists == True:
                f = open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json',)
            else:
                f = open('BayesianData.json',)
            
            self.data = json.load(f)
            self.knowledge = copy.deepcopy(self.data)
            self.knowledge = self.prepareStudentKnowledge()
            self.knowledgeInternal = copy.deepcopy(self.data)
            self.proficiencies = []
            self.dc = []
            gender = self.generateGender()
      
            for i in self.knowledge['concepts']: # set all the terminal nodes
                proficiency = self.getTestValuesAverageConcept(sid, i['id'])
                self.proficiencies.append(proficiency)
                degree_careful = self.generateDegreeCarefullness()
                i['degreeCarefull'] = degree_careful
                self.dc.append(degree_careful)
                i['proficiency'] = proficiency
                i['gender'] = gender
                # Concept ID	Gender	Age	SchoolClass	DegreeCarefulness	Proficiency
                # if i['terminal'] == 1: #no dependancies
                #     i['known'] = self.generateKnown()
                known = self.getTestValuesAverageConcept(sid, i['id'])
                i['known'] = known
                
          
            age = self.generateAge()
            clasId = self.generateCLassID(age)
            for i in self.knowledge['concepts']:
                known = self.getTestValuesAverageConcept(sid, i['id'])
               
                i['known'] = known
                    
                i['learnt'] = 0
                i['age'] = age
                i['classID'] = clasId
                
            count = 0
            for i in self.knowledgeInternal['concepts']: 
                gender = self.generateGender()
                i['proficiency'] = self.proficiencies[count]
                i['degreeCarefull'] = self.dc[count]
                i['gender'] = gender
                known = self.getTestValuesAverageConcept(sid, i['id'])
            
                i['known'] = known
                i['learnt'] = 0
                i['age'] = age
                i['classID'] = clasId
                count = count + 1
                

            with open('StudentKnowledge/KnowledgeMap' + str(sid) + '.json', 'w') as outfile:
                json.dump(self.knowledge, outfile)

            with open('StudentKnowledge/KnowledgeMapLearnt' + str(sid) + '.json', 'w') as outfile:
                json.dump(self.knowledgeInternal, outfile)
            
            self.studentKnowledge.append(self.knowledgeInternal)
            
    def getTestValuesAverageConcept(self, id, concept):
        self.dataset = pd.read_csv('TestData/student' + str(id), delimiter=',', header=None)
   
        for row in self.dataset.values:
           
            if int(row[3]) == int(concept):
                average = (row[0] + row[1] + row[2] + row[5]) / 4
                
      
        if self.fuzzy_used == True:
            average = average * 2.0
           
            average = self.fuzzy.predict(average) + 0.15
         
        return average
        
    def generateCLassID(self, age):
        self.seed = self.seed + 1
        random.seed(self.seed)
        
        if age > 17:
            choice = random.randint(0, 100)
            if choice > 85:
                id = 5
            else:
                id = 6
        elif age == 17:
            choice = random.randint(0, 100)
            if choice > 85:
                id = 6
            elif choice > 15:
                id = 5
            else:
                id = 4
        elif age == 16:
            choice = random.randint(0, 100)
            if choice > 85:
                id = 5
            elif choice > 15:
                id = 4
            else:
                id = 3
        elif age == 15:
            choice = random.randint(0, 100)
            if choice > 85:
                id = 4
            elif choice > 15:
                id = 3
            else:
                id = 2
        elif age == 14:
            choice = random.randint(0, 100)
            if choice > 85:
                id = 3
            elif choice > 15:
                id = 2
            else:
                id = 1
        else:
            choice = random.randint(0, 100)
            if choice > 85:
                id = 2
            else:
                id = 1
        return id
           
            
    def generateAge(self):
        age_choice = 0
        for i in self.knowledge['concepts']:
            if i['proficiency'] > 0.75:
                if int(str(i['id'])[:1]) >= 4:
                    age_choice = age_choice + 4
                elif int(str(i['id'])[:1]) >= 3:
                    age_choice = age_choice + 3
                elif int(str(i['id'])[:1]) >= 2:
                    age_choice = age_choice + 2
                elif int(str(i['id'])[:1]) >= 1:
                    age_choice = age_choice + 1
            elif i['proficiency'] > 0.5:
                if int(str(i['id'])[:1]) >= 4:
                    age_choice = age_choice + 2
                elif int(str(i['id'])[:1]) >= 3:
                    age_choice = age_choice + 1
                elif int(str(i['id'])[:1]) >= 2:
                    age_choice = age_choice + 0
                elif int(str(i['id'])[:1]) >= 1:
                    age_choice = age_choice - 1
            elif i['proficiency'] > 0.25:
                if int(str(i['id'])[:1]) >= 4:
                    age_choice = age_choice + 0
                elif int(str(i['id'])[:1]) >= 3:
                    age_choice = age_choice - 1
                elif int(str(i['id'])[:1]) >= 2:
                    age_choice = age_choice -2
                elif int(str(i['id'])[:1]) >= 1:
                    age_choice = age_choice - 3
            else:
                if int(str(i['id'])[:1]) >= 4:
                    age_choice = age_choice -1
                elif int(str(i['id'])[:1]) >= 3:
                    age_choice = age_choice -2
                elif int(str(i['id'])[:1]) >= 2:
                    age_choice = age_choice  -3
                elif int(str(i['id'])[:1]) >= 1:
                    age_choice = age_choice - 4
            
        age_choice = age_choice + 428 # normalize
        
        self.seed = self.seed + 1
        random.seed(self.seed)
   
        if age_choice <= 214:
            age = random.randint(0,5)
            if age > 3:
                age = 13
            else:
                age = 14
       
        elif age_choice <= 428:
            age = random.randint(14, 15)
  
        elif age_choice <= 642:
            age = random.randint(15, 16)
  
        else:
            age = random.randint(0,6)
            if age > 5:
                age = 19
            elif age > 2:
                age = 18
            else:
                age= 17
                
        return age
        
    
    def generateGender(self):
        self.seed = self.seed + 1
        random.seed(self.seed)
        choice = random.randint(0,1)
        if choice == 0:
            return 'Male'
        else:
            return 'Female'
        
    


    
    def generateDegreeCarefullness(self):
        self.seed = self.seed + 1
        random.seed(self.seed)
        return random.randint(0,1)
    

    


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


    
