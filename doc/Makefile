clean:
	rm -rf build

html:
	sphinx-build -b html . build/html

readme:
	sphinx-build -b rst . build/rst
	sed 's!\[image\]!.. image:: https://bitbucket.org/cbillington/bprofile/raw/default/doc/example.png!g' build/rst/index.rst > 1.tmp
	sed 's/Note:/Note:\n  /g' 1.tmp > 2.tmp
	sed 's/Warning:/Warning:\n  /g' 2.tmp > ../README.rst
	rm *.tmp
