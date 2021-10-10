from StudentModel import StudentModel

StudentModel = StudentModel("Tilanie", 12, "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA")

vals = StudentModel.predictStudentKnowledge('Midpoints')
print("Student Model")
print(vals)