ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sorting the list
ages.sort()

print(f"Minimum is {ages[0]}")
print(f"Maximum is {ages[-1]}")

# now finding the median age
if(len(ages) % 2 ==1 ):
    print(ages[len(ages)//2])
else:
    print(sum(ages[len(ages)//2 : len(ages)//2 + 2])/2)

# finding the average
print(sum(ages) / len(ages))

# finding the range of ages max - min
print(max(ages) - min(ages))

print("I am Ali, my life is not going well something inside doesnt make me to feel happy and good and completed.I want to get to the max and I thik I could. ")