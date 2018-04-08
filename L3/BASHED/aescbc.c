#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>
#include <openssl/rand.h>

// a simple hex-print routine. could be modified to print 16 bytes-per-line
static void hex_print(const void* pv, size_t len)
{
    const unsigned char * p = (const unsigned char*)pv;
    if (NULL == pv)
        printf("NULL");
    else
    {
        size_t i = 0;
        for (; i<len;++i)
            printf("%02X ", *p++);
    }
    printf("\n");
}

static void hex_xor(const void* pv, size_t len, const void* ky, size_t klen)
{
    const unsigned char * p = (const unsigned char*)pv;
    const unsigned char * k = (const unsigned char*)ky;
    if(NULL == pv) printf("NULL");
    else 
    {
        size_t i = 0;
        for(; i<len;++i) printf("{ %02X, %02X, %02X } ", *p, *k, *p++^*k++);
    }
    printf("\n");
}

// main entrypoint
int main(int argc, char **argv)
{
    int keylength;
    printf("Give a key length [only 128 or 192 or 256!]:\n");
    scanf("%d", &keylength);

    /* generate a key with a given length */
    unsigned char aes_key[keylength/8];
    memset(aes_key, 0, keylength/8);
    if (!RAND_bytes(aes_key, keylength/8))
        exit(-1);
    printf("aes_key:[%s]\n", aes_key);

    size_t inputslength = 0;
    printf("Give an input's length:\n");
    scanf("%lu", &inputslength);

    /* generate input with a given length */
    unsigned char aes_input[inputslength];
    memset(aes_input, 'X', inputslength);

    /* init vector */
    unsigned char iv_enc[AES_BLOCK_SIZE], iv_dec[AES_BLOCK_SIZE];
    RAND_bytes(iv_enc, AES_BLOCK_SIZE);
    memcpy(iv_dec, iv_enc, AES_BLOCK_SIZE);
    printf("iv_enc[%s] \t iv_dec[%s]\n", iv_enc, iv_dec);

    // buffers for encryption and decryption
    const size_t encslength = ((inputslength + AES_BLOCK_SIZE) / AES_BLOCK_SIZE) * AES_BLOCK_SIZE;
    unsigned char enc_out[encslength];
    unsigned char dec_out[inputslength];
    memset(enc_out, 0, sizeof(enc_out));
    memset(dec_out, 0, sizeof(dec_out));

    printf("original:\t");
    hex_print(aes_input, sizeof(aes_input));
    
    printf("key:\t\t");
    hex_print(aes_key, sizeof(aes_key));

    printf("IV:\t\t");
    hex_print(iv_enc, sizeof(iv_enc));

    printf("encrypt:\t");
    hex_print(enc_out, sizeof(enc_out));

    printf("decrypt:\t");
    hex_print(dec_out, sizeof(dec_out));
    printf("--------------\n");


    // so i can do with this aes-cbc-128 aes-cbc-192 aes-cbc-256
    AES_KEY enc_key, dec_key;
    AES_set_encrypt_key(aes_key, keylength, &enc_key);
    AES_cbc_encrypt(aes_input, enc_out, inputslength, &enc_key, iv_enc, AES_ENCRYPT);

    AES_set_decrypt_key(aes_key, keylength, &dec_key);
    AES_cbc_encrypt(enc_out, dec_out, encslength, &dec_key, iv_dec, AES_DECRYPT);
    
    printf("original:\t");
    hex_print(aes_input, sizeof(aes_input));
    
    printf("key:\t\t");
    hex_print(aes_key, sizeof(aes_key));

    printf("IV:\t\t");
    hex_print(iv_enc, sizeof(iv_enc));

    printf("encrypt:\t");
    hex_print(enc_out, sizeof(enc_out));

    printf("decrypt:\t");
    hex_print(dec_out, sizeof(dec_out));

    // printf("XOR:\t");
    // hex_xor(dec_out, sizeof(dec_out), dec_key, sizeof(dec_key));

    return 0;
}