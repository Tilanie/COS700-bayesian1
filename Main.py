from StudentModel import StudentModel
from StudentSimulator import StudentSimulator
from NeuralNetwork import NeuralNetwork
seed = 2
method = 0
use_stereotype = True
fuzzy_used = False
num_learning = 10

def useBayesian(sid):
    use_stereotype = False
    studentSimulator = StudentSimulator(seed)
    studentSimulator.generateStudentData()
    studentModel = StudentModel("Tilanie", int(sid), "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, 0, use_stereotype)
    for i in range(0, num_learning):
        studentModel.learn()

    final_knowledge = studentModel.finalTotalKnowledge(0)
    print("-------------- final_knowledge ----------------")
    print(final_knowledge)
    writeToFile(sid, final_knowledge, 'Bayesian Network', use_stereotype, seed)
    use_stereotype = True
    studentSimulator = StudentSimulator(seed)
    studentSimulator.generateStudentData()
    studentModel = StudentModel("Tilanie", int(sid), "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, 0, use_stereotype)
    for i in range(0, num_learning):
        studentModel.learn()

    final_knowledge = studentModel.finalTotalKnowledge(0)
    print("-------------- final_knowledge ----------------")
    print(final_knowledge)
    writeToFile(sid, final_knowledge, 'Bayesian Network and Self-organising Maps', use_stereotype, seed)


def useNeuralNetwork(sid):
    use_fuzzy = False
    use_stereotype = False
    studentSimulator = StudentSimulator(seed)
    studentSimulator.generateStudentData()
    studentModel = StudentModel("Tilanie", int(sid), "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, 1, use_stereotype, use_fuzzy)
    for i in range(0, num_learning):
        studentModel.learn()

    final_knowledge = studentModel.finalTotalKnowledge(0)
    print("-------------- final_knowledge ----------------")
    print(final_knowledge)
    writeToFile(sid, final_knowledge, 'Neural Network', use_fuzzy, seed)

    use_fuzzy = True
    use_stereotype = False
    studentSimulator = StudentSimulator(seed, use_fuzzy)
    studentSimulator.generateStudentData()
    studentModel = StudentModel("Tilanie", int(sid), "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, 1, use_stereotype, use_fuzzy)
    for i in range(0, num_learning):
        studentModel.learn()

    final_knowledge = studentModel.finalTotalKnowledge(0)
    print("-------------- final_knowledge ----------------")
    print(final_knowledge)
    writeToFile(sid, final_knowledge, 'Neural Network and Fuzzy Network', use_fuzzy, seed)

def useStandard(sid):
    studentSimulator = StudentSimulator(seed)
    studentSimulator.generateStudentData()
    use_stereotype = False
    studentModel = StudentModel("Tilanie", int(sid), "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, 2, use_stereotype)
    for i in range(0, num_learning):
        studentModel.learn()

    final_knowledge = studentModel.finalTotalKnowledge(0)
    print("-------------- final_knowledge ----------------")
    print(final_knowledge)
    writeToFile(sid, final_knowledge, 'Standard Model', use_stereotype, seed)

def writeToFile(sid, result, technique, additional_used, seed):
    f = open("Results/data2.txt", "a")
    f.write(" ------------------------------ \n")
    f.write("SEED: " + str(seed))
    f.write('\n')
    f.write("STUDENT ID: " + str(sid))
    f.write('\n')
    f.write("TECHNIQUE USED: " + str(technique))
    f.write('\n')
    f.write("ADDITIONAL TECHNIQUE USED: " + str(additional_used))
    f.write('\n')
    f.write("-- FINAL RESULT: " + str(result))
    f.write('\n')
    f.write('\n')
    f.close()

def run(seedp):
    seed = seedp
    

    studentIds = ['1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011']
    for sid in studentIds:
    

        useBayesian(sid)
        
        seed = seed + 1
        useNeuralNetwork(sid)

    
        seed = seed + 1
        useStandard(sid)

def testRun():
    studentSimulator = StudentSimulator(fuzzy_used)
    studentSimulator.generateStudentData()
    studentIds = ['1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011']
    use_stereotype = False
    method = 0
    use_fuzzy = True
    studentModel = StudentModel("Tilanie", int('1000'), "tbresler", "pass", "t@gmail.com", "English", "Pretoria", "SA", seed, method, use_stereotype, use_fuzzy)
    for i in range(0, 5):
        studentModel.learn()

        final_knowledge = studentModel.finalTotalKnowledge(0)
        print("-------------- final_knowledge ----------------")
        print(final_knowledge)

run(seed)
# testRun()

