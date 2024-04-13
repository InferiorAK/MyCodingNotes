// Author: InferiorAK
// Infinite loop in C programming

#include <stdio.h>

int while_loop()
{
    while (1) // while(any non-zero number)
    {
        printf("While Loop!\n");
    }
}

int for_loop()
{
    for (;;)
    {
        printf("For Loop!\n");
    }
}

int main()
{
    while_loop();
    // for_loop();
    return 0;
}