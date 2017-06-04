COPY_FILES = $(patsubst src/%,output/%,$(wildcard src/*))

all: $(COPY_FILES)

output/%: src/%
	    cp -f $< $@
