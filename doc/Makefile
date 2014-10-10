clean:
	rm -rf build

html:
	sphinx-build -b html . build/html

readme:
	sphinx-build -b rst . build/rst
	python fixreadme.py
