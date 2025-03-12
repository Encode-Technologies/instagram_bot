.PHONY: install
install:
	uv sync

.PHONY: run
run:
	uv run python src/main.py