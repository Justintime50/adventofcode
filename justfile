VIRTUAL_ENV := ".venv"
VIRTUAL_BIN := VIRTUAL_ENV / "bin"
PROJECT_NAME := "adventofcode"
TEST_DIR := "test"

# Test the project and generate an HTML coverage report
coverage:
    {{VIRTUAL_BIN}}/pytest --durations=0 --cov={{PROJECT_NAME}} --cov-branch --cov-report=html --cov-report=lcov --cov-report=term-missing --cov-fail-under=70

# Cleans the project
clean:
    rm -rf {{VIRTUAL_ENV}} dist *.egg-info .coverage htmlcov .*cache
    find . -name '*.pyc' -delete

# Lints the project
lint:
    {{VIRTUAL_BIN}}/ruff check {{PROJECT_NAME}}/ {{TEST_DIR}}/
    {{VIRTUAL_BIN}}/ruff format --check {{PROJECT_NAME}}/ {{TEST_DIR}}/

# Fixes lint issues
lint-fix:
    {{VIRTUAL_BIN}}/ruff check --fix {{PROJECT_NAME}}/ {{TEST_DIR}}/
    {{VIRTUAL_BIN}}/ruff format {{PROJECT_NAME}}/ {{TEST_DIR}}/

# Install the project locally
install:
    uv venv
    uv pip install -e '.[dev]'

# Test the project
test:
    {{VIRTUAL_BIN}}/pytest --durations=0
