def compare( x, y ):
    if x < y:
        print x, "is less than", y
        
    elif x > y:
        print x, "is greater than", y
        
    else:
        print x, "and", y, "are equal"

def isVowel( character ):
    if character == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
        print character, "is a vowel"
    elif character == "y" or "Y":
        print character, "is sometimes a vowel"
    else:
        print character, "is a consonant"

isVowel("i")