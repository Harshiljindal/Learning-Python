a = str("hello world")
b = int(20)
c = float(1.4)
d = complex(2j)
e = list(("apple", "bannana", "cherry"))
f = tuple(("apple", "bannana", "cherry"))
g = range(6)
h = dict(name="harshil", age=14)
i = set(("apple", "bannana", "cherry"))
j = frozenset(("apple", "bannana", "cherry"))
k = bool(5)
l = bytes(5)
m = bytearray(5)
n = memoryview(l)

#numbers in this 3 types come int float and complex
print(type(b))
print(type(c))
print(type(d))
#now we will change type
b = float(b)
print(type(b))

#string in this only one type str
print(type(a))
print(a)
print(a[0]) #this will print first letter of var a as in this counting start from 0
print(len(a)) #this will print of lenght of var a
print("hello" in a) #this will check that a has hello or not if yes it will print true
print("hello" not in a) #this will check that  this sould not be there
print(a[2:5]) #this will print from 3rd letter to 5th menas 2 to 5 but 5 not include lik 0=h 1=e 2=l 3=l 4=o  so this will print 2,3,4
print(a[:5]) #start til 4
print(a[2:]) #from 2 to end 
print(a.upper()) #print string in upper case
print(a.lower()) #print string in lower case
print(a.replace("H", "J"))  #replace h with j
print(a.split(",")) # returns ['Hello', ' World!']