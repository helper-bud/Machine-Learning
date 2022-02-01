'''while True:
    try:
        a = int(input("Enter a : "))

    except ValueError:
        print("wrong value")

    print("value", a)'''


i = 1
print(">>___from 1 to 5")
while i < 6:
  print(i,end=' ')  
  i += 1

print()
print(">>___from 1 to 5 except 3")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i,end=' ')
