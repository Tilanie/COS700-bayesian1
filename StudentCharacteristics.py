from TeachingHistory import ConceptHistory, TestHistory, UnitHistory
from SkillPredictor import SkillPredictor

class StudentCharacteristics:
    def __init__(self):
        self.PersonalData = self.PersonalData("Tilanie", 12, "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA")
        self.user_record = [11, 'Female', 24, 1 ,0, 0.50]
        self.PerformanceData = self.PerformanceData(self.user_record)
        self.TeachingHistory = self.TeachingHistory()

        
        
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
            self.SkillPredictor = SkillPredictor(self.user_record)
            self.init_skill = self.SkillPredictor.predictSkill()

            
        
    class TeachingHistory:
        def __init__(self):
            self.concept_history = []
            self.test_history = []
            self.unit_history = []
    
               
        