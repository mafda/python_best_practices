#!/bin/bash

clear

for file in $(find ./src/ -type f -name "*.py")
do  
	isort ${file}  
	black --line-length 79 ${file}  
	flake8 ${file}
done
