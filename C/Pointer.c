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
    int *y;
    y = &x;

    printf("%u\n", x);  // We will get the value of var x
    printf("%u\n", &x); // We will get the address of var x
    printf("%u\n", y);  // We will get the adress of var x
    printf("%u\n", *y); // We will get the value of var x
    // -> let me assume like this, * and & are opposite to each other, so *y=&x => y=x,
    // ultimately it will print the value of var x if I print *y
    printf("%u\n\n", &y); // We will get the adress of var y

    float a = 69.69;
    void *ptr; // When we use void pointer then we don't get any trouble of declaring int, float, char.
    // Like suppose- It will automatically detect the type casting!
    ptr = &a;

    printf("%f\n", a);
    printf("%u\n", &a);
    printf("%u\n", ptr);
    printf("%f\n", *(float *)ptr); // *ptr -> *(type *)ptr .
                                   // In void case, We have to declare the type there if we want to get the value of var a!
    printf("%u\n", &ptr);
}
