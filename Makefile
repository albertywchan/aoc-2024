.PHONY: run-all

run-all:
	@for d in day*; do \
		printf "\n\033[1;34m=== Running $$d ===\033[0m\n"; \
		python3 -c "import time; start=time.time(); __import__('os').system('cd \"$$d\" && python3 main.py'); end=time.time(); print(f'\033[1;32mCompleted in {(end-start)*1000:.0f}ms\033[0m\n')"; \
	done