#!/bin/bash

id_ranges=(0 100 200 300)
for value in ${id_ranges[@]};do
	python main.py $value
	sleep 70
done
echo All done
