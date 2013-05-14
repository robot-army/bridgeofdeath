.PHONY: doc

test: $(patsubst %/__init__.py,cover/%.lint.html,$(wildcard */__init__.py)) cover/index.html

cover/%.lint.html: %/__init__.py %/__init__.py
	-pylint-python2.7 --rcfile=.pylintrc $*/*.py > $@

cover/index.html: */*.py
	nosetests-2.7 --exe --with-coverage --cover-html --detailed-errors --with-doctest --doctest-tests --cover-package=pyfare,models

doc:
	make -C doc html
