# Set items are unchangeable, but you can remove items and add new items.
# Set items are unordered, unchangeable, and do not allow duplicate values. Cant use refrred index
# Duplicate values will be ignored

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# output : {'apple', 'banana', 'cherry'} > duplicate item ignored.

print(len(thisset))

set1 = {"abc", 34, True, 40, "male"} #> A set can contain different data types


GEEK = {'g', 'e', 'k'}
# adding 's'
GEEK.add('s')
print('Letters are:', GEEK) #> Letters are: {'k', 'g', 'e', 's'}


GEEK = {'g', 'e', 'k'}
# removing 'k'
GEEK.remove('k')
print('Letters are:', GEEK) #> Letters are: {'g', 'e'}
