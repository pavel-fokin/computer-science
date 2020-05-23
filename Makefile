.PHONY: all
all: help

.PHONY: help
help:
	@echo 'Makefile help:                      '
	@echo '                                    '
	@echo '   lint              Run linters    '
	@echo '   tests             Run unit tests '

.PHONY: tests
tests:
	@PYTHONPATH=. pytest tests -W ignore --cov

.PHONY: lint
lint:
	@flake8 cs tests
	@pylint --exit-zero --rcfile setup.cfg cs tests
