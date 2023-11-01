import sys
from utilities import *


if __name__ == "__main__":
    if 'advance' == sys.argv[1]:
        path = "./input/advance/input{0}.txt".format(sys.argv[2])
        level = 'advance'
    else:    
        path = "./input/level_{0}/input{1}.txt".format(sys.argv[1],sys.argv[2])
        level =  "level_" + sys.argv[1]
    algName = sys.argv[3]
    # if "heuristic" in algName:
    algo = alg[algName]
    algName = algName.replace('_heuristic_1', '') 
    algName = algName.replace('_heuristic_2', '')
    input = "input" + sys.argv[2]
    print("exploredualizing {} on input {}".format(algName,path))
    path_finding(path,algo, algName, level, input)

