#! /bin/bash
## Author: InferiorAK
## Define a function method

# method-1
example_1(){
	echo "You can also do it with <function_name>(){  code  }"
	for (( i=1; i<=5; i++ ))
	do
		echo "This is $1 $i"
	done
}
example_1 "example"


example_2(){ for (( i=1; i<=5; i++ )) ; do echo "This is $1 $i" ; done }        # Also it can be in single line like this
example_2 "example2"

# method-2
function method_2(){
	echo "You can also do it with function <function_name>(){  code  }"
}
method_2