#! /bin/bash
## Author: InferiorAK
## sleep

i=20
while [ i -gt 0 ]
do
	echo "$i"
	(( --i ))
	sleep 0.1
done