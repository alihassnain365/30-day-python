def capitalize_list(l):
    for li in l:
        print(li.upper())

# capitalize_list(['ali','shehri','shami','sunny'])

def add_item(item,list_):
    list_.append(item)
    return list_

friends = ['ahsan','sadi','shami','sheki','mango']
friends = add_item('sunny',friends)
print(friends)