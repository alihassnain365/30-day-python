import math
def two_number_sun(n1,n2):
    return n1 + n2
print(f"Sum of two number is : {two_number_sun(57,23)}")


def are_of_circle(radius):
    return 3.142 * radius * radius

print(f"Radius of the circle is {are_of_circle(34)}")


def arbitrary_number(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

print(f"Sum of the arbitray number is {arbitrary_number(1,2,3,4,5,6,7,8,9)}")

def solve_quad_eq(a,b,c):
    if a== 0:
        print("Not a quadratic equation")
    discriminent = b**2 - 4 * a * c
    if discriminent > 0:
        x1 = (-b + math.sqrt(discriminent)) / 2 * a
        x2 = (b - math.sqrt(discriminent)) / 2 * a
        return {x1,x2}

print(solve_quad_eq(1,-1,3))


def print_list(list_):
    print(list_)

def print_reverse_list(list_):
    for brother in range(-1,-1*len(list_)-1, -1):
        print(list_[brother])

def main():
    brother = ['ali','shehri', 'sunny', 'shami']
    print_list(brother)
    print_reverse_list(brother)

main()