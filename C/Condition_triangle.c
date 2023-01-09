// Author: InferiorAK
// Validate Triangle fomation
// One Liner Conditional Code

#include <stdio.h>

void validate(float a, float b, float c)
{
    ((a || b || c)!=0 && (a + b) > c && (a + c) > b && (b + c) > a) ? printf("Possible.\n") : printf("Not Possible.\n");
}

int main()
{
    float a, b, c;
    printf("Triangle Fomation Possible or not?\n");
    printf("value => a b c\n=> ");
    scanf("%f %f %f", &a, &b, &c);
    validate(a, b, c);
    return 0;
}
