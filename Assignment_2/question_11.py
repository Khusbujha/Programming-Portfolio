"""This program performs the following operations on the sets:
(a) Print the union and its size.
(b) Print the difference of setA - setB.
(c) Print the intersection of both sets.
(d) Check whether setA is a subset of setB.
(e) Remove element 7 from setB and display the result.

"""

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print("Original sets:")
print("SetA=", setA)
print("SetB=", setB)
print("The union of sets A and B:", setA.union(setB))
print("The size of the union:", len(setA.union(setB)))
print("The difference of sets A and B:", setA.difference(setB))
print("The intersection of sets A and B:", setA.intersection(setB))
print("Is SetA a subset of B?", setA.issubset(setB))
setB.discard(7)
print("SetB after removing 7:", setB)
