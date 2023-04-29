#! /bin/bash
## Author: InferiorAK
## Logical "AND" "OR" Operation (leap year checker)


		## Logical AND : && , -a
		## Logical OR  : || , -o


# #   AND Operation
# # <--------------->

read -p "Input Year: " year

var1=$(( year % 100 ))
var2=$(( year % 400 ))
var3=$(( year % 4 ))

# if [[ $var1 -eq 0 && $var2 -eq 0 || $var3 -eq 0 ]]
# if [ $var1 -eq 0 ] && [ $var2 -eq 0 ] || [ $var3 -eq 0 ]
# if [ $var1 -eq 0 -a $var2 -eq 0 ] || [ $var3 -eq 0 ]
if [ $var1 -eq 0 -a $var2 -eq 0 -o $var3 -eq 0 ]
then
	echo "$year is a leap year"
else
	echo "$year is not a leap year"
fi

# Note: If I use && or || inside bracket, then I have to use [[ ]] - double
# But if I use -a or -o inside bracket, then I have to use [] - sinle
# Also the main point is, I can't use -a or -o with && or || together in bracket
