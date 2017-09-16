wordyWord = '2-4a0r7-4k'

# --------------------------------------------------------------------------------------------------------------------------
# BAD WAY DOESNT WORK FOR SOME
# def stringReformatting(st, k):
#     returnString = ''
#     groupPos = 0
#     # go backwards
#     for letter in st[::-1]:
#         add=False
#         if letter != '-' and groupPos != k or letter == st[0]: #error here where letter can be repeated in the begginning and middle
#             returnString+=letter
#         elif letter != '-' and groupPos == k and letter != st[0]:
#             add=True
#             returnString+= letter + '-'
#         groupPos+= 1 if not add else -(k-1)#
#     return returnString[::-1] # cause i went backwards go backwards again
#
# print "'%s',1 output: "%wordyWord + stringReformatting(wordyWord,1) #doesnt work here
# print "'%s',2 output: "%wordyWord + stringReformatting(wordyWord,2) # doesnt work here
# print "'%s',3 output: "%wordyWord + stringReformatting(wordyWord,3)
# print "'%s',4 output: "%wordyWord +  stringReformatting(wordyWord,4)

# --------------------------------------------------------------------------------------------------------------------------
# NOTE: might be index out of bounce, but it's ok in python
# other way (i had the idea after the previous one)
# find number of groups there should be and from there find the positions to have place the '-'
def stringReformatting(st, k):
    groups = ''.join(st.split('-')) #remove all dashes
    totalLetter = len(groups)
    splitTotal = totalLetter/k
    if totalLetter%k > 0:
        splitTotal +=1 # the extra group
    for dashIndex in range(1,splitTotal): # dashes is = number of groups - 1
        groups = groups[:totalLetter-(dashIndex*k)] + '-' +  groups[totalLetter-(dashIndex*k):] #goes backwards so as not to mess up the index
    return groups

print 'going in reverse way'
print "'%s',1 output: "%wordyWord + stringReformatting(wordyWord,1)
print "'%s',2 output: "%wordyWord + stringReformatting(wordyWord,2)
print "'%s',3 output: "%wordyWord + stringReformatting(wordyWord,3)
print "'%s',4 output: "%wordyWord +  stringReformatting(wordyWord,4)
print "'%s',5 output: "%wordyWord +  stringReformatting(wordyWord,5)
print "'%s',6 output: "%wordyWord +  stringReformatting(wordyWord,6)
print "'%s',7 output: "%wordyWord +  stringReformatting(wordyWord,7)
print "'%s',8 output: "%wordyWord +  stringReformatting(wordyWord,8)
print "'%s',9 output: "%wordyWord +  stringReformatting(wordyWord,9)
print

# --------------------------------------------------------------------------------------------------------------------------
# NOTE: might be index out of bounce, but it's ok in python
# other other way..... going forward
def stringReformatting(st, k):
    groups = ''.join(st.split('-'))
    totalLetter = len(groups)
    # make first group
    curIndex = (totalLetter%k) if (totalLetter%k) != 0 else k
    returnString = groups[:curIndex]
    prevIndex=curIndex
    curIndex+=k
    # make rest of group
    while curIndex <= totalLetter:
        returnString+='-' + groups[prevIndex:curIndex]
        prevIndex=curIndex
        curIndex+=k
    return returnString

print 'going in forward way'
print "'%s',1 output: "%wordyWord + stringReformatting(wordyWord,1)
print "'%s',2 output: "%wordyWord + stringReformatting(wordyWord,2)
print "'%s',3 output: "%wordyWord + stringReformatting(wordyWord,3)
print "'%s',4 output: "%wordyWord +  stringReformatting(wordyWord,4)
print "'%s',5 output: "%wordyWord +  stringReformatting(wordyWord,5)
print "'%s',6 output: "%wordyWord +  stringReformatting(wordyWord,6)
print "'%s',7 output: "%wordyWord +  stringReformatting(wordyWord,7)
print "'%s',8 output: "%wordyWord +  stringReformatting(wordyWord,8)
print "'%s',9 output: "%wordyWord +  stringReformatting(wordyWord,9)
