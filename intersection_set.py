#QUESTION:


'''
.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).
'''



#CODE:
  
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.intersection(b)))
