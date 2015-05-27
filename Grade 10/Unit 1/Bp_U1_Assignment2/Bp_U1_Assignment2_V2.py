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