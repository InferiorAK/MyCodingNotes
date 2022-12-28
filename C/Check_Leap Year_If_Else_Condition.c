// Author: InferiorAK
// Leap year Checker

#include <stdio.h>

void check(int a)
{
    // Long Process
    // ------------
    // if (a % 400 == 0)
    // {
    //     printf("Oh! %d is a Leap Year", a);
    // }
    // else if (a % 100 == 0)
    // {
    //     printf("Oh! %d is not a Leap Year", a);
    // }
    // else if ( a % 4 == 0)
    // {
    //     printf("Oh! %d is a Leap Year", a);
    // }

    // Short Process
    // -------------
    if (a % 400 == 0 || a % 100 != 0 && a % 4 == 0)
    {
        printf("Oh! %d is a Leap Year", a);
    }
    else
    {
        printf("Sorry! %d not a Leap Year", a);
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