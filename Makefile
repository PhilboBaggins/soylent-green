
ALL := soylent-green.dxf soylent-green.svg

.PHONY: all clean

all: $(ALL)

soylent-green.dxf: soylent-green-dxf.py
	./soylent-green-dxf.py

soylent-green.svg: soylent-green-svg.py
	./soylent-green-svg.py

clean:
	rm -f $(ALL)
