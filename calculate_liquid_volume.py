import math
def calc_liquid_volum(h, r=10):
    pi = math.pi
    return ( 4 * pi * r ** 3 ) / 3 - ( pi * h ** 2 * ( 3 * r - h ) ) / 3


l_v = calc_liquid_volum(2)
print(l_v)

# learned first use of math function
# uses pi, and alternative to pow which is in math module. dir(math) help(math.pow)