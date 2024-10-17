import sys
from enum import Enum


i = 0
inputCodeLines = []
outputCodeLines = []

# citanje podataka iz dateoteke
for inputLine in sys.stdin:
    inputCodeLines.append(inputLine)

def asignNumAndIdn(activeToken):
    if activeToken == Tokens.BROJ:
        outputCodeLines.append("BROJ " + str(lineNumber) + " " + readChars)
    if activeToken == Tokens.IDN:
        outputCodeLines.append("IDN " + str(lineNumber) + " " + readChars)

# file = open("test11/test.in", "r")
# for line in file:
#     inputCodeLines.append(line)
# file.close()

class Tokens(Enum):
    IDN = 1
    BROJ = 2
    OP_PRIDRUZI = 3
    OP_PLUS = 4
    OP_MINUS = 5
    OP_PUTA = 6
    OP_DIJELI = 7
    L_ZAGRADA = 8
    D_ZAGRADA = 9
    KR_ZA = 10
    KR_OD = 11
    KR_DO = 12
    KR_AZ = 13
    NISTA = 14

activeToken = Tokens.NISTA
lineNumber = 0

for line in inputCodeLines:
    prevToken = Tokens.NISTA
    activeToken = Tokens.NISTA

    readChars = ""
    lineNumber += 1

    for char in line:
        if char == "/" and line[line.index(char) + 1] == "/":
            asignNumAndIdn(activeToken)
    
            break

        if char == "=":
            asignNumAndIdn(activeToken)
            outputCodeLines.append("OP_PRIDRUZI " + str(lineNumber) + " " + char)

            prevToken = Tokens.OP_PRIDRUZI
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if char == "*":
            asignNumAndIdn(activeToken)

            outputCodeLines.append("OP_PUTA " + str(lineNumber) + " " + char)

            prevToken = Tokens.OP_PUTA
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if char == "/":
            asignNumAndIdn(activeToken)

            outputCodeLines.append("OP_DIJELI " + str(lineNumber) + " " + char)

            prevToken = Tokens.OP_DIJELI
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if char == "+":
            asignNumAndIdn(activeToken)
            outputCodeLines.append("OP_PLUS " + str(lineNumber) + " " + char)

            prevToken = Tokens.OP_PLUS
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if char == "-":
            asignNumAndIdn(activeToken)
            
            outputCodeLines.append("OP_MINUS " + str(lineNumber) + " " + char)

            prevToken = Tokens.OP_MINUS
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if char == "\n":
            asignNumAndIdn(activeToken)

            if activeToken == Tokens.KR_AZ:
                outputCodeLines.append("KR_AZ " + str(lineNumber) + " " + readChars)
                
            break
        
        if char == "(":
            asignNumAndIdn(activeToken)

            outputCodeLines.append("L_ZAGRADA " + str(lineNumber) + " " + char)

            prevToken = Tokens.L_ZAGRADA
            activeToken = Tokens.NISTA
            readChars = ""
            continue
            
        if char == ")":
            asignNumAndIdn(activeToken)

            outputCodeLines.append("D_ZAGRADA " + str(lineNumber) + " " + char)
            
            prevToken = Tokens.D_ZAGRADA
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if char == " ":
            if prevToken == Tokens.KR_AZ:
                outputCodeLines.append("KR_AZ " + str(lineNumber) + " " + readChars)
                break

            if prevToken == Tokens.KR_ZA or prevToken == Tokens.KR_OD or prevToken == Tokens.OP_MINUS or prevToken == Tokens.OP_PLUS or prevToken == Tokens.OP_PUTA or prevToken == Tokens.OP_DIJELI:
                if activeToken == Tokens.BROJ:
                    outputCodeLines.append("BROJ " + str(lineNumber) + " " + readChars)
                    prevToken = Tokens.BROJ
                    activeToken = Tokens.NISTA
                    readChars = ""
                    continue
                elif activeToken == Tokens.IDN:
                    outputCodeLines.append("IDN " + str(lineNumber) + " " + readChars)   
                    prevToken = Tokens.IDN
                    activeToken = Tokens.NISTA
                    readChars = ""
                    continue
            

        if activeToken == Tokens.IDN and char == " " and prevToken == Tokens.KR_OD:
            outputCodeLines.append("BROJ " + str(lineNumber) + " " + readChars)
            prevToken = Tokens.IDN
            activeToken = Tokens.NISTA
            readChars = ""
            continue


        if readChars == "za" and char == " ":
            outputCodeLines.append("KR_ZA " + str(lineNumber) + " " + readChars)

            prevToken = Tokens.KR_ZA
            activeToken = Tokens.NISTA
            readChars = ""
            continue

        if readChars == "od" and char == " ":
            outputCodeLines.append("KR_OD " + str(lineNumber) + " " + readChars)

            prevToken = Tokens.KR_OD
            activeToken = Tokens.NISTA
            readChars = ""
            continue
        
        if readChars == "do" and char == " ":
            outputCodeLines.append("KR_DO " + str(lineNumber) + " " + readChars)

            prevToken = Tokens.KR_DO
            activeToken = Tokens.NISTA
            readChars = ""
            continue

         #ignoriramo praznine i tabulator
        if char == " " or char == "\t":
            continue

        if char.isdigit() and activeToken == Tokens.NISTA:
            activeToken = Tokens.BROJ

        if char.isalpha():
            if activeToken == Tokens.NISTA:
                activeToken = Tokens.IDN

            elif activeToken == Tokens.BROJ:
                asignNumAndIdn(activeToken)
                activeToken = Tokens.IDN
                prevToken = Tokens.BROJ
                readChars = ""


        #ucitavanje znaka u readChars ako se ne poklapa sa nijednim tokenom
        readChars += char

        if readChars == "az" and (line[line.index(char) + 1] == " " or line[line.index(char) + 1] == "\n"):
            activeToken = Tokens.KR_AZ
            

# if activeToken == Tokens.BROJ:
#     outputCodeLines.append("BROJ " + str(lineNumber) + " " + readChars)
# if activeToken == Tokens.IDN:
#     outputCodeLines.append("IDN " + str(lineNumber) + " " + readChars)
# if activeToken == Tokens.KR_AZ:
#     outputCodeLines.append("KR_AZ " + str(lineNumber) + " " + readChars)


for line in outputCodeLines:
    print(line)

# file = (open("test11/res.out", "w"))
# for line in outputCodeLines:
#     file.write(line + "\n")
    
# file.write("\n")
# file.close()
   