.DEFAULT_GOAL := help


APP_ID := to_gif
APP_NAME := lib_occ
APP_VERSION := 0.0.1


.PHONY: help
help:
	@echo "  Welcome to $(APP_NAME) $(APP_VERSION)!"
	@echo " "
	@echo "  Please use \`make <target>\` where <target> is one of"
	@echo " "
	@echo "  build        		  			  builds the library"
	@echo " "


.PHONY: build
build:
	exec python -m build


