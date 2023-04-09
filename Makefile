# Current version
VERSION := $(shell poetry version -s)


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
