SOURCES := $(shell find src -name '*.dasm')

build/example.bin:

build/%.bin: build/preprocess/%.dasm
	dasm $< $@

build/preprocess/%.dasm: %.dasm $(SOURCES) tools/preprocess.py
	@mkdir -p $(dir $@)
	python3 tools/preprocess.py -Isrc $< > $@

docs: $(SOURCES:%=docs/%.md)
.PHONY: docs

docs/%.md: % tools/docfile.py
	@mkdir -p $(dir $@)
	python3 tools/docfile.py $< > $@

%/run: build/%.bin
	tc-dcpu $<

clean:
	rm -rf build docs/src
.PHONY: clean

.SECONDARY:
