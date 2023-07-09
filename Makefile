# Makefile for 
# C++

## Ingredients/Variables
### Project
CC = g++
CFLAGS =
SRC = main.cpp
SRC_DIR = src/
BIN = cpp-practice
OUT_DIR = out/
PREFIX = /usr/local/bin ## user install directory

### Environment
SHELL = /bin/bash

### Defaults
.PHONY := help
.DEFAULT_RULES := help

## Recipes/Targets
help:
	## Display all commands
	@echo -e "\thelp      : Display this help menu and all commands"
	@echo -e "\tsetup     : Perform setup and prepare dependencies"
	@echo -e "\tbuild     : Compile/build project into binary"
	@echo -e "\tclean	  : Clean temporary files generated"
	@echo -e "\tinstall   : Install binary/files into system directory"
	@echo -e "\tuninstall : Uninstall/Remove installed files from system"

setup:
	## Setup process
	### Check directories
	@test -d ${OUT_DIR} || mkdir -p ${OUT_DIR}

build: setup
	## Compile/build source code
	${CC} ${CFLAGS} -o ${OUT_DIR}/${BIN} ${SRC_DIR}/${SRC}

clean: setup
	## Clean up temporary files generated

install: setup
	## Install binary/files into system directory
	@install 0644 ${OUT_DIR}/${BIN} ${PREFIX}

uninstall: setup
	## Uninstall/remove installed files from system
	@rm ${PREFIX}/${BIN}

