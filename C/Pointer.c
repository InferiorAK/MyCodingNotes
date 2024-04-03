// Author: InferiorAK
// Pointer in C programming

#include <stdio.h>

// # Basic:
// & = Referencing Operator
// * = Dereferncing Operator
// %u = Unsigned Operator -> We use this for Adress, Cz Adress is always +ve Value

int main()
{
    int x = 69;
    int *y = &x;

    printf("%u\n", x);    // We will get the value of var x
    printf("%u\n", &x);   // We will get the address of var x
    printf("%u\n", y);   // We will get the adress of var x
    printf("%u\n", *y);   // We will get the value of var x
    // -> let me assume like this, * and & are opposite to each other, so *y=&x => y=x,
    // ultimately it will print the value of var x
    printf("%u\n", &y);   // We will get the adress of var y
}