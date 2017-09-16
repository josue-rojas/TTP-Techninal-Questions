import re

sentence = 'Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.'

# function for testing
def runFunctions():
    print 'arrays:'
    print [a.start(0) for a in  re.finditer(r'\(', sentence)]
    print [a.start(0) for a in  re.finditer(r'\)', sentence)]
    print comment
    print getClosingParen(sentence, 10)
    print getClosingParen(sentence, 28)
    print getClosingParen(sentence, 57)
    print getClosingParen(sentence, 68)
    print getClosingParen(sentence, 8)

# DONT WORK CAUSE ASSUME NO MIDDLE CLOSING LIKE (()()())
# --------------------------------------------------------------------------------------------------------------------------
# comment = 'find all the index of opening and closing paranthesis, put them in list \ntheir position on index is backwards position of the closing'
# def getClosingParen(sentence, openingParenIndex):
#     indexOpen = [a.start(0) for a in  re.finditer(r'\(', sentence)]
#     indexClose = [a.start(0) for a in  re.finditer(r'\)', sentence)]
#     # make sure they are even and paranthesis exist
#     if len(indexOpen) != len(indexClose) or openingParenIndex not in indexOpen:
#         return -1
#     return indexClose[-(indexOpen.index(openingParenIndex)+1)]
#
# runFunctions()
#
# --------------------------------------------------------------------------------------------------------------------------
# comment = 'same but  shorter return just cause'
# def getClosingParen(sentence, openingParenIndex):
#     indexOpen = [a.start(0) for a in  re.finditer(r'\(', sentence)]
#     indexClose = [a.start(0) for a in  re.finditer(r'\)', sentence)]
#     return -1 if len(indexOpen) != len(indexClose) or openingParenIndex not in indexOpen else indexClose[-(indexOpen.index(openingParenIndex)+1)]
# # runFunctions()
# --------------------------------------------------------------------------------------------------------------------------
comment = 'using push and pop starting at the beginnign \n(assumes even)'
def getClosingParen(sentence, openingParenIndex):
    curIndex = 0
    openPar = []
    for letter in sentence:
        if letter == '(':
            openPar.append(curIndex)
        elif letter == ')':
            if openPar[-1] == openingParenIndex:
                return curIndex
            openPar.pop()
        curIndex+=1
    return -1 # none found

runFunctions()

# --------------------------------------------------------------------------------------------------------------------------
comment = 'using push and pop, but starting from the index \n(assumes even)'
def getClosingParen(sentence, openingParenIndex):
    # starting is not opening paranthesis
    if sentence[openingParenIndex] != '(':
        return -1
    curIndex = openingParenIndex
    openPar = []
    for letter in sentence[openingParenIndex:]:
        if letter == '(':
            openPar.append(curIndex)
        elif letter == ')':
            openPar.pop()
            if len(openPar) == 0:
                return curIndex
        curIndex+=1
    return -1 # none found

runFunctions()
