
install:
	python setup.py install --root=$(DESTDIR)/

clean:
	rm -Rf build dist __pycache__

.PHONY: clean install
