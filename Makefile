.SUFFIXES:
# .SUFFIXES: .o .cpp
#============================================================


PYTHON_SCRIPT_FOLDER =  ./pyscript
ELECTRON_FOLDER     =  ./gui
NODE_FOLDER = ./node
NODE_DOWNLOAD = https://nodejs.org/dist/v15.4.0/node-v15.4.0-linux-x64.tar.gz
setpath = export PATH=$(CURDIR)/node-v15.4.0-linux-x64/bin/:$$PATH; 

# -Wall

#============================================================
all: 
	wget $(NODE_DOWNLOAD)
	tar -xvf node-v15.4.0-linux-x64.tar.gz
	$(setpath) npm -v
	cd $(ELECTRON_FOLDER)
	$(setpath) cd $(ELECTRON_FOLDER); npm install
	$(setpath) cd $(ELECTRON_FOLDER); ./node_modules/.bin/vue-cli-service electron:build
	cp -R $(PYTHON_SCRIPT_FOLDER) $(ELECTRON_FOLDER)/dist_electron/linux-unpacked/
# Implicit rules: $@ = target name, $< = first prerequisite name, $^ = name of all prerequisites
#============================================================
run: all
	$(ELECTRON_FOLDER)/dist_electron/linux-unpacked/gui


clean:
	rm -rf $(ELECTRON_FOLDER)/dist_electron.
	rm -rf node-v15.4.0-linux-x64.tar.gz
	rm -rf node-v15.4.0-linux-x64



