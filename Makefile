# Ravino Coin/Blockchain Makefile
#
# Docker
DC    = docker-compose
BUILD = $(DC) build
DOWN  = $(DC) down
UP    = $(DC) up

test:
	@make destroy
	$(DC) up -d --build --force-recreate --remove-orphans
	$(DC) exec blockchain python3 ravino/coin/ravino.py --developer Rye --devops Tiffany
	@make destroy

up:
	$(BUILD)
	$(DC) up
	@exit
	$(DC) down

.PHONY: build
build:
	$(BUILD) --no-cache --force-rm

destroy:
	$(DOWN) --rmi all --volumes --remove-orphans

run:
	$(DC) exec blockchain python3 ravino/coin/ravino.py --developer Rye --devops Tiffany