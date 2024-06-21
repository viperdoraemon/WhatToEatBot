# Setting up a Python project for GitHub Codespaces

## 1. Add a dev container configuration

The default development container, or "dev container," for GitHub Codespaces comes with the latest Python version, package managers (pip, Miniconda), and other common tools preinstalled. However, we recommend that you configure your own dev container to include all of the tools and scripts your project needs. This will ensure a fully reproducible environment for all GitHub Codespaces users in your repository.

To set up your repository to use a custom dev container, you will need to create one or more devcontainer.json files. You can either add these from a predefined configuration template, in Visual Studio Code, or you can write your own. For more information on dev container configurations, see "Introduction to dev containers."

Access the Visual Studio Code Command Palette (Shift+Command+P / Ctrl+Shift+P), then start typing "add dev". Click Codespaces: Add Dev Container Configuration Files.

## 2. 