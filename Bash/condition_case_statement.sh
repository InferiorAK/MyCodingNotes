#! /bin/bash
## Author: InferiorAK
## case condition

read -p "Input your username: " user

case $user in
	"InferiorAK" )
		echo "Correct Username" ;;
	"inferiorak" )
		echo "Well done!" ;;
	? )
		echo "What have you entered bloody fool? A symbol!" ;;
	* )
		echo "You are Obviuosly a fool! Ungabunga" ;;
esac