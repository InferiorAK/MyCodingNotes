// Author: InferiorAK
// Array in C Programming

// string  --> char ArrayName[total_strings][string_length] = {element1, element2, ...}
// integer --> int ArrayName[row][column] = {{num, num, num, ...}, {num, num, num, ...}, ...}

#include <stdio.h>

int chr_array()
{
	char array[][4] = {"hey", "love", "you"};
	int i;
	for (i = 0; i <= 2; i++)
	{
		printf("%s\n", array[i]);
	}
	printf("array simple demo: %s\n", array[0]);
}

int int_array()
{
	int array2[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	printf("array2 simple demo: %d\n", array2[2]);

	int array3[3][4] = {
		// col1 col2 col3 col4
		{1, 2, 3, 4},	  // row1
		{11, 12, 13, 14}, // row2
		{21, 22, 23, 24}  // row3
	};
	printf("array3 simple demo: %d\n", array3[1][3]); // but everything starts with 0, here array3[1][3] means - array[row2][col4] element
	int j, k;
	for (j = 0; j <= 2; j++)
	{
		for (k = 0; k <= 3; k++)
		{
			printf("%d ", array3[j][k]);
		};
	};
	printf("\n");
}


#define len(array) (sizeof(array) / sizeof(array[0]))
int main()
{
	chr_array();
	int_array();

	int arr[] = {1, 2, 3, 4, 5};
	printf("length of the array 'arr' is: %d\n", len(arr));
	return 0;
}
