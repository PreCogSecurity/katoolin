# Contributing to Katoolin

We welcome contributions to improve Katoolin's reliability, security, and maintainability.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/PreCogSecurity/katoolin.git
   cd katoolin
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Run the test suite:
   ```bash
   pytest -v
   ```

4. Run linter checks:
   ```bash
   flake8 katoolin tests
   ```

## Pull Request Guidelines
- Include unit tests for any new functionality or bug fixes.
- Ensure all tests pass (`pytest -v`) before submitting a pull request.
- Keep commits focused and descriptive.
