

class ConceptHistory:
    def __init__(self, title, id, experience_level, knowledge_level, duration, num_passes):
        self.title = title
        self.id = id
        self.experience_level = experience_level
        self.knowledge_level = knowledge_level
        self.duration = duration
        self.num_passes = num_passes
        
        
class TestHistory:
    def __init__(self, id, difficulty_level, degree_of_mastery, knowledge_level, success, duration):
        self.id = id
        self.difficulty_level = difficulty_level
        self.degree_of_mastery = degree_of_mastery
        self.knowledge_level = knowledge_level
        self.success = success
        self.duration = duration
        
class UnitHistory:
    def __init__(self, title, id, duration):
        self.title = title
        self.id = id
        self.duration = duration
        