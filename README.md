# Research Assistant

A powerful research assistant that combines Wikipedia, Reddit, and Semantic Scholar using LangGraph and Chainlit.

## Prerequisites

- Python 3.9 or higher
- `uv` package manager (install with `curl -LsSf https://astral.sh/uv/install.sh | sh`)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd research-assistant
```

2. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
# Install all dependencies (including dev dependencies)
uv sync --all

# Or, install only production dependencies
uv sync
```

4. Configure your environment:
```bash
# Copy the environment template
cp .env.template .env

# Edit .env with your API keys
OPENAI_API_KEY=your_openai_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
```

## Development

The project uses modern Python development tools:
- `ruff` for linting
- `black` for code formatting
- `mypy` for type checking

To run the development tools:
```bash
# Format code
black .

# Lint code
ruff check .

# Type check
mypy .
```

## Running the Application

1. Activate the virtual environment (if not already activated):
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

2. Start the Chainlit app:
```bash
chainlit run app.py
```

The application will be available at `http://localhost:8000`

## Project Structure

- `app.py`: Main application with LangGraph implementation
- `tools.py`: Tool implementations (Wikipedia, Reddit, Semantic Scholar)
- `chainlit.md`: Chainlit welcome message
- `pyproject.toml`: Project metadata and dependency specifications
- `.env.template`: Template for environment variables 