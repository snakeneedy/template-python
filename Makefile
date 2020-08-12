MODULE=src

test:
	python3 -m pytest

clean: FORCE
	find ${MODULE}/ -type d -name __pycache__ -exec rm -rf {} +
	find tests/ -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache/

FORCE:
