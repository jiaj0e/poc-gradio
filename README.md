# P-AI Project

A Python project template with FastAPI integration and modern development tools.

## Requirements

- Python 3.12 or higher
- pip or uv package manager
- git (for version control and pre-commit hooks)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd p-ai
```

2. Create and activate a virtual environment:  
(You can try running `dev.sh` script to skip the following steps)  
Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
```bash
uv venv <env_name>
source <env_name>/bin/activate
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:

Using uv (recommended):
```bash
# Install uv first if you haven't
pip install uv
# Install project dependencies
uv pip install -e ".[dev]"
```

Using pip:
```bash
pip install -e ".[dev]"
```

4. Set up pre-commit hooks:
```bash
pre-commit install
```

## Development

- Run the development server:
```bash
python main.py
```

- Run tests:
```bash
pytest
```

- Format and lint code:
```bash
ruff check .
ruff format .
```

## Project Structure

- `main.py`: Main application entry point
- `agent.py`: Call to gemini model
- `pyproject.toml`: Project configuration and dependencies
- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `dev.sh`: Development setup script

## Dependencies

- FastAPI: Web framework
- Uvicorn: ASGI server
- Pydantic: Data validation
- Ruff: Linting and formatting
- Pytest: Testing
- Pre-commit: Git hooks
