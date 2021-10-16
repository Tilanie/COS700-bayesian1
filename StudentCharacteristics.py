from TeachingHistory import ConceptHistory, TestHistory, UnitHistory
from SkillPredictor import SkillPredictor
import json

class StudentCharacteristics:
    def __init__(self, name, id, username, password, email, language, city, country):
        self.personalData = self.PersonalData(name, id, username, password, email, language, city, country)
        self.user_record = []
  
        self.performanceData = self.PerformanceData(self.user_record)
        self.teachingHistory = self.TeachingHistory()

        
    def getPersonalData(self, id, concept):
        f = open('knowledgeMap' + str(id) + '.json',)
        self.data = json.load(f)
        
        for i in self.data['concepts']:
            if i['id'] == concept['id']:
                gender = i['gender']
                age = i['age']
                degree_careful = i['degreeCarefull']
                class_id = i['classID'] 
                proficiency = i['proficiency']
                
        
            
        
    class PersonalData:
        def __init__(self, name, id, username, password, email, language, city, country):
            self.name = name
            self.id = id
            self.username = username
            self.password = password
            self.email = email
            self.language = language
            self.city = city
            self.country = country
            
    class PerformanceData:
        def __init__(self, user_record):
            self.user_record = user_record
            self.time = 0
            self.id = 0
            self.detail_level = 0
            self.session_number = 0
            self.learning_style = ''
            self.init_skill_level = 0
           
        
            
        
    class TeachingHistory:
        def __init__(self):
            self.concept_history = []
            self.test_history = []
            self.unit_history = []
    
               
        