fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

val= 10
for x in range(val): # will print:  0 to 9
    print(x)

for x in range(2, 6): # will print:  2 to 5
    print(x)

for x in range(2, 30, 3): # 2 5 8 11 14 17 20 23 26 29. > 3 step diffrence
  print(x)

#only else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
#output:
'''
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
'''

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass


#break statement
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")



for x in range(2, 30, 3):
    print(x)
