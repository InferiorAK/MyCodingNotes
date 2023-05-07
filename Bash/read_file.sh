#! /bin/bash
## Author: InferiorAK
## file read


read -p "Input your filename: " inp

# method-1
while read x
do
    echo "$x"
done < $inp     # this will redirect to x and the file data will be stored in x. Then using echo, it will be printed.


# method-2
cat $inp | while read x
do
    echo "$x"
done

# method-3
# while IFS=" " read -r x
while IFS= read -r x
do
    echo "$x"
done < $inp
