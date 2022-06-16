import pyparsing as pp
import sys

argLen = len(sys.argv)

def splitExpr(input):
    inputList = []
    if(input[0] == '('):
        #dothis
        i = 0
        j = 0
        for x in input:
            j = j + 1
            if(x == '('):
                i = i + 1
            elif(x == ')'):
                i = i - 1
            if(i == 0):
                break
        print("i = ",i)
        inputList.append(input[0: j])
        inputList.append(input[j + 1:])
    else:
        inputList = input.split(' ', 1)
    
    return inputList

def printResult(input):
    print("input: " + input)
    ##check if int
    if(input.isnumeric()):
        return input
    ##else try to parse
    elif(input[0] == '(' and input[-1] == ')'):
        input = input[1:-1]
        inputList = input.split(' ', 1)
        ##split inputList[1] into two parts
        newList = splitExpr(inputList[1])
        print("inputList",inputList)
        print("newList: ",newList)
        inputList[1] = newList[0]
        inputList.append(newList[1])
        print("inputList",inputList)


        if(inputList[0] == "add"):
            print("accessed")
    else:
        input = "invalid input"
    
    return input


if(argLen != 2):
    print("Expected single argument")
else:
    input = sys.argv[1]
    printResult(input)



##EXPR = INTEGER | ADD | MULTIPLY
##INTEGER = pp.Word(pp.nums)
##ADD = "(add " + EXPR + " " + EXPR + ")"
##MULTIPLY = "(multiply " + EXPR + " " + EXPR +")"