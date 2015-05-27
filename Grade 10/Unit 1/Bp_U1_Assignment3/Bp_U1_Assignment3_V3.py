'''
Name: Basil Pocklington
Class: ICS201-01
Date: 04/02/14
Assignment 3
'''

####################

#Ontario Sales Receipt 

taxRate = 0.13
itemPrice = input("Price of Item")
totalTax = itemPrice*taxRate
totalPrice = totalTax+itemPrice

print "The sale price is", itemPrice
print "The tax is", totalTax
print "The total price is", totalPrice

####################

#Manitoba Sales Receipt

RSTRate = 0.07
GSTRate = 0.05
itemprice = input("Price of Item")
RST = itemprice*RSTRate
GST = itemprice*GSTRate
totalprice = itemprice+RST+GST

print "The sale price is", itemprice
print "The RST is", RST
print "The GST is", GST
print "The total price is", totalprice

#####################

#Temperature Conversion
tempCelcius = input("Enter temperature to convert to Fahrenheit")
tempFahrenheit = 9.0/5 * tempCelcius + 32

print "The temperature in Fahrenheit is", tempFahrenheit

#####################

#Cup to Liter Conversion

cups = input("Enter the number of cups to convert to liters")
liters = cups * 0.2273045
print "The amount of cups in liters is", liters
