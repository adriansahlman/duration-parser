.PHONY: help
help:  ## print recipes and comments for recipes starting with ##
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'


.PHONY: review
review : lint test  ## Run both linting and tests


.PHONY: lint
lint : lint-mypy lint-style  ## Run linting


.PHONY: lint-style
lint-style :  ## Run flake8 linter
	@echo 'Checking codestyle...'
	@PYTHONPATH="$(shell pwd):${PYTHONPATH}" flake8 .
	@echo 'No issues'


.PHONY: lint-mypy
lint-mypy :  ## Run static type checker (mypy)
	@echo 'Running static type checker...'
	@PYTHONPATH="$(shell pwd):${PYTHONPATH}" mypy .


TEST = tests/

.PHONY: test
test :  ## run all tests (or those specified by arg `TEST`)
	PYTHONPATH=$(shell pwd) pytest -v -x $(TEST)
