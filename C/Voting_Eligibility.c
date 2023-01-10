// Author: InferiorAK
// Eligible for Voting or Not?

#include <stdio.h>

void validate(int age)
{
    (age >= 18) ? printf("Eligibe for Voting\n") : printf("Not Eligible for Voting\n");
}

int main()
{
    int age;
    printf("Input your Age: ");
    scanf("%d", &age);
    validate(age);
    return 0;
}
