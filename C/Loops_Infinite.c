// Author: InferiorAK
// Infinite loop in C programming

#include <stdio.h>

int while_loop()
{
    int i = 1;
    while (1) // while(any non-zero number)
    {
        printf("While Loop %d!\n", i);
        i++;
    }
}

int do_loop()
{
    int i = 1;
    do
    {
        printf("Do Loop %d!\n", i);
        i++;
    } while (1);
}

int for_loop()
{
    int i = 1;
    for (;;)
    {
        printf("For Loop %d!\n", i);
        i++;
    }
}

int main()
{
    // while_loop();
    do_loop();
    // for_loop();
    return 0;
}
