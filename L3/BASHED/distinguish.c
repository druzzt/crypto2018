#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	char ch;
	int wordCounter = 0;
	char* word = malloc(1 * sizeof(char));
	char** sentence = malloc(1 * sizeof(*word));
	int letter_in_word = 0;
	while(read(STDIN_FILENO, &ch, 1) > 0)
	{
		letter_in_word++;
		word = realloc(word, letter_in_word * sizeof(*word));
		if(ch == ' ') {
			printf("{%s} \n", word);
			wordCounter++;
			letter_in_word = 0;
			sentence = realloc(sentence, wordCounter * sizeof(*sentence));
			sentence[wordCounter-1] = word;
			printf("[%s]\n", sentence[wordCounter-1]);
		} else {
			word[letter_in_word-1] = ch;
		}
	}
	printf("{%s} \n", word);
	free(word);
	free(sentence);
	printf("------\n");
	return 0;
}
