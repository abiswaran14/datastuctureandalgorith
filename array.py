import array as ar
a=ar.array(("i"),[1,2,3,4,5,6])
print(a)

print("--------------------------")

#searching
print("searching in array")
print("searching in array",a[4])

print("--------------------------")

#inserting
#for insering use inser(location,value)
print("inserting in array")
a.insert(0,0)
#where first zero is location and second zero is value
print(a)

print("--------------------------")

#deleting
#for deleting use pop(location)
#if nothing is gived the last value will be deleted
print("deleting in array")
a.pop(4)
print(a)
