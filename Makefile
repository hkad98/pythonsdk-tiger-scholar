.PHONY: dev
dev:
	python -c 'import sys;  exit(0 if sys.version_info[:2] >= (3, 8) else 1)'
	python -m venv .venv --upgrade-deps
	.venv/bin/pip3 install -r requirements.txt