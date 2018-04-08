#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>

unsigned char* hexstr_to_char(const char* hexstr)
{
    size_t len = strlen(hexstr);
    if(len %2 != 0)
        return NULL;
    size_t final_len = len / 2;
    unsigned char* chrs = (unsigned char*)malloc((final_len+1) * sizeof(*chrs));
    for (size_t i=0, j=0; j<final_len; i+=2, j++)
        chrs[j] = (hexstr[i] % 32 + 9) % 25 * 16 + (hexstr[i+1] % 32 + 9) % 25;
    chrs[final_len] = '\0';
    return chrs;
}

int main(int argc, char* argv[])
{
    FILE *fp1;
    fp1 = fopen(argv[3], "r");
    char c1;
    int column = 0;
    unsigned char* iv1 = hexstr_to_char(argv[1]);
    unsigned char* iv2 = hexstr_to_char(argv[2]);
    if (fp1) {
        while (((c1 = getc(fp1)) != EOF )) {
            column++;
            printf("%c", c1 ^ iv1[column-1] ^ iv2[column-1]);
        }
        fclose(fp1);
    }
	return 0;
}
