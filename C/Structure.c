// Author: InferiorAK
// Structures in C programming

#include <stdio.h>
#include <string.h>

// struct NewTest
// {
//     char name[30];
//     int class;
//     char section;
//     int roll;
// } test1, test2;
// Or,

struct NewTest
{
    char name[30];
    int class;
    char section;
    int roll;
};

int main()
{
    // struct NewTest test1 = {"InferiorAK", 13, 'B', 8617};
    // Or,
    
    struct NewTest test1, test2;
    
    strcpy(test1.name, "InferiorAK");
    test1.class = 10;
    test1.section = 'B';
    test1.roll = 8617;

    strcpy(test2.name, "InferiorAK2");
    test2.class = 12;
    test2.section = 'B';
    test2.roll = 12562;

    printf("%s %d %c %d\n", test1.name, test1.class, test1.section, test1.roll);
    printf("%s %d %c %d\n", test2.name, test2.class, test2.section, test2.roll);
    return 0;
}
