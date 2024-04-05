// Author: InferiorAK
// Dynamic Memorty Allocation in C programming

#include <stdio.h>
#include <stdlib.h> // Allocation Library for gcc Compiler

int m_alloc()   // Memory Allocation
{
    int *ptr, i, count;
    printf("How many numbers you want to test with?: ");
    scanf("%d", &count);
    //    (data_type *)malloc(size_bytes)
    ptr = (int *)malloc(i * sizeof(count)); // Here we have already declared total memory size with malloc.
                                            // Memory size will be 4bytes*counts = Total bytes

    if (ptr == NULL)
    {
        printf("Memory not Available!");
        exit(1);
    }
    else
    {
        for (i = 0; i < count; i++)
        {
            printf("Input your number %d: ", i + 1);
            scanf("%d", ptr + i); // Here we are increasing ptr adress value by 1 each time!
                                  // Suppose, Primary ptr address is 1000, now we are increasing
                                  // it like this: 1001, 1002, 1003 , .......
                                  // Thus we are making this, allocated with given bytes with sequential Address
        }
    }
    for (i = 0; i < count; i++)
    {
        printf("Number %d: %d\n", i + 1, *(ptr + i)); // Here the values of ptr will be printed sequentially
    }
}

int c_alloc()   // Contiguous Allocation
{
    int *ptr, i, count;
    printf("How many numbers you want to test with?: ");
    scanf("%d", &count);
    //    (data_type *)calloc(block_count, size_bytes_per_block)
    ptr = (int *)calloc(8, i * sizeof(count)); // Here we have already declared total blocks and memory size with calloc.
                                               // Memory size will be 4bytes*counts = Total bytes

    if (ptr == NULL)
    {
        printf("Memory not Available!");
        exit(1);
    }
    else
    {
        for (i = 0; i < count; i++)
        {
            printf("Input your number %d: ", i + 1);
            scanf("%d", ptr + i);
        }
    }
    for (i = 0; i < count; i++)
    {
        printf("Number %d: %d\n", i + 1, *(ptr + i)); // Here the values of ptr will be printed sequentially
    }
}

int main()
{
    // m_alloc();  // malloc() contains Garbage Value Initially
    c_alloc();  // calloc() contains 0 at initialization
    return 0;
}