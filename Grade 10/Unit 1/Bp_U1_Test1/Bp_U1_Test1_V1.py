"""
Basil
Bp_U1_Test
28/02/14
"""

# Methods

def investingCalc(startAmount, years, rate):
    startAmount = startAmount * 1.0
    totalAmount = startAmount * (1 + rate) ** years
    totalAmount = round(totalAmount, 2)
    return totalAmount

def pizzaCalc(people):
    numPiecesLeft = 32 % people
    numPiecesLeft = str(numPiecesLeft)
    numPieces = float(32) / people
    numPiecesRnded = int(numPieces)    
    numPieces = str(numPieces)
    numPiecesRnded = str(numPiecesRnded)
    
    option1 = "option 1: " + numPiecesRnded + " slices each, " + numPiecesLeft + " left over\n"
    option2 = "option 2: " + numPieces + " slices each"
    
    return option1 + option2

def pythonCageCalc(length):
    length = length * 1.0
    while length < 6 or length == 6:
        cageDim = length / 2
        return cageDim
    while length > 6:
        startDim = 6 / 2
        left = length - 6
        endDim = (left * 3)/4
        cageDim = startDim + endDim
        return cageDim

# Main

print investingCalc(1000, 5, .05)
print pizzaCalc(10)
print pythonCageCalc(9)