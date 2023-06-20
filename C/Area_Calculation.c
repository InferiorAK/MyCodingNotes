// Author: InferiorAK
// Area Calculation of some fields

#include <stdio.h>
#include <math.h>
#define PI 3.1416 // value of PI constant

//  options
// ---------
// r = radius
// a = side
// b = base
// h = height

float area;

int cricle(){
    float r;
    printf("Input radius: ");
    scanf("%f", &r);
    area = PI * r*r;
    printf("Area of the Circle is : %.3f\n", area); // %.3f, here .3 means there will be 3 digits after point
}

int triangle(){
    float b, h;
    printf("Input base and height: ");
    scanf("%f %f", &b, &h);
    area = 0.5 * b * h;
    printf("Area of the Triangle is : %.3f\n", area);
}

int isosceles_triangle()
{
    float a, b;
    printf("Input a and b: ");
    scanf("%f %f", &a, &b);
    area = (b/4) * sqrt(a*a - b*b);
    printf("Area of the Isosceles Triangle is : %.3f\n", area);
}

int equilateral_triangle(){
    float a;
    printf("Input side: ");
    scanf("%f", &a);
    area = (sqrt(3)/4) * a*a;
    printf("Area of the Equilateral Triangle is : %.3f\n", area);
}

int square(){
    float a;
    printf("Input side: ");
    scanf("%f", &a);
    area = a*a;
    printf("Area of the Square is : %.3f\n", area);
}

int rectangle(){
    float a, b;
    printf("Input length and width : ");
    scanf("%f %f", &a, &b);
    area = a*b;
    printf("Area of the Rectangle is : %.3f\n", area);
}

int rhombus(){
    float d1, d2;
    printf("Input d1 and d2: ");
    scanf("%f %f", &d1, &d2);
    area = 0.5 * d1*d2;
    printf("Area of the Rhombus is : %.3f\n", area);
}

int parellelogram(){
    float d1, d2;
    printf("Input d1 and d2: ");
    scanf("%f %f", &d1, &d2);
    area = d1*d2;
    printf("Area of the Parallel is : %.3f\n", area);
}

int main(){
    printf("  Area Calculator\n*=================*\n");
    printf("01. Circle\n");
    printf("02. Triangle\n");
    printf("03. Isosceles Triangle\n");
    printf("04. Equilateral triangle\n");
    printf("05. Square\n");
    printf("06. Rectangle\n");
    printf("07. Rhombus\n");
    printf("08. Parellelogram\n");

    int c;
    printf("Choose Option: ");
    scanf("%d", &c);
    if (c <= 8){
        if (c == 1){
            cricle();
        }
        else if (c ==2){
            triangle();
        }
        else if (c ==3){
            isosceles_triangle();
        }
        else if (c ==4){
            equilateral_triangle();
        }
        else if (c ==5){
            square();
        }
        else if (c ==6){
            rectangle();
        }
        else if (c ==7){
            rhombus();
        }
        else{
            parellelogram();
        };
    }
    else{
        printf("Invalid Choice");
    };

    return 0;
}
