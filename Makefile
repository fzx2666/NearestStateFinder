.SUFFIXES:
# .SUFFIXES: .o .cpp
#============================================================


PYTHON_SCRIPT_FOLDER =  ./pyscipt
ELECTRON_FOLDER     =  ./gui
NODE_FOLDER = ./node
NODE_DOWNLOAD = https://nodejs.org/dist/v15.4.0/node-v15.4.0-linux-x64.tar.gz


# -Wall

#============================================================
all: 
echo hello

# Implicit rules: $@ = target name, $< = first prerequisite name, $^ = name of all prerequisites
#============================================================

ALL_SOURCES = Makefile $(C_SOURCES) $(MY_INCLUDES)

NOTES =
%= otherstuff.np 

clean:
	rm -f $(ELECTRON_FOLDER)/dist_electron



