'''
Created on 2013-2-21

@author: huysh1976
'''
def sayHello(msg, times=1):
    print(msg*times)

def forFunc(items):
    for item in items:
        print(item)
items = ['s1', 's4','s2']
#sayHello(msg='mm', times=5)
items.append("s3")
items.sort(key=None, reverse=False)
print(items)
items.__delitem__(0)
items.__delitem__(0)
print(items)
