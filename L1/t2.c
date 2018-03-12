/** https://www.mathstat.dal.ca/~selinger/random/ */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 1000
int correct = 0;
int predicted[SIZE];
int input[SIZE];

/// oi = oi-31 + oi-3 mod 2^31 or oi = oi-31 + oi-3 + 1 mod 2^31, for all i ≥ 31.
void predict_rand(int start) {
    int i31 = input[start - 31];
    int i3 = input[start - 3];
    int prediction = (i31 + i3) % (1 << 31);
    printf("Which index=%d; what value=%d\n", start, prediction);
    predicted[start] = prediction;
}

int main() {
    srand(time(NULL));
    int i = 0;
    for(i = 0; i < SIZE; i++) {
        input[i] = rand();
        if(i >= 31) {
            predict_rand(i);
            if(input[i] == predicted[i - 31]) {
                // prediction went ok
                correct = correct + 1;
            }
        }
    }
    return correct;
}
