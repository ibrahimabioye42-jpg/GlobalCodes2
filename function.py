# def hello():
#     print("Hello")

# def Goodbye():
#     print("Goodbye")
    
# def nameSchool():
#     print("My school name is HTU")

# hello()
# Goodbye()
# nameSchool()

# def add(a,b):
#     return a + b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = add(a,b)
# print(f"the sum of {a} and {b} is {result}")

def light(color):
    if color == "green":
        print("Go")
    elif color == "yellow":
        print("Caution")
    elif color == "red":
        print("Stop")
color = input("Enter the traffic light color: ")

light(color)