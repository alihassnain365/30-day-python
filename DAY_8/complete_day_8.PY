# Create an empty dictionary called dog
dic1 = dict()
dic2 = {}  # this syntax is similar to set() - but we can only create empty set by a = set() not set = {}

# Add name, color, breed, legs, age to the dog dictionary
dic1['name'] = 'shanky'
dic1['color'] = 'black'
dic1['legs'] = 'blue'
dic1['age'] = 12
print(dic1)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, 
# skills, country, city and address as keys for the dictionary

student = {'first_name' : 'Ali',
           'last_name' : 'Hassnain',
           'gender' : 'Male',
           'age' : 12,
           'isMarried' : False,
           'skills' : ['c++', 'python', 'mysql', 'git'],
           'country' : 'Pakistan',
           'city': 'Lahore',
           'address' : 'khanqah dogran'
           }

print(student)

# Get the length of the student dictionary
print(len(student)) # this would count the number of key values in the main dic ignores the inner dics

# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

# Modify the skills values by adding one or two skills
student.get('skills').extend(['assembly','java'])
print(student.get('skills'))

# Get the dictionary keys as a list
print(student.keys()) # it would return a list consist of keys
# Get the dictionary values as a list
print(student.values()) # it would return a list of values
# Change the dictionary to a list of tuples using items() method
print(student.items()) # .items() return the list of tuples with key and value pairs
# student = student.items()
print(student)

# Delete one of the items in the dictionary
print(student.popitem()) # it romoves the last item in the dictionary
print(student.pop('skills'))
del student['first_name']
# Delete one of the dictionaries
del student

