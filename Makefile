.PHONY: help setup install clean dist publish publish-test

help:
	@echo "Targets:"
	@echo "  setup   - create venv and install deps"
	@echo "  install - install deps into current env"
	@echo "  clean   - remove venv and caches"
	@echo "  dist    - build sdist and wheel into dist/"
	@echo "  publish - upload to PyPI (twine)"
	@echo "  publish-test - upload to TestPyPI"

setup:
	@bash scripts/setup_virtualenv.sh

install:
	python -m pip install -r requirements.txt

clean:
	rm -rf venv __pycache__ .mypy_cache .pytest_cache

dist:
	python -m pip install --upgrade build
	python -m build

publish:
	python -m pip install --upgrade twine
	twine upload dist/*

publish-test:
	python -m pip install --upgrade twine
	twine upload --repository testpypi dist/*
