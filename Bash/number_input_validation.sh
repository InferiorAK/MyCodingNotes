#! /bin/bash
## Author: InferiorAK
## It will validate the number


read -p "Input a number: " num

if [[ $num =~ ^[0-9]+$ ]] ; then
	echo "Here is your Entered Number: $num"
elif [[ $num =~ ^-?[0-9]+$ ]] ; then
	echo "Here is your Entered Neg Number: $num"
elif [[ $num =~ ^-?[0-9]+([.][0-9]+)?$ || $num =~ ^-?([.][0-9]+)?$ ]] ; then
	echo "Here is your Entered decimal Number: $num"
else
	echo "It's a Text"
fi