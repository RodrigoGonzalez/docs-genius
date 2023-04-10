# =============================================================================
# MAKEFILE FOR DOCS-GENIUS
# =============================================================================
#
# Partially inspired by https://github.com/johschmidt42/python-project-johannes
#
# To do stuff with make, you type `make` in a directory that has a file called
# "Makefile". You can also type `make -f <makefile>` to use a different filename.
#
# A Makefile is a collection of rules. Each rule is a recipe to do a specific
# thing, sort of like a grunt task or an npm package.json script.
#
# A rule looks like this:
#
# <target>: <prerequisites...>
# 	<commands>
#
# The "target" is required. The prerequisites are optional, and the commands
# are also optional, but you have to have one or the other.
#
# Type `make` to show the available targets and a description of each.
#

# =============================================================================
# GLOBAL VARIABLES
# =============================================================================

PROJECTNAME := $(shell basename "$(PWD)")
PYTHON_INTERPRETER := python3.10

.SILENT: ;               # no need for @

# =============================================================================
# ENVIRONMENT SETUP
# =============================================================================

##@ Environment

setup: poetry-install pre-commit-install  ## Setup Virtual Environment

    poetry-install:  ## Install dependencies using Poetry
		poetry env use $(PYTHON_INTERPRETER)
		poetry install

    pre-commit-install:  ## Install pre-commit hooks
		poetry run pre-commit install

update-deps: pip-upgrade poetry-update pre-commit-autoupdate  ## Update dependencies

    pip-upgrade:  ## Upgrade pip
		poetry run pip install --upgrade pip

    poetry-update:  ## Update Poetry dependencies
		poetry update
		poetry lock

    pre-commit-autoupdate:  ## Update pre-commit hooks
		poetry run pre-commit autoupdate -c .pre-commit-config.yaml

local: setup update-deps  ## Locally install the package
	docs-genius --help

add:  ## Adds packages with poetry. (e.g. To add requests and numpy run `make add PACKAGES="requests numpy"`)
	poetry add $(PACKAGES)

add-dev:  ## Adds development packages with poetry. (e.g. To add requests and numpy run `make add-dev PACKAGES="commitizen pre-commit"`)
	poetry add --group dev $(PACKAGES)

add-lint:  ## Adds lint packages with poetry. (e.g. To add black and flake8 run `make add-lint PACKAGES="black flake8"`)
	poetry add --group lint $(PACKAGES)


.PHONY: setup update-deps local add add-dev add-lint

# =============================================================================
# DEVELOPMENT
# =============================================================================

##@ Development

# Get the list of changed files
changed_files = $(shell git diff --name-only --diff-filter=d $$(git merge-base HEAD origin/main))

# Filter only Python files
changed_py_files = $(filter %.py, $(changed_files))

pre-commit:  ## Manually run all pre-commit hooks
	# not added to `pre-commit-tool` in order to prevent unwanted behavior when running in workflows
	git add -A
	poetry run pre-commit run -c .pre-commit-config.yaml
	#poetry run pre-commit run --all-files -c .pre-commit-config.yaml

pre-commit-tool:  ## Manually run a single pre-commit hook (e.g. `make pre-commit-tool TOOL=black ARGS="--check"`)
	poetry run pre-commit run $(TOOL) $(ARGS) -c .pre-commit-config.yaml
	#poetry run pre-commit run $(TOOL) --all-files -c .pre-commit-config.yaml

.PHONY: pre-commit pre-commit-tool

# =============================================================================
# FORMATTING
# =============================================================================

##@ Formatting

format: format-black format-isort format-autoflake format-pyupgrade  ## Run all formatters

format-black: ## Run black (code formatter)
	$(MAKE) pre-commit-tool TOOL=black

format-isort: ## Run isort (import formatter)
	$(MAKE) pre-commit-tool TOOL=isort

format-autoflake: ## Run autoflake (remove unused imports)
	$(MAKE) pre-commit-tool TOOL=autoflake

format-pyupgrade: ## Run pyupgrade (upgrade python syntax)
	$(MAKE) pre-commit-tool TOOL=pyupgrade

.PHONY: format format-black format-isort format-autoflake format-pyupgrade

# =============================================================================
# LINTING
# =============================================================================

##@ Linting

lint: lint-black lint-isort lint-flake8 lint-mypy ## Run all linters

.PHONY: lint lint-black lint-isort lint-flake8 lint-mypy

lint-black: ## Run black in linting mode
	$(MAKE) pre-commit-tool TOOL=black ARGS="--check"

lint-isort: ## Run isort in linting mode
	$(MAKE) pre-commit-tool TOOL=isort ARGS="--check"

lint-flake8: ## Run flake8 (linter)
	$(MAKE) pre-commit-tool TOOL=flake8

lint-mypy: ## Run mypy (static-type checker)
	$(MAKE) pre-commit-tool TOOL=mypy

lint-mypy-report: ## Run mypy & create report
	poetry run mypy --install-types --non-interactive --verbose --html-report ./.mypy_html_report src
	#$(MAKE) pre-commit-tool TOOL=mypy ARGS="--html-report ./mypy_html"

lint-mypy-changed:  ## Run mypy on changed Python files & create report
	$(if $(changed_py_files), poetry run mypy --install-types --non-interactive --verbose --html-report ./.mypy_html_report $(changed_py_files), echo "No changed Python files to lint.")

.PHONY: lint-mypy-report

# =============================================================================
# TESTING
# =============================================================================

##@ Testing

unit-tests: ## run unit-tests with pytest
	pytest --doctest-modules

unit-tests-cov: ## run unit-tests with pytest and show coverage (terminal + html)
	pytest --doctest-modules --cov=src --cov-report term-missing --cov-report=html

unit-tests-cov-fail: ## run unit tests with pytest and show coverage (terminal + html) & fail if coverage too low & create files for CI
	pytest --doctest-modules --cov=src --cov-report term-missing --cov-report=html --cov-fail-under=80 --junitxml=pytest.xml | tee pytest-coverage.txt

.PHONY: unit-tests unit-tests-cov unit-tests-cov-fail

# =============================================================================
# BUILD & RELEASE
# =============================================================================

##@ Build & Release

build:  ## Build the project
	poetry build


bump-major:  ## Bump major version
	poetry version major
	git add pyproject.toml
	cz commit --hook --message "bump: major version to $(shell poetry version -s)"
	git tag -a "v$(shell poetry version -s)" -m "v$(shell poetry version -s)"
	git push --tags


bump-minor:  ## Bump minor version
	poetry version minor
	git add pyproject.toml
	cz commit --hook --message "bump: minor version to $(shell poetry version -s)"
	git tag -a "v$(shell poetry version -s)" -m "v$(shell poetry version -s)"
	git push --tags


bump-patch:  ## Bump patch version
	poetry version patch
	git add pyproject.toml
	cz commit --hook --message "bump: patch version to $(shell poetry version -s)"
	git tag -a "v$(shell poetry version -s)" -m "v$(shell poetry version -s)"
	git push --tags


deploy:  ## Deploy to PyPI
	poetry publish --build

.PHONY: build bump-major bump-minor bump-patch deploy

# =============================================================================
# SELF DOCUMENTATION
# =============================================================================

.DEFAULT_GOAL := help
.PHONY: help
help:  ## Display this help
	echo
	echo " The following commands can be run for "$(PROJECTNAME)":"
	echo
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
