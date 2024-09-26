'''
Name: Zachary Briggs
Date: 9/24/24
Description: More on f-strings, unput, and numbers/ ops
'''
print('My first commit!')

my_int= 5
my_float= 7.44
print(f"{my_int} {my_float}") #space matters otherwise its 57.44 rather than 5 7.44

another_float= 8.0 #make a float by adding .0 at the end.
float_two= float(8) #make a float by casting
print(f"{another_float} {float_two}")

#get decimal from a user
radius= float(input("Enter a radius: ")) #float is needed for decimals otherwise code will break
print(f"You entered a radius of {radius}")

#operations on numbers
#P E MMD AS (extra m is for mod)
#modulus operator or remainder operator
print(15 % 7) #prints remainder when 15 is divided by 7 (2 remainder 1)
print((2+3)*4) #2+3 first, times 4

#exponent is not ^, instead its **
print(5**4) #this is 5^4 (5 to the 4th)
print(5^4) #came out as 1

#weird math stuff
print(0.3-0.2) #it equals .09999999999999999998 (called roundoff error

#roudning
#method 1, use round()
num=2.896
print(round(num,2))
#method 2, use f string
print(f"{num:.2f}")

#Ask a user for some amount of US dollars
#Store this is in a variable
#Convert that money to some currency of choice
#Store final amount in a variable
#Print it like "__ USD is the same as __ --". Round to two decimal places.

U_S_D = float(input("Enter an amount of dollars (USD)(Make sure to use two decimal places)"))
Exchange= U_S_D*525.08
Rounded_Exchange= (f"{Exchange:.2f}")
print(f"{U_S_D} USD is the same as {Rounded_Exchange} in the Colon (Costa Rican currency)")

#String methods
name= "Zachary Briggs"
name2= "Thomas the Tank Engine"
print(name.upper())
print(name.title())
print(name2.lower()) #Lower case
