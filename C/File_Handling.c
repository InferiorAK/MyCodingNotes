#include <stdio.h>

// Read a File
int read()
{
    FILE *file;
    file = fopen("test.txt", "r");
    if (file == NULL)
    {
        printf("File Doesn't Exist!");
    }
    else
    {
        char MyString[1000];
        // fgets(MyString, 1000, file); // Here 1st line of the file will be stored into MyString Var
        while (fgets(MyString, 1000, file)) // Here all the contents of the file will be stored into MyString Var
        {
            printf("%s", MyString);
        }
        fclose(file);
    }
}

// Write a File
int write()
{
    FILE *file;
    file = fopen("test.txt", "w");
    char txt[] = "Hey I am Testing!";
    fprintf(file, txt);
    fclose(file);
}

// Append to a File
int append()
{
    FILE *file;
    file = fopen("test.txt", "a");
    char txt[] = "\nHey I am Testing!";
    for (int i = 0; i <= 100; ++i)
    {
        fprintf(file, txt);
    }
    fclose(file);
}

int main()
{
    read();
    // write();
    // append();
    return 0;
}