# This is a muscle-memory kind of dirty hack, not a great Makefile.

MAIN=main.py
BOARDVOL=/Volumes/CIRCUITPY
TARGET=$(BOARDVOL)/$(MAIN)

#.PHONY: clean

main: $(MAIN)
	echo "install or clean, there is no try"

install: $(MAIN)
	cp $(MAIN) $(TARGET)

lib: $(MAIN)
	cp -Rv ./lib/* $(BOARDVOL)/lib/

font: $(MAIN)
	cp -Rv ./font/* $(BOARDVOL)/font/


make all: $(MAIN)
	make lib
	make font
	make install

#clean:
# rm -rf *.o
# rm main

