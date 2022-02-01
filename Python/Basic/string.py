x= "hi "
y = "hello, how are you"
z = x+y  #concat

print(z)

# accessing value of string
print(y[0])

# length
print(len(y)-1)

print(y.lower())
print(y.upper())

print(y.title()) #it will make all the first letter of string upper case

print(y.strip()) # remove the space beginig and end

print(y.find("h")) # to find index

print(y.replace("h","j")) # replace all of them

print('hello' in y) # check if the string exist in the string

# !! string slicing
m = "my name is azmain"
#m[a:b] -> return from index a up until index b(b not included)
print (m[0:5])
print (m[:5]) # it will automatically take 0 as the begining
print(m[-1]) # it will print the value of last element
