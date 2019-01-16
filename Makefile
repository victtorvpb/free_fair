install:
	$(info ************  Not command ************)
install-requirements:
	pipenv sync
install-requirements-dev:
	pipenv sync --dev
install-requirements-test:
	pipenv sync --dev
clean:
	pipenv --rm
pep8:
	pipenv run flake8 . 
test:
	pipenv run py.test --cov=apps --cov-config .coveragerc
	coverage html
formatter:
	pipenv run black . -S -v --py36 --exclude .venv -l 99 
	make pep8

coverage:
	coverage xml	 
	python-codacy-coverage -r coverage.xml