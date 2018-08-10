from pprint import pprint

a = list(range(1,11))
b = list(range(11,21))
c = list(range(21,31))

#dic = {'a': a, 'b': b, 'c': c}
dic = dict(a=a, b=b, c=c)

pprint(dic)

# multi level indexing



print(dic['b'][2])  # third value of b

# Iterate dictionary

# 1 using for?
for key, value in dic.items():
    print( key, ' has value', value)



# 2 using list comprehension

ite = {key: value for key, value in dic.items()}

pprint(ite)