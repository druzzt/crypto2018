from loaders import readFile
from loaders import convertTo
from loaders import toAscii
from loaders import xor
from loaders import asciid
from loaders import is_ascii
from loaders import number_is_ascii
from loaders import strxor
from loaders import strxorShifted
from loaders import arrayOfNumberToArrayOfASCII
from loaders import arrayOfAsciiToArrayOfNumber
from loaders import readConcordance
from loaders import probableSentence
import pdb

import string
import collections
import sets

ciphertextsList = readFile("ciphertexts/all.txt")
dictlist = readConcordance("concordance/raj.txt", 1000)
listsOfBytes = convertTo(ciphertextsList)
superarr = []
for byteList in listsOfBytes:
    arr = []
    for byte in byteList:
        elem = toAscii(byte)
        arr.append(elem)
    superarr.append(arr)


dicted = dict.fromkeys(string.ascii_letters, 0)
special = dict.fromkeys(".-,'!? ", 0)
dicted.update(special)

size_of_seeked_cipher = len(superarr[len(superarr)-1])

d = []
for index1, ciphertext1 in enumerate(superarr):
    xored = strxor(ciphertext1, superarr[len(superarr)-1])
    d.append(xored)


X = "A"
minProb = 0.5
while X != "":
# for X in dictlist[::-1]:
    for it, probString in enumerate(d):
        if len(X) < size_of_seeked_cipher:
            singleHit = []
            for i, x in enumerate(X):
                singleHit.append(probString[i] ^ ord(x))
            sent = ''.join(arrayOfNumberToArrayOfASCII(singleHit)).lower()
            # if probableSentence(sent, minProb, [x.lower() for x in dictlist]):
            print(sent, it, X, len(probString), len(sent)*8)
    X = raw_input(">")
    print("-----------------------", X)
            






















# dicted.update({"Romeo": 0})
# dicted.update({"Juliet": 0})
# # dicted.update({"Oh!": 0})
# # print dicted

# dictlist = []
# for key, value in dicted.iteritems():
#     temp = [key,value]
#     dictlist.append(temp)
# print dictlist

# known_key_positions = set()
# final_key = [None]*size_of_seeked_cipher
# target_cipher = superarr[len(superarr)-1]
# print target_cipher

# d = []
# for index1, ciphertext1 in enumerate(superarr):
#     counter = collections.Counter()
#     for index2, ciphertext2 in enumerate(superarr):
#         if index1 != index2:
#             d.append(strxor(ciphertext1, ciphertext2))


# counter = collections.Counter()
# forEachDProbableSpace = []
# for index1, ciphertext1 in enumerate(superarr):
#     if index1 < len(superarr)-1:
#         xored = strxor(ciphertext1, superarr[index1-1])
#         probableSpace = []
#         for i, letter in enumerate(arrayOfNumberToArrayOfASCII(xored)):
#             # if letter.isalpha() and letter in string.printable:
#             if letter in dicted and letter in string.printable:
#                 if xored not in d:
#                     d.append(xored)
#                     counter[i] += 1
#                 probableSpace.append({i: letter})
#         print (index1, probableSpace, len(ciphertext1), len(probableSpace))
#         forEachDProbableSpace.append(probableSpace)

# print("--------- THE END --------")






















#         cribDetected = []
#         previouslyHit = []
#         for crib in dictlist:
#             for ishift, shift in enumerate(xored):
#                 for ilet, letter in enumerate(xored):
#                     hit = []
#                     for icriblet, cribLetter in enumerate(crib):
#                         if icriblet >= ilet:
#                             oneDet = xor(ord(cribLetter), xored[ishift])
#                             cribDetected.append(oneDet)
#                             # for aLetterInsideOneDet in oneDet:
#                             if oneDet > 32 and oneDet < 127:
#                                 # print(oneDet)
#                                 hit.append(oneDet)
#                             else:
#                                 break
#                     if hit in previouslyHit:
#                         break
#                     else:
#                         previouslyHit.append(hit)
#                         # if len(hit) > 4:
#                         #     print ''.join(arrayOfNumberToArrayOfASCII(hit))
#         for index, hit in enumerate(previouslyHit):
#             if len(hit)> 6:
#                 print ''.join(arrayOfNumberToArrayOfASCII(hit))
#         print "$$$$$$$$$$$"
                            
