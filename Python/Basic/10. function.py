def printVal():
    print("20 days",str(resutl)," in min:")
    print(" all good! ")

def printValWithParameters(num_of_days, a):
    print(f"{num_of_days} {a}")


a = 20
b = 24
c = 60

resutl   = a *b * c

printVal()

printValWithParameters(20,b)
