'''#List
a=[]
b=[1,2,3,4]
c=['apples','grapes','mangoes']
d=[1.2,3.4,4.6]
b[0]=99
print(b)
print(c[1])

for i in range(len(b)):
    print(b[i]*2)

statement="this is a sentence"
words=statement.split()
print(words)
for i in range(len(words)):
    words[i]=words[i].upper()
print(words)'''
    
'''#List methods
#insert
example=[1,2]
print(example)
example.insert(2,10)
print(example)
example.insert(3,100)
print(example)
#append
example.append('new')
print(example)

example1=[161,172,145]
print(example1)
changed_list=example+example1+['a','b','c']
print(changed_list)'''

'''#pop
a=[2,4,6,8,10]
print(a)
a.pop()
print(a)
a.pop(2)
print(a)'''

'''#searching a list
list_1=[2,3,4,5,6,7]
target=5
if target in list_1:
    print("element is there")
else:
    print("element is not there")'''

'''#sorting of list elements
list_1=[6,2,4,1,9,56,3]
print(list_1)
list_1.sort()
print(list_1)'''

#aliasing and its side effects

first=[10,20,30]
second=first
print("second list",second)
print("first list",first)
first[1]=100
print("second list",second)
print("first list",first)

third=[]
for i in first:
    third.append(i)
print("first",first)
print("third",third)
first[1]=700
print("first",first)
print("third",third)






