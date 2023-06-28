#! /bin/bash
## Author: InferiorAK
## loops

# #     for loop
# #   <---------->

# method-1
for i in {1..20..2}    # initial...final...difference
do
    echo "Welcome for loop1 $i times"
done

# method-2
for (( i=1 ; i<=10 ; i++ ))    # initialization ; condition ; increment/decreement
do
    echo "Welcome for loop2 $i times"
done


# #     while loop
# #   <----------->

x=1     # Always remeber that x = value is not valid. If you give space, it will be counted as command

# while [ $x -le 100 ]
# while (( x <= 100 ))
while (( $x <= 10 ))
do
	echo "While loop $x"
	x=$(( $x + 1 ))
	# x=$(( x + 1 ))
    # (( x++ ))
    # (( ++x ))
done


# #     until loop
# #   <----------->

y=1
until [ $y -ge 10 ]
do
    echo "$y"
    (( y++ ))
done


## single line loop
# for (( i=1 ; i<=10 ; i++ )); do echo "single line code $i times" ; done