'''
Name: Basil
Class: ICS201-01
Date: 04/02/14
Assignment 2
'''

x = input("Enter a number")
print type(x)

x = raw_input("Enter a number")
print type(x)

x = raw_input("Enter a number")
print type(x)
x = float(x)
print type(x)

x = raw_input("Enter a sentence")
print x

x = input("Enter a number")
print x

####################

#Program 1
x=2
y=x+x
print y

#Program 2
s="2"
t=s+s
print t

#Program 1 treats the variable x as a number, Program 2 treats s as a character

####################

ConversionFactor = 2.54

inches = input("Please enter the number of inches to convert to centimetres")

centimetres = inches * ConversionFactor
centimetres = round(centimetres, 1)

print inches, "inches =", centimetres, "cm."

####################

ConversionFactor = 2.54

centimetres = input("Please enter the number of centimetres to convert to inches")

inches = centimetres / ConversionFactor
inches = round(inches, 1)

print centimetres, "cm. =", inches, " inches"

#No error ^^^

###################

DateOfBirth = input("Please enter year of birth")

Age = 2014 - DateOfBirth

print Age

###################

FirstName = raw_input("First Name")
LastName = raw_input ("Last Name")

print LastName,",", FirstName

###################

x=input("Enter a Number")
y=input("Enter a Second Number")
print "The sum is", x+y
print "The difference is", x-y
print "The average is", x+y/2
print "The maximum is", max (x, y)
print "The distance is", abs (x-y)
print "The square is", x+y**2
print "The cube is", x+y**3
print "The fourth power is", x+y**4

###################