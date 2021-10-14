from StudentModel import StudentModel
from StudentSimulator import StudentSimulator
from NeuralNetwork import NeuralNetwork

# studentModel = StudentModel("Tilanie", 12, "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA")
studentSimulator = StudentSimulator()
studentSimulator.generateStudentData()
# vals = studentModel.predictStudentKnowledge('Midpoints')
# print("Student Model")
# print(vals)
neuralNetwork = NeuralNetwork()
neuralNetwork.predict([0.87,0.68,0.83,122,1])