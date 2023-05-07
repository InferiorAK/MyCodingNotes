#! /bin/bash
## Author: InferiorAK
## Array in Bash


# #   IndexedArray			# In python this method is called listing
# # <-------------->
declare -a array1=("babe" "boy" "bootstrap" "baby")
echo "${array1[@]}"     # for printing all values
echo "${array1[3]}"     # for printing specific value

array1+=("hello" "bye")		# this will add more values
echo "with new values added : ${array1[@]}"

unset array1[3]		# this will remove the indexed value
echo "with removing value : ${array1[@]}"

count=0
for mal in ${array1[@]}
do
	echo "$count. $mal"
	(( count ++ ))
done

# #   AssociativeArray		# In python this method is called dictionary
# # <------------------>
declare -A array2=(
	[key1]="value1"
	[key2]="value2"
	[key3]="value3"
	[key4]="value4"
	[key5]="value5"
	[key6]="value6"
)
echo "${array2[@]}"		# for printing all values
echo "${!array2[@]}"	# for printing all keys

array2+=([bal]="chal")	# adding more key=value
echo "${array2[@]}"

unset array2[bal]		# this will remove the given key with value
echo "with removing value : ${array2[@]}"

for key in "${!array2[@]}"
do
	echo "Key: $key , Value: ${array2[$key]}"
done

# for key in $(echo "${!array2[@]}" | tr ' ' '\n' | sort)		# sorting / sequentially ordering
# do
# 	echo "Key: $key , Value: ${array2[$key]}"
# done

# function test
# {
function test(){
	declare -ga test_AI=(nana tata)
	declare -gA test_AA=([test3]=banana [test4]=potato)
}
test
echo "IndexedArray from a function: ${test_AI[@]}"			# Declaring global IndexedArray in a function. the flag is -ga
echo "AssosiativeArray from a function: ${test_AA[@]}"		# Declaring global AssosiativeArray in a function. the flag is -gA


function Iteration
{
	vehicles=${#IndexedArray[@]}
	for (( i=0; i<vehicles; i++ ))
	do
		echo ${IndexedArray[$i]}
	done
}
IndexedArray=(car rickshaw cycle plane)
echo "** New Iteration **"
Iteration ${IndexedArray[@]}