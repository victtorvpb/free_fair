install:
	$(info ************  Not command ************)
install-requirements:
	pipenv install

make:
	pipenv install
install-requirements-dev:
	pipenv install --dev
	pipenv run pip install black
clean:
	pipenv --rm
pep8:
	pipenv run flake8 . 
test:
	pipenv run py.test --cov=apps --cov-config .coveragerc
formatter:
	make flake8
	pipenv run black . -S -v --py36 --exclude .venv -l 99 
coverage:
	coverage xml
	python-codacy-coverage -r coverage.xml