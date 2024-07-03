#! /bin/bash
## Author: InferiorAK
## If Else condition part 1 (basics + textual and numeric testing)

## All Conditional Flags that needed to know

# integer comparisons:
        # -eq : equal to  --  if [ "$a" -eq "$b" ]
        # -ne : not equal to  --  if [ "$a" -ne "$b" ]
        # -lt : less than  -- if [ "$a" -lt "$b" ]
        # -gt : greater than  -- if [ "$a" -gt "$b" ]
        # -le : less than equal to  -- if [ "$a" -le "$b" ]
        # -ge : greater than equal to  -- if [ "$a" -ge "$b" ]
        #  <  : less than  -- if (( "$a" < "$b" ))
        #  >  : greater than  -- if (( "$a" > "$b" ))
        #  <= : less than equal to  -- if (( "$a" <= "$b" ))
        #  >= : greater than equal to  -- if (( "$a" >= "$b" ))

# string comparisons
        #  =  : equal to  --  if [ "$a" = "$b" ]
        # ==  : equal to  --  if [ "$a" == "$b" ]    # or, if [[ "$a" == "$b" ]]
        # !=  : not equal to  --  if [ "$a" != "$b" ]
        #  <  : less than (in ASII alphabetical order)  --  if [[ "$a" < "$b" ]]
        #  >  : greater than (in ASII alphabetical order)  --  if [[ "$a" > "$b" ]]
        # -z  : null string (zero length string)

# file and directory testing flags
        # -b  : checks block special file  --  if [ -b $file ]
        # -c  : checks character special file  --  if [ -c $file ]
        # -d  : checks existence of a directory  --  if [ -d $dir ]
        # -e  : checks file existence  --  if [ -e $file ]
        # -f  : checks file existence & regular type or not  --  if [ -f $file ]
        # -s  : checks file is empty or not  --  if [ -s $file ]
        # -r  : checks file existence & read permission  --  if [ -r $file ]
        # -w  : checks file existence & write permission  --  if [ -w $file ]
        # -x  : checks file existence & execute permission  --  if [ -x $file ]


# Note: integer and string condition format diffrence is in brackets (( )) , [[ ]] ... while using common conditional operators of them ... like "<" ">" "<=" and ">="


# #   integer
# # <--------->

read -p "input a number: " num

if [ $num -gt 69 ]
# if (( $num > 69 ))
then
    echo "It's greater than 69"
elif [ $num -eq 69 ]
then
    echo "Oh! I liked 69"
# elif [ $num -lt 69 ]
elif (( $num < 69 ))
then
    echo "It's less than 69"
else
    echo "Sorry, It's unexpected"
fi


# #   string
# # <--------->

read -p "input text: " txt

# if [ $txt == "hey" ]
if [ $txt == "hey" ]
then
    echo "yo man!"
elif [[ $txt < "hey" ]]     # in this case each character will be compared to "hey" string sequentially
then
    echo "so little"
else
    echo "$txt"
fi
