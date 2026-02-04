#6
try:
    n = int(input())
    print(10 / n)
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("Error")

#7
try:
    x = int("5")
except ValueError:
    print("Error")
else:
    print(x * 2)

#8
try:
    f = open("a.txt", "w")
    f.write("hi")
finally:
    f.close()

#9
try:
    print(5 + "5")
except TypeError:
    print("Error")

#10
try:
    age = -3
    if age < 0:
        raise ValueError
except ValueError:
    print("Error")
