import collections
import pprint
file_input=input("mooc.txt")
with open(file_input,'r') as info:
    count=collections.Counter(info.read().upper())
    value=pprint.pformat(count)
print(value)
