from StudentModel import StudentModel
from StudentSimulator import StudentSimulator
from NeuralNetwork import NeuralNetwork

seed = 2
method = 2

studentSimulator = StudentSimulator()
studentSimulator.generateStudentData()
studentModel = StudentModel("Tilanie", 1001, "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, method)
wait = input("first learning")
studentModel.learn()
wait = input("second learning")
studentModel.learn()

