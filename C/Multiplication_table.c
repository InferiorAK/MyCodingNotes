// Author: InferiorAK
// Multiplication table

#include <stdio.h>

void mt(int a)
{
    int b;
    for (b = 1; b <= 10; b++)
    {
        printf("%d X %d = %d\n", a, b, a * b);
    }
}

int main()
{
    int a;
    printf("Input Your Number: ");
    scanf("%d", &a);
    mt(a);
    return 0;
}
