.PHONY: run

run:
	@if [ "$(word 2,$(MAKECMDGOALS))" = "all" ]; then \
		for d in day_*; do \
			$(call run_day,$$d); \
		done \
	else \
		day_num=$(word 2,$(MAKECMDGOALS)); \
		if [ -n "$$day_num" ]; then \
			day_dir=day_$$(printf "%02d" $$day_num 2>/dev/null || echo "$$day_num"); \
			$(call run_day,$$day_dir); \
		fi \
	fi

define run_day
	if [ -d "$(1)" ]; then \
		printf "\033[1;34m=== Running $(1) ===\033[0m\n"; \
		python3 -c "import time; start=time.time(); __import__('os').system('cd \"$(1)\" && python3 main.py'); end=time.time(); print(f'\033[1;32mCompleted in {(end-start)*1000:.0f}ms\033[0m\n')"; \
	else \
		echo "Directory $(1) not found"; \
	fi
endef

%:
	@: