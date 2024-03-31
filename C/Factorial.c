// Author: InferiorAK
// Factorial in C programming

#include <stdio.h>

int factorial_with_recursion(int num)
{
    int result = num;
    if (num > 1)
    {
        result *= factorial_with_recursion(num - 1);
        return result;
    }
    else
    {
        return 1;
    }
}

int factorial_with_for_loop(int num)
{
    int result = 1;
    if (num == 1)
    {
        return result;
    }
    else
    {
        for (int i = 1; i < (num + 1); i++)
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
