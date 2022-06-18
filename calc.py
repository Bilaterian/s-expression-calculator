from ast import Break
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
        inputList.append(input[0: j])
        inputList.append(input[j + 1:])
    else:
        inputList = input.split(' ', 1)
    
    return inputList

def calculateResult(input):
    ##check if int
    if(input.isnumeric()):
        return input
    ##else try to parse
    elif(input[0] == '(' and input[-1] == ')'):
        if(len(input) <= 2):
            input = "input too short"
        else:
            input = input[1:-1]
            inputList = input.split(' ', 1)

            ##null checking needs to happen after split
            if(len(inputList) != 2):
                input = "not enough elements"
                return input
            
            ##split inputList[1] into two parts
            newList = splitExpr(inputList[1])
            
            ##check again for null
            if(len(newList) != 2):
                input = "not enough elements"
                return input
            
            inputList[1] = newList[0]
            inputList.append(newList[1])

            #recursive elements
            inputList[1] = calculateResult(inputList[1])
            inputList[2] = calculateResult(inputList[2])

            if(inputList[1].isnumeric() and inputList[2].isnumeric()):
                if(inputList[0] == "add"):
                    result = int(inputList[1]) + int(inputList[2])
                    input = str(result)
                elif(inputList[0] == "multiply"):
                    result = int(inputList[1]) * int(inputList[2])
                    input = str(result)
                else:
                    input = "invalid operator"
            else:
                input = "invalid input"
    else:
        input = "invalid input, not encased in parenthisis and not numeric"
    
    return input


if(argLen != 2):
    print("Expected single argument")
else:
    input = sys.argv[1]
    result = calculateResult(input)
    print(result)


##EXPR = INTEGER | ADD | MULTIPLY
##INTEGER = pp.Word(pp.nums)
##ADD = "(add " + EXPR + " " + EXPR + ")"
##MULTIPLY = "(multiply " + EXPR + " " + EXPR +")"