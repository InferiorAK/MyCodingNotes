// Author: InferiorAK
// Temperature Converter

#include <stdio.h>

void from_cel(float t)
{
    float F, K;
    F = ((9 * t) / 5) + 32;
    printf("=> Fahrenheit %.2f\n", F);
    K = t + 273;
    printf("=> Kelvin %.2f\n", K);
}

void from_fah(float t)
{
    float C, K;
    C = 5 * (t - 32) / 9;
    printf("=> Celcius %.2f\n", C);
    K = C + 273;
    printf("=> Kelvin %.2f\n", K);
}

void from_kel(float t)
{
    float C, F;
    C = t - 273;
    printf("=> Celcius %.2f\n", C);
    F = ((9 * C) / 5) + 32;
    printf("=> Kelvin %.2f\n", F);
}

int main()
{
    int op;
    float t;

    printf(" Choose Converter\n+================+\n");
    printf("1. From Celcius\n2. From Fahrenheit\n3. From Kelvin\n");
    printf("\n");
    printf("Select Option: ");
    scanf("%d", &op);
    if (op <= 3 && op >= 1)
    {
        printf("Input Temperature: ");
        scanf("%f", &t);

        if (op == 1)
        {
            from_cel(t);
        }
        else if (op == 2)
        {
            from_fah(t);
        }
        else if (op == 3)
        {
            from_kel(t);
        }
    }
    else
    {
        printf("Invalid Input\n");
    }

    return 0;
}
