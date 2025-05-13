#!/bin/bash

# You can also use the command `pip install -e .` to install the package in editable mode.
# [dev, test] to install all dependencies for development and testing.

# Exit on any error
set -e

# Check if uv is already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
else
    echo "uv is already installed"
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
else
    echo "Virtual environment already exists"
fi

# Install dependencies (without activating the environment, uv handles this)
echo "Installing project dependencies..."
uv pip install -e ".[dev]"

# Optional: Setup shell completion for your specific shell
if [ -n "$ZSH_VERSION" ]; then
    # Only add completion if not already present
    if ! grep -q "uv generate-shell-completion zsh" ~/.zshrc; then
        echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
        echo "Added zsh completion for uv"
    fi
fi

echo "============================================"
echo "Setup complete! To activate the environment:"
echo "source .venv/bin/activate"
echo "============================================"
