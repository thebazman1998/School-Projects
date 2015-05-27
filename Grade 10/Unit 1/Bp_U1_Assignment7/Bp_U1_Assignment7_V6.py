"""
Name: Basil
Class: ICS201-01
Date: 19/02/14
Assignment 7
"""

def compare(x, y):
    if x < y:
        print x, "is less than", y
        
    elif x > y:
        print x, "is greater than", y
        
    else:
        print x, "and", y, "are equal"

################################################################################

def isVowel(character):
    character = character.lower()
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        print character, "is a vowel"
    elif character == "y" or character == "Y":
        print character, "is sometimes a vowel"
    else:
        print character, "is a consonant"

################################################################################

def isDivisibleBy3(n):
    if n % 3 == 0:
        print n,"is divisible by 3"
    else:
        print n, "is not divisible by 3"

################################################################################

def weight_class(n):
    if n > 205 and n < 266:
        return n, "Is Heavyweight"
    elif n > 185 and n < 205:
        return n, "Is Light Heavyweight"
    elif n > 170 and n < 185:
        return n, "Is Middleweight"
    elif n > 155 and n < 170:
        return n, "Is Welterweight"
    elif n > 145 and n < 154:
        return n, "Is Lightweight"

################################################################################

def welcomeScreen():
    play = raw_input("Would you like to play?").lower()
    if play == "yes" or play == "yup" or play == "sure" or play == "y" or play =="ok":
        return "Welcome to 'The Game' \n Good Luck"
    else:
        return "Thank you for playing"

print welcomeScreen()

################################################################################

def isDigit(n):
    if (n > 0 or n == 0) and (n < 9 or n == 9):
        return True
    else:
        return False

################################################################################

# 4 is less than 7, therefore it prints "True"
print 4 < 7
# 4 is not greater than 7, therefore it prints "False"
print 4 > 7
# Prints "True" because both of them are = to True
print True and True
# Both are True, so prints out "True"
print 4 < 7 and 1 < 10

# Prints "False" because only one is True
print True and False
# Prints "False" because only one is True
print 4 < 7 and 1 > 10

# Prints "True" because one of them is = to True
print True or False
# Prints "True" because one of them is = to True
print 4 < 7 or 1 > 10

# Prints "True" because it is the opposite of False
print not(False)

################################################################################

def calculatePayroll(hoursWorked, hoursOver, hourlyRate):
    notOvertime = hoursWorked - hoursOver
    notOverPay = notOvertime * hourlyRate
    overPay = hoursOver * (hourlyRate * 1.5)
    totalPay = notOverPay + overPay
    
    print "Hours worked not overtime:", notOvertime, "\n Hours worked overtime:", hoursOver, "\n not overtime pay:", notOverPay, "\n Overtime pay:", overPay, "\n Total pay:", totalPay
    
################################################################################