// Author: InferiorAK
// Format Specifiers in C programming


// %o	an octal (base 8) integer
// %d	a decimal integer (assumes base 10)
// %x	a hexadecimal (base 16) integer
// %i	a decimal integer (detects the base automatically)
// %u	int unsigned decimal

// %f	a floating point number for floats
// %e	a floating point number in scientific notation
// %E	a floating point number in scientific notation

// %s	a string
// %c	a single character

// %lf	long double

// %p	an address (or pointer)

// %hi	short (signed)
// %hu	short (unsigned)
// %n	prints nothing
// %%	the % symbol


#include <stdio.h>

int main()
{
    int x = 6969;
    printf("This is a base8!: %o\n", x);
    printf("This is a base10!: %d\n", x);
    printf("This is a base16!: %x\n", x);
    printf("This is an unsigned integer!: %i\n\n", x);

    float y = 696969.695;
    printf("This is a float!: %f\n", y);
    printf("This is a float!: %15.9f before\n", y); // a = +ve, so it's taking char space before the floating num
    printf("This is a float!: %-15.9f after\n", y); // a = -ve, so it's taking char space after the floating num
    // printf("%a.bf", var) --> here a=total character space taking, b=number showing after point "."
    printf("This is a scintific format!: %e\n", y); // 10^times format
    printf("This is a scintific format!: %E\n\n", y);

    char z = '1';   // 1 byte	Stores a single character/letter/number, or ASCII values
    char z2[] = "12345";
    char z3[3] = "cw";
    char z4[] = "casio-991cw";
    printf("This is sigle character!: %c\n", z);
    printf("This is indexed sigle character!: %c\n", z2[4]);
    printf("This is 2 characters!: %s\n", z3);
    printf("This is a string!: %s\n\n", z4);

    int p = -6969;
    char p2 = 'a';  // Keep in mind that, you have to use single quote in this case!
    printf("This is an unsigned integer!: %u\n", p); // The -6969 value is converted into it's positive equivalent by %u
    printf("This is ASCII Value of the Character!: %u\n\n", p2);

    float q = 15486415486465846841545454643215484864154.52315144564;
    double r = 15486415486465846841545454643215484864154.52315144564;
    printf("This is a float!: %f\n", q);
    printf("This is long float!: %lf\n\n", r);  // long float

    int *ptr = &x;
    printf("The address in decimal : %d\n", ptr); 
    printf("The address in hexadecimal : %p\n", ptr);

    return 0;
}