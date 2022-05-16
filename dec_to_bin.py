def toBinary(decimal): # Converts "decimal" args to binary representation of input number.
    binary = []
    decDiv = decimal // 2 # Decimal divided by two using floor division. to implement and represent LSB and MSB
    remainder = str(decimal % 2)
    binary.append(remainder)
    while decDiv > 0:
        remainder = str(decDiv % 2)
        decDiv = decDiv // 2
        binary.append(remainder)
    binary.reverse()

    return ''.join(binary) # Returning string rather than list for aesthetic reasons B)
