run:
	uv run bible-cli query "$(ARGS)"

tests:
	pytest -s ./tests/** --cov-report=term-missing --cov-report=html -v

check:
	uv run ruff check --fix

format:
	uv run ruff format

install:
	uv pip install -e .

update:
	uv sync

make release:
	cz bump
	git push --follow-tags
