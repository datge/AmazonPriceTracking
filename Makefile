clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr
	
typehint:
	mypy --ignore-missing-imports src/

test:
	pytest tests/

lint:
	pylint src/

checklist: lint typehint test

sort: isort -rc src/

black:
	black -l 79 *.py

setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

.PHONY: clean typehint test lint checklist sort black setup
