'''
Created on May 26, 2014

@author: Basil

I decided to make the program read the seperate digits as seperate numbers in the hundreds, tens, and ones column, and i made a different dictionary for each column, so that i didnt have to remove the zeros from the Decimal Numeral equivalent of each Roman Numeral, then add each column together in a string that i would print
'''

# I started off by putting the Roman Numerals into dictionaries with the key being Decimal Numbers, and the value being the equivalent Roman Numeral (No zeros)
conversion_3_digit = {'9' : 'CM', '8' : 'CCM', '7' : 'DCC', '6' : 'DC', '5' : 'D', '4' : 'CD', '3' : 'CCD', '2' : 'CC', '1' : 'C'}
conversion_2_digit = {'9' : 'XC', '8' : 'XXC', '7' : 'LXX', '6' : 'LX', '5' : 'L', '4' : 'XL', '3' : 'XXL', '2' : 'XX', '1' : 'X'}
conversion_1_digit = {'9' : 'IX', '8' : 'IIX', '7' : 'VII', '6' : 'VI', '5' : 'V', '4' : 'IV', '3' : 'III', '2' : 'II', '1' : 'I'}

def menu(): # Asks if you want to run the program
    choice = raw_input('Would you like to run the program?\n>> ').lower()
    if 'y' in choice:
        main()

def main(): 
    done = False
    roman_numeral = [] # This will be the final list of Roman Numerals
    
    while not done:
        number = raw_input('Please enter a Positive Integer (Greater than zero) to convert to Roman Numerals. Type end to quit.\n>> ')
        if number != 'end':
            if len(number) == 3: # Runs code if it is a three digit number
                roman_numeral.append(conversion_3_digit[number[0]]) # Uses first digit to find the Roman Numeral equivalent
                roman_numeral.append(conversion_2_digit[number[1]]) # Uses second digit to fine the Roman Numeral equivalent
                roman_numeral.append(conversion_1_digit[number[2]]) # Uses third digit to fine the Roman Numeral equivalent
                roman_numeral_str = roman_numeral[0] + roman_numeral[1] + roman_numeral[2] # Adds each Roman Numeral from the list into a string 
                print roman_numeral_str # prints the Roman Numeral
                
            elif len(number) == 2: # Runs if it is a two digit number
                roman_numeral.append(conversion_2_digit[number[0]])
                roman_numeral.append(conversion_1_digit[number[1]])
                roman_numeral_str = roman_numeral[0] + roman_numeral[1]
                print roman_numeral_str
            
            elif len(number) == 1: # Runs if it is a one digit number
                roman_numeral.append(conversion_1_digit[number[0]])
                print roman_numeral[0]
            
            roman_numeral = []
        else:
            done = True

menu()