MODULE=src

test:
	python3 -m pytest

docs: FORCE
	rm -rf docs/
	sphinx-apidoc -o .sphinx/ ${MODULE}/
	sphinx-build -b html .sphinx/ docs/

clean: FORCE
	find ${MODULE}/ -type d -name __pycache__ -exec rm -rf {} +
	find tests/ -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache/

FORCE:
