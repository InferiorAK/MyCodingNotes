// Author: InferiorAK
// Vowel-Consonant Checker

#include <stdio.h>

void check(char inp)
{
    switch (inp)
    {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
    case 'A':
    case 'E':
    case 'I':
    case 'O':
    case 'U':
        printf("%c is a Vowel", inp);
        break;

    default:
        printf("%c is a Consonant", inp);
        break;
    }
}

int main()
{
    char inp;
    printf("Input a Character: ");
    scanf("%c", &inp);
    check(inp);
    return 0;
}