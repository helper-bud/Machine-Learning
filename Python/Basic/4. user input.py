def printVal():
    print("20 days",str(resutl)," in min:")
    print(" all good! ")

def printValWithParameters(num_of_days, a):
    print(f"{num_of_days} {a}")


a = int(input("Enter a : "))

b = float(input("Enter b : "))

c = bool(input("Enter c : "))

d = str(input("Enter d : "))

print(c)
resutl   = a *b * c

printVal()

printValWithParameters(20,b)
