// Author: InferiorAK
// checking b*b = ac or not
// One Liner Conditional Code

#include <stdio.h>

int main()
{
    int a, b, c;
    printf("Check b*b = ac or not?\n");
    printf("value => a b c\n=> ");
    scanf("%d %d %d", &a, &b, &c);

    (b * b == a * c) ? printf("Yes! It's Propotional.\n") : printf("No! It's is not Propotional.\n");

    return 0;
}