#         # print ''.join(arrayOfNumberToArrayOfASCII(cribDetected))

                        


# knownSpaceIndexes = []
# for ind, val in counter.items():
#     if val >= 7: knownSpaceIndexes.append(ind)
# # print (knownSpaceIndexes, "<- space's indices") # Shows all the positions where we now know the key!
# # print ("---------")


# oksized = []
# for ds in d:
#     if len(ds) >= size_of_seeked_cipher:
#         oksized.append(ds)
# # print len(oksized)
# # print oksized

# # print "++++++++++++++++"

# for ciph in superarr:

#     xor_with_spaces = strxor(ciph, [32]*size_of_seeked_cipher)
#     for index in knownSpaceIndexes:
#         if len(xor_with_spaces) < index: pass
#         else:
#             # print(index, len(xor_with_spaces))
#             final_key[index] = xor_with_spaces[index]
#             known_key_positions.add(index)

# # print "----------+++++++++++++---------------"

# # final_key_bin = [val if val is not None else 0 for val in final_key]
# # # print final_key_bin

# # output = strxor(target_cipher, final_key_bin)
# # print ''.join(arrayOfNumberToArrayOfASCII(output))












# now brute xor against non space indiced cipher letters
# for dCipher in oksized:
#     out = []
#     for iterator, possibleLetter in enumerate(dCipher):
#         if iterator in knownSpaceIndexes:
#             out.append(32)
#         else:
#             xored = xor(possibleLetter, ord('I'))
#             if xored > 32 and xored < 127:
#                 out.append(xored)
#     print(''.join(arrayOfNumberToArrayOfASCII(out)))
#     print "_________"
    




























# for allDs in d:
#     whereSpace = []
#     for i, letter in enumerate(allDs):
#         attemptToXorSpace = xor(letter, 32)
#         if attemptToXorSpace >= 32 and attemptToXorSpace < 127:
#             whereSpace.append(i)

#     print arrayOfNumberToArrayOfASCII(newText)
    

# now i have 18 xored d = (m1 xor m2) = (c1 xor c2)
# now try to guess positions of ' ' in m1 which is plaintext of cipher20 (the seeked one)

# outputArr = []
# for shift in range(0, size_of_seeked_cipher-1):
# for dis in d:
#     something = strxorShifted(dis, arrayOfAsciiToArrayOfNumber(["T","h","e", " "]), 0)
#     if len(something) > 0:
#         print arrayOfNumberToArrayOfASCII(something)
# print " + + + + + + + + + + + + + "
#     outputArr.append(strxor(dis, arrayOfAsciiToArrayOfNumber(["T","h","e", " "])))

# numOutputArr = []
# for i in outputArr:
#     val = arrayOfNumberToArrayOfASCII(i)
#     numOutputArr.append(val)
#     print val
# print numOutputArr










    #         for indexOfChar, xoredValueCharNumber in enumerate(strxor(ciphertext1, ciphertext2)):
    #             if number_is_ascii(xoredValueCharNumber):
    #                 char = asciid(xoredValueCharNumber)
    #                 if is_ascii(char):
    #                     if char in string.printable and char.isalpha():
    #                         counter[indexOfChar] += 1 # Increment the counter at this index
    # knownSpaceIndexes = []
    
    # # for ind, val in counter.items():
    # #     if val >= 7: 
    # #         knownSpaceIndexes.append(ind)


    # # l = [ord(' ')]*size_of_seeked_cipher
    # # xor_with_spaces = strxor(ciphertext1,l)
    # # print xor_with_spaces


    












    

# for index, array in enumerate(d):
#     toPrint = []
#     for i, letter  in enumerate(array):
#         toPrint.append(asciid( xor(array[i], asciiNumber))
#     print (index,toPrint)




    









# zippedArr = zip(
#                 superarr[0],
#                 superarr[1],
#                 superarr[2],
#                 superarr[3],
#                 superarr[4],
#                 superarr[5],
#                 superarr[6]
#                 )


