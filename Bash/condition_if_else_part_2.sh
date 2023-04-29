#! /bin/bash
## Author: InferiorAK
## condition part 1 (file and directory testing)


# #   file testing
# # <-------------->
read -p "input file PATH to check: " file

if [ -e $file ]
then
	echo "$file is present"

	if [ -s $file ]
	then
		echo "$file is not Empty"
	else
		echo "$file is Empty"
	fi

	if [ -x $file ]
	then
		echo "$file is Executable"
	else
		echo "$file is not Executable"
	fi

else
	echo "$file is Missing or Wrong PATH"
fi