.PHONY: dev
dev:
	python3.10 -m venv .venv --upgrade-deps
	.venv/bin/pip3 install -r requirements.txt