# d0Col0 = xor(zippedArr[0][0], zippedArr[1][0])
# d1Col0 = xor(zippedArr[1][0], zippedArr[2][0])
# d2Col0 = xor(zippedArr[2][0], zippedArr[3][0])
# d3Col0 = xor(zippedArr[3][0], zippedArr[4][0])

# d0Col1 = xor(zippedArr[0][1], zippedArr[1][1])
# d1Col1 = xor(zippedArr[1][1], zippedArr[2][1])
# d2Col1 = xor(zippedArr[2][1], zippedArr[3][1])
# d3Col1 = xor(zippedArr[3][1], zippedArr[4][1])

# d0Col2 = xor(zippedArr[0][2], zippedArr[1][2])
# d1Col2 = xor(zippedArr[1][2], zippedArr[2][2])
# d2Col2 = xor(zippedArr[2][2], zippedArr[3][2])
# d3Col2 = xor(zippedArr[3][2], zippedArr[4][2])

# d0Col3 = xor(zippedArr[0][3], zippedArr[1][3])
# d1Col3 = xor(zippedArr[1][3], zippedArr[2][3])
# d2Col3 = xor(zippedArr[2][3], zippedArr[3][3])
# d3Col3 = xor(zippedArr[3][3], zippedArr[4][3])

# d0Col4 = xor(zippedArr[0][4], zippedArr[1][4])
# d1Col4 = xor(zippedArr[1][4], zippedArr[2][4])
# d2Col4 = xor(zippedArr[2][4], zippedArr[3][4])
# d3Col4 = xor(zippedArr[3][4], zippedArr[4][4])

# d0 = [d0Col0, d0Col1, d0Col2, d0Col3, d0Col4]
# d1 = [d1Col0, d1Col1, d1Col2, d1Col3, d1Col4]
# d2 = [d2Col0, d2Col1, d2Col2, d2Col3, d2Col4]
# d3 = [d3Col0, d3Col1, d3Col2, d3Col3, d3Col4]

# d = [d0, d1, d2, d3]

# # print(asciid(0), asciid(127))
# for numberInASCIIRange in range(48, 127):
#     # for shift in range(0, 5):
#     hitArray = []
#     # for dIteration in range(0, 4):
#         # print("----", d[dIteration])
#     shiftedPossibleLetter = number_is_ascii(
#                                             xor(
#                                                 d[3][4], 
#                                                 numberInASCIIRange
#                                             )
#                                         )
#     if shiftedPossibleLetter: 
#         hitArray.append(asciid(shiftedPossibleLetter))
#     else:
#         hitArray.append("#")
#     # print hitArray
#                 # print asciid(shiftedPossibleLetter)
            


#     # d0l1 = number_is_ascii(xor(d0Col0, ord('T')))
#     # d0l2 = number_is_ascii(xor(d0Col1, ord('h')))
#     # d0l3 = number_is_ascii(xor(d0Col2, ord('e')))
#     # d0l4 = number_is_ascii(xor(d0Col3, ord(' ')))

#     # d1l1 = number_is_ascii(xor(d1Col0, ord('T')))
#     # d1l2 = number_is_ascii(xor(d1Col1, ord('h')))
#     # d1l3 = number_is_ascii(xor(d1Col2, ord('e')))
#     # d1l4 = number_is_ascii(xor(d1Col3, ord(' ')))

#     # d2l1 = number_is_ascii(xor(d2Col0, ord('T')))
#     # d2l2 = number_is_ascii(xor(d2Col1, ord('h')))
#     # d2l3 = number_is_ascii(xor(d2Col2, ord('e')))
#     # d2l4 = number_is_ascii(xor(d2Col3, ord(' ')))

#     # d3l1 = number_is_ascii(xor(d3Col0, ord('T')))
#     # d3l2 = number_is_ascii(xor(d3Col1, ord('h')))
#     # d3l3 = number_is_ascii(xor(d3Col2, ord('e')))
#     # d3l4 = number_is_ascii(xor(d3Col3, ord(' ')))

#     # print(d0l1, d0l2, d0l3, d0l4)
#     # print(d1l1, d1l2, d1l3, d1l4)
#     # print(d2l1, d2l2, d2l3, d2l4)
#     # print(d3l1, d3l2, d3l3, d3l4)
