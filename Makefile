COPY_FILES = $(patsubst src/%,output/%,$(wildcard src/*) $(wildcard src/*/*))

all: download $(COPY_FILES) \
	output/understanding-video-compact.mp4

download: \
	src/understanding-video-compact.mp4

src/understanding-video-compact.mp4:
	curl -k -o $@ https://thevisible.net/u/davidbau/home/$(patsubst src/%,%,$@)

output/people:
	mkdir -p output/people

output/%: src/%
	echo $@
	cp -r -f -v $< $@

deploy:
	cp -r -v src/* output
