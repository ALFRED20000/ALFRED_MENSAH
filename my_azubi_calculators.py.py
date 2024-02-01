#my nested dictionary
my_cars= { 
    "car1":{
        "name":"Benz",
        "year":"2007"},
    "car2":{
        "name":"toyota",
        "year":"2006"}

}

my_dictionary= {
"Alfred Mensah":" alfredmensah2000@gmail.com",
"John Mensah":" johnmensah2012@yahoo.com",
"patrick":"pato@gmail.com"
}

print(my_dictionary)







 # Developing python simple calculator
def add(x, y): 
    return (x + y)
def subtract(x, y):
    return (x - y)
def multiply(x, y):
    return x * y
def divide (x, y):
    if  y == 0:
        return "Error: Division by Zero is error "
    else:
        return x / y

print ("simple calculator")
print ("1. add")
print ("2. subtract")
print ("3. multiply")
print ("4. divide")

choice = input("select an operation to perform (1/2/3/4) ")
try:
    num1 = float(input(" Enter the first number "))
    num2 = float(input("Enter the second number "))
    
except ValueError:
    print("invalid input: please input valid numeric value")
    exit()

if choice in ["1", "2", "3", "4"]:
    if choice == "1":
        result = add(num1, num2)
        print("Result: " + str(result))

    elif choice =="2":
        result = subtract(num1,num2)
        print ("result: " + str(result))
        result = subtract(num1, num2)
        print("Result: " + str(result))
    elif choice == "3":
        result = multiply(num1, num2)
        print("Result: " + str(result))
    elif choice == "4":
        result = divide(num1, num2)
        print("Result: " + str(result))

else:
    print("Invalid choice. Please select a valid operation (1/2/3/4).")


