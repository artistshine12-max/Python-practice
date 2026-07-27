#lists:
a= ["Apple","Orange",1,3.5, False,True]
a[0]="Grapes"
a[3]=5
print(a)
a[5]=False
print(a)
#Unlike strings, lists are mutable.
#Lists are slice in the same ways as Strings:
print(a[2:4])
#Important List functions:
a.append("HEllo")
print(a)
b= [2,1,3,6,7,10,9,5,4]
b.sort()
print(b)
b.reverse()
print(b)
b.insert(3, "Shin Chan")
print(b)
b.pop(3)
print(b)
print(b.pop(3))
