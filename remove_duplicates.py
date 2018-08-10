# eliminate duplicate keys

a = ["1", 1, "1", 2]

print (list(set(a)))


# using ordered dict

from collections import OrderedDict

print (list(OrderedDict.fromkeys(a)))