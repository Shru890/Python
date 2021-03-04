#1.to accept a tuple from user
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print(s)
a=tuple(map(str,input("Enter the values for alphabetic tuple::").split(" ")))
print(a)

#2.to make a tuple according to user specified data type
ty=input("Enter the type of tuple Ex. numeric or aplhabetic::")
if ty=="numeric":
    s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
    print(s)
else:
    a=tuple(map(str,input("Enter the values for alphabetic tuple::").split(" ")))
    print(a)

#3.to accept a numeric tuple and print any element
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print(s[0])

#4.to convert tuple to string
s=tuple(map(str,input("Enter the values for alphabetic tuple::").split(" ")))
print(s)
print(" ".join(s))

#5.to accept a tuple and display it's fourth and fourth last element
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print(s[3])
print(s[-4:-3])

#6.to check element in a tuple
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
k=int(input("Enter the element::"))
print(k in s)

#7.to remove an element for a tuple
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
i=int(input("index of the element to be removed::"))
print(s)
p=list(s)
p.remove(i)
print(tuple(p))

#8.to give the length of a tuple
s=tuple(map(str,input("Enter the values for tuple::").split(" ")))
print(len(s))
