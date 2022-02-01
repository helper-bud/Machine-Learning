a = int(input("Enter a : "))

if a > 0:
    print("positive")
elif (a==0):
    print("zero cant be accepted ")
else:
    print("negative")

num = int(input("enter a number"))
check = True

if (num>0):
    check = False
else:
    check =  True

print("check on time", num>0)
print(check)
