c = dict(c=3)
d = dict(a=1, b=2)
sumd = {**d, **c}

print (sumd)

# SUM OF DICT VALUES

print ("sum dictionary values")
print ( sum(sumd.values()))

# Filter dictionary by value

sumd = {key: value for key, value in sumd.items() if value <2} # dictionary comprehension

print (sumd)