.PHONY: tests

ifeq ($(debug),1)
    PYTHON_CMD := uv run python -m debugpy --listen 5678 --wait-for-client -m
else
    PYTHON_CMD := uv run python -m
endif

run:
	$(PYTHON_CMD) bible_telegram_bot.app

tests:
	$(PYTHON_CMD) pytest -s ./tests/** --cov-report=term-missing --cov-report=html -v

check:
	uv run ruff check --fix

format:
	uv run ruff format

install:
	uv pip install -e .

update:
	uv sync

release:
	cz bump
	git push --follow-tags

debug:
	uv run python -m debugpy --listen 5678 --wait-for-client -m bible_telegram_bot.app
