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
