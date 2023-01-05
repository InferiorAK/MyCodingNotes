// Author: InferiorAK
// Even and Odd Number Checker

#include <stdio.h>

void check(int a)
{
    switch (a % 2)
    {
    case 0:
        printf("Oh! It's an Even Number");
        break;
    default:
        printf("It's an Odd Number");
        break;
    }
}

int main()
{
    int a;
    printf("input a number: ");
    scanf("%d", &a);
    check(a);
    return 0;
}
