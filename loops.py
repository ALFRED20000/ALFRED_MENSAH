#Question 1
# if applicant has high income and good credit, Eligible for loan

has_high_income= True
has_good_credit = True
if has_good_credit and has_high_income:
    print("eligible for loan")

#question 2
'''
  if temperature is greter than 30, its a hot day.
  otherwise 
  if its less than 10
  its a cold day.
  otherwise, 
  its neither hot nor cold'''

temperature = float(input( "what your temperature? "))
if temperature >30: 
     print("its a hot day")
elif temperature <10:
    print("its a cold day")
else:
    print(" its neither hot or cold")

'''
question 3
if name is less than 3 characters long
name must be at least three characters
otherwise if its more than 50 characters long
name must be a maximum of 50 charaters
otherwise name looks good'''

#solution

name = str(input(" please enter your full name: "))
if len(name) < 3: 
    print(" name must be at least three characters")
elif len(name) > 50:
    print (" name must be at most 50 characters")
else:
    print(" name looks good")


#weight calculator

weight = int(input(" input your weight:  "))
unit = input("(L)bs or (K)g? ")
if unit.upper()=="L":
    converted=weight * 0.45
    print(f"you are {converted} kilos")
elif unit.uppper()=="K":
    como=weight // 0.45
    print(f" you are {como} pounds")
else:
    print(" invalid input")
    


#while loops
i = 1 
while i <= 9:
    print ("*" * i)
    i +=1



#guessing game with while loop

secret_number = 9
guesses = 0
count_limit =3
while guesses < count_limit:
    guess= int(input("Guess:  "))
    guesses += 1
    if guess == secret_number:
        print("you won!! ")
        break
else:
    print("sorry you failed")



#car game 
command = ""
started =False

while command != "quit":
    command = input("> ").lower()
    if command =="start":
        if started:
            print("car has already started!") 
        else:
            print(" car started")
        print(" car started...")   
    elif command == "stop":
        if not started: 
            print("car already stopped")
        else:
            started = False
        print(" car stopped")
    
    elif command == "help":
        print("""
        start- To start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print(" sorry i do not understand")



#sales and discount

amount = float (input("Please Enter the amount you purchased: "))
state_tax = amount * 0.05
print("state_tax is %.2f " % state_tax)
county_tax = amount * 0.025
print("county_tax is %.2f " %county_tax)
total_tax = state_tax + county_tax
print("total_tax is % .2f" %total_tax)
total_sale = total_tax + amount
print("total_sale is %.2f"% total_sale)



'''
Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

The owner wants you to do some calculations on the data with these criteria's:

    -calculate the total price average for all products

    -create a new price list that reduces the old prices by $ 5

    -calculate the total revenue generated from the products

    -calculate the average daily revenue generated from the products

    -based on the new prices, which products are less than $ 30 

Below is the data you are to use for the problem :

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]'''



























