SHELL = /usr/bin/bash
.PHONY: clear

run: 
	python3 main.py | less
	clear

test:
	python3 test*.py | less
	clear

clear:
	rm *.csv