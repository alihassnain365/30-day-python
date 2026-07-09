#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(0,11):
    print(i)
else:
    print("Job is completed boss")

count = 0
while(count<=10):
    print(count)
    count = count+1
else:
    print("Job is competed boss")

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

for i in range(0,7):
    for j in range(0,i):
        print('#',end='')
    print()

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.

l = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for language in l:
    print(language)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
l1 = ['banana', 'orange', 'mango', 'lemon']
for fruit in range(-1,-5,-1):
    print(l1[fruit])
else:
    print("job is done")