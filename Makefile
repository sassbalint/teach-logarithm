SHELL:=/bin/bash

all:
	@echo "choose explicit target = type 'make ' and press TAB"

S=scripts
I=data
O=out


# ===== MAIN STUFF 

SCRIPT=$S/log_y_axis.py
nevek:
	@echo "--- $@" 1>&2
	rm -f log_y_nevek.png ; clear ; python3 $(SCRIPT) > log_y_nevek.csv ; eog log_y_nevek.png 

