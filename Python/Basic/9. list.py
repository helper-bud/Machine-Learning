mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[-1]) # last item
print(thislist[2:5]) # 3,4,5th item
print(thislist[:4]) # 0,1,2,3
print(thislist[-4:-1]) #This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

# changing
thislist[1] = "blackcurrant" # change the 1 item to blacurrant
thislist[1:3] = ["blackcurrant", "watermelon"] # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist.insert(2, "watermelon")
thislist.clear() # clear list item

#adding
thislist.append("orange")
thislist.insert(1, "orange") # insert an item in the second positon

# remove
thislist.remove("banana")
thislist.pop(1) # remove the second item
thislist.pop() # remove the last item
del thislist[0] # remove the 1st item of the list.
del thislist # it will delete the list

# loop in the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# sorting
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(reverse = True)


# copy the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# adding two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#another way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
#another way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


# checking
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
