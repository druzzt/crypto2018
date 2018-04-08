#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
 
#define bufSize 1024
 
int main(int argc, char *argv[])
{
    FILE *fp1;
    FILE *fp2;
    int c1, c2;
    fp1 = fopen(argv[1], "rb");
    fp2 = fopen(argv[2], "rb");
    if (fp1 && fp2) {
        printf("\n");
        while (((c1 = getc(fp1)) != EOF ) && ((c2 = getc(fp2)) != EOF))
            printf("%c %c \t=\t %d\n", c1, c2, c1==c2);
        fclose(fp1);
        fclose(fp2);
    }
    return 0;
}