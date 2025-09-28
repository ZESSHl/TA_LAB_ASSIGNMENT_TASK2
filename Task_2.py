import math

def circle_calc():
    Choice = input("Area or Circumference: ")
    R = float(input("Insert Value: "))
    if Choice == "Area":
        result = math.pi * (R ** 2) 
    else:
        result = (2 * math.pi * R)
    return result
print(round (circle_calc(), 4))
