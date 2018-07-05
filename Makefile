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
	pipenv run black . -S -v --py36 --exclude .venv -l 99 
	pipenv run flake8 . 
test:
	pipenv run pytest