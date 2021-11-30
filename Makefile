COPY_FILES = $(patsubst src/%,output/%,$(wildcard src/*))

all: download $(COPY_FILES) \
	output/understanding-video.mp4

download: \
	src/understanding-video.mp4

COPY_FILES = $(patsubst src/%,output/%,$(wildcard src/*))

src/understanding-video.mp4:
	curl -k -o $@ https://thevisible.net/u/davidbau/home/$(patsubst src/%,%,$@)

output/%: src/%
	cp -r -f -v $< $@
