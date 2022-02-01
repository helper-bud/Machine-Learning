thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Access items
x = thisdict["model"]

#Get the value of the "model" key:
x = thisdict.get("model")

# get all keys
x = thisdict.keys()

# Changing items in two ways.
thisdict["year"] = 2018
thisdict.update({"year": 2020})

# add items
thisdict["color"] = "red"
print(thisdict)

# remove items
thisdict.pop("color")
print(thisdict)

# looping items

print(" >>__get all the values")
for x in thisdict:
  print(x)


print(" >> __get all the keys")
for x in thisdict.keys():
  print(x)


print(" >> __get all the values and keys")
for x, y in thisdict.items():
  print(x, y)
  
# copying a dictionary
mydict = thisdict.copy()
print(mydict)
