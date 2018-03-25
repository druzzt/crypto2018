import binascii
import string

def readFile(filename):
    with open(filename) as fileobj:
        ciphertextsList = []
        for line in fileobj:  
            singleCiphertext = ""
            for ch in line: 
                singleCiphertext = singleCiphertext + ch
            if singleCiphertext.startswith('ciphertext') or singleCiphertext.startswith('\n'):
                pass
            else:
                ciphertextsList.append(singleCiphertext[:-3])
        return ciphertextsList

def turn_to_dict(*args):
    return {i: v for i, v in enumerate(args)}

def convertTo(ciphertextsList):
    listOfCiphertexts = []
    for singleStringCiphertext in ciphertextsList:
        singleASCIICharacterOfCiphertextList = singleStringCiphertext.split(' ')
        listOfASCII = []
        for asciiCharacter in singleASCIICharacterOfCiphertextList:
            listOfASCII.append(asciiCharacter)
        listOfCiphertexts.append(listOfASCII)
    return listOfCiphertexts

def toAscii(byteString):
    return int(byteString, 2)

def xor(one, two):
    return (int(one) ^ int(two))

def asciid(number):
    return str(unichr(number))

def is_ascii(text):
    if isinstance(text, unicode):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False
    return True

def number_is_ascii(number):
    return number if number >= 32 and number < 128 else False

def strxor(a, b):     # xor two int (trims the longer input)
    return ([(x ^ y) for (x, y) in zip(a, b)])

def strxorShifted(a, b, shift):     # xor two int (trims the longer input)
    newA = []
    if shift >= len(a):
        return []
    for ai, i in enumerate(a):
        if i >= shift:
            newA.append(i)
    zipped = zip(newA,b)
    # print zipped
    return ([(x ^ y) for (x,y) in zipped])
    # for (x,y) in zipped:
        # print(x, y, shift)
    # return ([(x ^ y) for (x, y) in zip(a, b)])

def arrayOfNumberToArrayOfASCII(arrayOfNumbers):
    ofAscii = []
    for i in arrayOfNumbers:
        if number_is_ascii(i):
            ofAscii.append(asciid(i))
        else:
            ofAscii.append("^")
    return ofAscii

def arrayOfAsciiToArrayOfNumber(arrayOfAscii):
    ofNumber = []
    for i in arrayOfAscii:
        ofNumber.append(ord(i))
    return ofNumber