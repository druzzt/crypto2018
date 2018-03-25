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

# ---------- finding spaces

list_of_list = list()
max_line_length = 0
for line_of_cipher in superarr:
    if (len(line_of_cipher) > max_line_length):
        max_line_length = len(line_of_cipher)
    line_aux = list()
    for c in line_of_cipher:
        line_aux.append(c)
    list_of_list.append(line_aux)

zero_to_max_line_length = range(0, max_line_length)

list_of_columns = list()
for step in zero_to_max_line_length:
    list_of_columns.insert(step, list())

for line in list_of_list:
    for index, item in enumerate(line, 0):
        aux_for_columns = list_of_columns.pop(index)
        aux_for_columns.append(item)
        list_of_columns.insert(index, aux_for_columns)

spaces = list()
pad = list()

for column in list_of_columns:
    mydict = {}
    for i in column:
        for j in column:
            result = i ^ j
            if (result >= 65):
                if i not in mydict:
                    mydict[i] = 1
                else:
                    mydict[i] = mydict.get(i) + 1
                if j not in mydict:
                    mydict[j] = 1
                else:
                    mydict[j] = mydict.get(j) + 1
                maximum = max(mydict, key=mydict.get)
    spaces.append(maximum)

for space in spaces:
    pad.append(space ^ 32)

cleartexts = []
for index_row, row in enumerate(superarr, 0):
    columns = []
    for index_column, column in enumerate(row, 0):
        columns.append(superarr[index_row][index_column] ^ pad[index_column])
    cleartexts.append(columns)

for clear in cleartexts:
    print ''.join(arrayOfNumberToArrayOfASCII(clear))






# ---------- sanity check against PAD
size_of_seeked_cipher = len(superarr[len(superarr)-1])

d = []
for index1, ciphertext1 in enumerate(superarr):
    xored = strxor(ciphertext1, superarr[len(superarr)-1])
    d.append(xored)


X = "A"
minProb = 0.5
count = 0
# for X in dictlist[::-1]:
while X != "":
    X = raw_input(">")
    print("-----------------------", X)
    for it, probString in enumerate(d):
        if len(X) <= size_of_seeked_cipher:
            singleHit = []
            for i, x in enumerate(X):
                if len(X) <= len(probString):
                    singleHit.append(probString[i] ^ ord(x))
                    sent = ''.join(arrayOfNumberToArrayOfASCII(singleHit)).lower()
                    # if probableSentence(sent, minProb, [x.lower() for x in dictlist]):
                    print(sent, it, X, len(probString), len(sent))
            singleHit = []
            