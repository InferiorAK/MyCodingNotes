// Author: InferiorAK
// Factorial in C programming

#include <stdio.h>

int factorial_with_recursion(int f)
{
    int result = 1;
    if (f == 1)
    {
        return result;
    }
    else
    {
        return f * factorial_with_recursion(f - 1);
    }
}

int factorial_with_for_loop(int f)
{
    int result = 1;
    if (f == 1)
    {
        return result;
    }
    else
    {
        for (int i = 1; i < (f + 1); i++)
        {
            result *= i;
        }
    }
    return result;
}

int main()
{
    printf("%d\n", factorial_with_recursion(10));
    printf("%d", factorial_with_for_loop(10));
    return 0;
}