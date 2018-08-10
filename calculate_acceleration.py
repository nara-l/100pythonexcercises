def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a


#print(acceleration(0, 10, 0, 20))

# why an error in this code?

def foo(a, b):
    return a + b


x = foo(2, 3) * 10

print(x)
