
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# Join A and B
c = A|B   # similar to c = a.union(b)
print(c)
# Find A intersection B
c.clear()
c = A.intersection(B)
print(c)
# Is A subset of B
print(f"Is A subset of B {A.issubset(B)}")
# Are A and B disjoint sets
print(f"Is A and B are disjoint : {A.isdisjoint(B)}")
# Join A with B and B with A
ab = A.union(B)
print(ab)
ba = B|A
print(ba)
# What is the symmetric difference between A and B
s_diff = A.symmetric_difference(B) # the elements that are in either one , not in both
print(s_diff)
# Delete the sets completely
del A
del B
del c
del ab
del ba
del s_diff



