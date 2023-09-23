help:
    @fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install requirements
    pip install -r requirements.dev.txt

clean:  ## Uninstall dev requirements    pip freeze | xargs pip uninstall -y

lock compile: ## Compile all requirements files
    pip-compile --no-emit-index-url --no-header --verbose requirements.in    pip-compile --no-emit-index-url --no-header --verbose requirements.dev.in

upgrade: ## Upgrade requirements files
    pip-compile --no-emit-index-url --no-header --verbose --upgrade requirements.in    pip-compile --no-emit-index-url --no-header --verbose --upgrade requirements.dev.in

fmt format: ## Run code formatters
    isort core tests    black core tests

lint: ## Run code linters
    isort --check core tests    black --check core tests
    flake8 core tests    mypy core tests
    yamllint --strict .

test: ## Run unit tests with coverage    python -m pytest tests/unit --lf --durations=5

test-integration: ## Run integration tests
    python -m pytest tests/integration

run: ## Run development server
    python -m core.runner dev

up: ## Create and start containers    @docker-compose up -d --build --remove-orphans

down: ## Stop and remove containers, networks, images, and volumes
    @docker-compose down

ps: ## List containers    @docker-compose ps

logs: ## View output from containers
    @docker-compose logs -f