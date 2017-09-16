import random
a = [random.randint(1,101) for x in range(10)]
b = [random.randint(1,101) for x in range(10)]
v = random.randint(1,101)

def sumOfTwo(a,b,v):
    for num in a:
        if v-num in b:
            return True
    return False

print 'unsorted list find sum'
print 'list a: ' + str(a)
print 'list b: ' + str(b)
print 'sum: ' + str(v)
print 'is there a sum?: '+ str(sumOfTwo(a,b,v))
