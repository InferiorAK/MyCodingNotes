// Author: InferiorAK
// Even and Odd Number Checker

#include <stdio.h>

void check(int a)
{
    if (a % 2 == 0)
    {
        printf("Oh! It's an Even Number");
    }
    else
    {
        printf("It's not an Odd Number");
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
