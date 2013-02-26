'''
Created on 2013-2-21

@author: huysh1976
'''

persons = ['p1','p4']
persons.insert(2, 'p2')
persons.sort(cmp=None, key=None, reverse=False)
print persons

map = {'u1':'u1@ns.com',
       'u2':'u2@ns.com',
       'u4':'u4@gmail.com'
       }
print map
map['u3']='u3@ns.com'
del map['u2']
print map
if 'u4' in map:
    print 'mail of %s is %s' % ('u4',map['u4'])
for key,value in map.items():
    print 'key:%s    value:%s' % (key, value)
    
print '1 to 2 of persons', persons[0:2]       
print '2 to 4 of characters', 'pythonstudy'[1:4] 

s1 = 'test string'
if s1.startswith('test'):
    print 'start with test..'
if 'r' in s1:
    print 'contain r'
if s1.find('string') != -1:
    print 'contain string'
