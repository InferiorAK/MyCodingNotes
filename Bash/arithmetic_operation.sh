#! /bin/bash
## Author: InferiorAK
## Arithmetic Operation in bash


read -p "num1: " num1
read -p "num2: " num2

# method-1
echo $(( num1 + num2 ))
echo $(( num1 - num2 ))
echo $(( num1 * num2 ))
echo $(( num1 / num2 ))
echo $(( num1 % num2 ))

# method-2
echo $( expr $num1 + $num2 )
echo $( expr $num1 - $num2 )
echo $( expr $num1 \* $num2 )
echo $( expr $num1 / $num2 )
echo $( expr $num1 % $num2 )

# method-3
# # apt-get install bc
echo "scale=6;(($num1+$num2)*10^10)/69" | bc
# here scale=6 is used for floating point. It made the output with 6 more digits after decimal point.

echo "scale=2;(($num1+$num2)/sqrt(100))/69" | bc -l
# here flag -l is for library