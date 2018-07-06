# free_fair

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc618984eca945c3ad5bdc1efcaaed9f)](https://app.codacy.com/app/victorpb/free_fair?utm_source=github.com&utm_medium=referral&utm_content=victorpb/free_fair&utm_campaign=badger) [![Build Status](https://travis-ci.org/victorpb/free_fair.svg?branch=master)](https://travis-ci.org/victorpb/free_fair)[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/1e3a5c1edbfc49c38ba884bff0a91260)](https://www.codacy.com/app/victorpb/free_fair?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=victorpb/free_fair&amp;utm_campaign=Badge_Coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Requirements
* Python 3.6
* [pipenv](https://docs.pipenv.org/)

## Environment
* `export PIPENV_VENV_IN_PROJECT=1`
* `pipenv --python 3.6`
* `pipenv shell`
* `make install-requirements-dev`
* `python manage.py migrate`

## Execute project

* Pre populate database `python manage.py loaddata dump_free_fair.json` with data from the city hall

* Run server `python manage.py runserver`

* Access [http://localhost:8000/v1](http://localhost:8000/v1) to list urls api

## Docs api

Access [http://localhost:8000/docs/](http://localhost:8000/docs/) to list documentation api

## Import CSV to database
* run `python manage.py shell`
* `from apps.core.scripts.import_csv_to_database import insert_csv_to_databse`
* `insert_csv_to_databse('path_file')`

## Execute test
Execute tests and generate docs coverage in folder htmlcov
* `make test `

Acesse folder htmlcov to show coverage docs

## Check pep8 formatter test
* `make pep8 `

## Formatter formatter code
* `make formatter `
