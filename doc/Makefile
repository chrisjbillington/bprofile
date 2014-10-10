clean:
	rm -rf build

html:
	sphinx-build -b html . build/html

readme:
	sphinx-build -b rst . build/rst
	sed 's!\[image\]!.. image:: https://bitbucket.org/cbillington/bprofile/raw/default/doc/example.png!g' build/rst/index.rst > ../README.rst
