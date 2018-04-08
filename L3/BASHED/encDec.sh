#!/bin/bash

# ENC FILE: -----------
# ./encDec.sh -ef fileToEncrypt keyToEncrypt 00001
if [[ $1 == "-ef" ]]
then 
    cat $2 | openssl enc -e -aes-256-cbc -k $3 -nosalt -iv $4
fi
# ---------------

# DEC FILE: ----------
# ./encDec.sh -df fileToDecrypt keyToEncrypt 00001
if [[ $1 == "-df" ]]
then
    cat $2 | openssl enc -d -aes-256-cbc -k $3 -nosalt -iv $4
fi
# ---------------

# ENC ORACLE: -----------
# # ./encDec.sh -eo m0.file m1.file keyToEncrypt 00001
# # cat $2 | openssl enc -e -aes-256-cbc -k $4 -nosalt -iv $5 > $2.e
# # cat $3 | openssl enc -e -aes-256-cbc -k $4 -nosalt -iv $5 > $3.e
# ./encDec.sh -eo keyToEncrypt 000001 m0 ... mq
if [[ $1 == "-eo" ]]
then
    i=1
    for arg do
        if [[ i -gt 3 ]]
        then
            echo $arg | openssl enc -e -aes-256-cbc -k $2 -nosalt -iv $3 #> $arg.enc
        fi
        i=$((i + 1))
    done
fi
# ---------------

# # DEC ORACLE: --------
# # ./encDec.sh -do m0.e m1.e keyToEncrypt 00001
# if [[ $1 == "-do" ]]
# then
#     cat $2 | openssl enc -d -aes-256-cbc -k $4 -nosalt -iv $5 > $2.d
#     cat $3 | openssl enc -d -aes-256-cbc -k $4 -nosalt -iv $5 > $3.d
# fi
# # ---------------


# CHALLENGE ORACLE: ------- 
# ./encDec.sh -co costam0 costam1 keyToEncrypt 00001
if [[ $1 == "-co" ]]
then
    random_index=$((RANDOM%2))+1
    args=("$@")
    random_msg=${args[$random_index]}
    cat $random_msg | openssl enc -e -aes-256-cbc -k $4 -nosalt -iv $5
    # printf "\n"
fi
# ---------------


# DEC MSG:  ------- 
if [[ $1 == "-dm" ]]
then
    cat $2 | openssl enc -d -aes-256-cbc -k $3 -nosalt -iv $4
fi
# ---------------

# PREDICT MODE: -------
if [[ $1 == "-p" ]]
then
    make
    # printf "\n"
    ivPrevious=46454544
    ivPredicte=46454545
    ./encDec.sh -eo keyToEncrypt $ivPrevious $2 > $2.enc
    # ./encDec.sh -df $2.enc keyToEncrypt $ivPredicte
    # ./encDec.sh -df $2.enc keyToEncrypt $ivPrevious
    ./predict $ivPrevious $ivPredicte $2.enc > $2.predict
    ./encDec.sh -co $2.predict $3 keyToEncrypt $ivPredicte > $2.enc2
    ./encDec.sh -dm $2.enc2 keyToEncrypt $ivPredicte
    ./distinguishMsgs $2.enc2 $2.enc
    printf "\n"
fi
# ---------------