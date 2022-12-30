// Author: InferiorAK
// Constant using

#include <stdio.h>
#define size 6 // preprocessor constant
#define shape "long cylinder"

int main()
{
    const int size2 = 7; // keyword constant
    const char shape2[] = "very long cylinder";

    printf("%s and %d\n", shape, size);
    printf("%s and %d", shape2, size2);
    return 0;
}
