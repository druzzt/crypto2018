#!/bin/bash

# ENC FILE: -----------
# ./encDec.sh -ef fileToEncrypt keyToEncrypt 00001
if [[ $1 == "-ef"]]
then 
    cat $2 | openssl enc -e -aes-256-cbc -k $3 -nosalt -iv $4 > $2.e
fi
# ---------------

# DEC FILE: ----------
# ./encDec.sh -df fileToDecrypt keyToEncrypt 00001
if [[ $1 == "-df"]]
then
    cat $2 | openssl enc -d -aes-256-cbc -k $3 -nosalt -iv $4 > $2.d
fi
# ---------------

# ENC ORACLE: -----------
# ./encDec.sh -eo m0.file m1.file keyToEncrypt 00001
if [[ $1 == "-eo" ]]
then
    cat $2 | openssl enc -e -aes-256-cbc -k $4 -nosalt -iv $5 > $2.e
    cat $3 | openssl enc -e -aes-256-cbc -k $4 -nosalt -iv $5 > $3.e
fi
# ---------------

# DEC ORACLE: --------
# ./encDec.sh -do m0.e m1.e keyToEncrypt 00001
if [[ $1 == "-do"]]
then
    cat $2 | openssl enc -d -aes-256-cbc -k $4 -nosalt -iv $5 > $2.d
    cat $3 | openssl enc -d -aes-256-cbc -k $4 -nosalt -iv $5 > $3.d
fi
# ---------------


# CHALLENGE ORACLE: ------- 
# ./encDec.sh -co costam0 costam1 keyToEncrypt 00001
if [[ $1 == "-co" ]]
then
    random_index=$((RANDOM%2))+1
    args=("$@")
    random_msg=${args[$random_index]}
    echo $random_msg | openssl enc -e -aes-256-cbc -k $4 -nosalt -iv $5
fi
# ---------------






# # if [[ $1 == "-eo" ]]
# # then
# #     i=1
# #     for arg do
# #         if [[ i -gt 3 ]]
# #         then
# #             # printf '%s\n' "Arg $i: $arg" | openssl enc -aes-256-cbc -k $2 -nosalt
# #             printf '%s\n' "$arg" | openssl enc -aes-256-ofb -k $2 -nosalt > $3
# #             # printf '\n' >> EO.enc
# #         fi
# #         i=$((i + 1))
# #     done
# #     exit 1
# # fi

# # if [[ $1 == "-d" ]]
# # then
# #     openssl enc -d -aes-256-cbc -in $2 -out $3 -iv $4 -nosalt
# # else
# #     openssl enc -aes-256-cbc -in $1 -out $2 -iv $3 -nosalt
# # fi