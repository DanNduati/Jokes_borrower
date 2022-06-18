#!/bin/bash

id_ranges=(0 100 200)
echo "Borrowing initiated"
for value in ${id_ranges[@]};do
	echo "started borrowing at id ${value}"
	python main.py $value
	sleep 60
done
echo All done
