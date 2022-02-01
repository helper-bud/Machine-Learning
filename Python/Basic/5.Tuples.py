# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Allow duplicates
# you cant make tuple with one item

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))


#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# access tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1]) # last item
print(thistuple[2:5]) # including 2 to 4
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


# tuples are immteable, so we have to convert it in to the list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange") # adding
thistuple = tuple(y)
print(thistuple)

#removing
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#iterating
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


# joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
