TEST_PATH=./tests

init:
	pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

clean:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox --recursive ."

pep:
	pep8 .

build:
	python3 setup.py build

install:
	python3 setup.py install

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

cov: clean-pyc
	py.test --verbose --color=yes --cov=arxivbot --cov-config .coveragerc

reset: clean
	python3 setup.py build
	python3 setup.py install
