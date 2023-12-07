'''data="hi there!"
for index in range(len(data)):
    print(index,data[index])'''

'''#string slicing
#substring

name="myfile.txt"
print(name[0:])
print(name[0:2])
print(name[:len(name)])
print(name[-3:])
print(name[2:6])'''

'''#string of bits to decimal integer
#0101010- decimal

bits=input("enter bits")
decimal=0
exp=len(bits)-1
for i in bits:
    decimal=decimal+int(i)*2**exp
    exp=exp-1
print("decimal value",decimal)'''


'''#string methods
statement=input("enter a statement")
list_of_words=statement.split()
print("there are",len(list_of_words),"words")
size=0
for word in list_of_words:
    size+=len(word)
print("the average word length is",size/len(list_of_words))'''

















    
