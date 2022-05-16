def toBinary(decimal):
    binary = []
    decDiv = decimal // 2
    remainder = str(decimal % 2)
    binary.append(remainder)
    while decDiv > 0:
        remainder = str(decDiv % 2)
        decDiv = decDiv // 2
        binary.append(remainder)
    binary.reverse()

    return ''.join(binary)