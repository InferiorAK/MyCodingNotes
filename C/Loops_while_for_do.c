// Author: InferiorAK
// Leap year Checker

#include <stdio.h>

// initialization, condition , increment or decrement

void w_h_i_l_e(int i, int n, int diff)
{
    while (i <= n)
    {
        printf("%d\n", i);
        i += diff;
    }
}

void f_o_r(int i, int n, int diff)
{
    for (i; i <= n; i += diff)
    {
        printf("%d\n", i);
    }
}

void d_o(int i, int n, int diff)
{
    do
    {
        i += diff;
    } while (i <= n);
    printf("%d\n", i);
}

int main()
{
    w_h_i_l_e(1, 100, 1);
    f_o_r(1, 100, 1);
    d_o(1, 100, 1);
    return 0;
}