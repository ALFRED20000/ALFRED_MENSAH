
def log (x,y):
    return log(xy)
def add     (x, y):
    return (x + y)
def subtract(x, y):
    return  (x - y)
def multiply(x, y):
    return  (x * y)
def divide  (x, y):
    if  y == 0:
        return (" Error: please input valid numerical value")
    else:
        return  (x / y)
def exponential (x,y):
    return  (x**y)


print ("1, add")
print ("1, Subtract")
print ("1, multtiply")
print ("1, divide")
print ("1, exponential")
print ("6, log") 

alfred =input("Select an operation to perform: (1/2/3/4/5) ")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input")
    exit()
if alfred in ["1", "2", "3", "4", "5",]:
    if alfred == "1":
        result= add(num1, num2)
        print("The sum is :" + str(result))
    
    if alfred == "2":
        result= subtract(num1, num2)
        print("The difference is : " + str(result))

    if alfred == "3":
        result= multiply(num1, num2)
        print("The product is : " + str(result))

    if alfred == "4":
        result= divide(num1, num2)
        print("The result is : " + str(result))

    if alfred == "5":
        result= exponential(num1, num2)
        print("The value is : " + str(result))
    if alfred == "6":
        result= log(num1, num2)
        print("The  remainder is : " + str(result))








