// Author: InferiorAK
// Pattern

#include <stdio.h>

void triangle(int count)
{
    int i, j;
    for (i = 1; i <= count; i++)
    {
        for (j = 1; j <= i; j++)
        {
            // printf("%d", j);
            printf("*");
        }
        printf("\n");
    }
}
void rev_triangle(int count)
{
    int i, j;
    for (i = count; i >= 1; i--)
    {
        for (j = 1; j <= i; j++)
        {
            // printf("%d", j);
            printf("*");
        }
        printf("\n");
    }
}

int main()
{
    int count;
    printf("Number of Lines: ");
    scanf("%d", &count);

    // triangle(count);
    rev_triangle(count);

    return 0;
}