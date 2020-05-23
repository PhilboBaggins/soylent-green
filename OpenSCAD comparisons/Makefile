NAME := SoylentGreen

SOURCES := \
	${NAME}1.scad \
	${NAME}2.scad \
	${NAME}3.scad \

ALL_OUTPUTS := \
	${NAME}1.dxf \
	${NAME}1.png \
	${NAME}1.svg \
	${NAME}2.dxf \
	${NAME}2.png \
	${NAME}2.svg \
	${NAME}3.dxf \
	${NAME}3.png \
	${NAME}3.svg \

.PHONY: all clean

all: ${ALL_OUTPUTS}

%.dxf: %.scad
	openscad -o $@ $<

%.png: %.scad
	openscad -o $@ $<

%.svg: %.scad
	openscad -o $@ $<

clean:
	rm -f ${ALL}
