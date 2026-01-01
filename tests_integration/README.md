# Integration Tests

These tests verify that the `simple-adder` package works correctly after installation.

## Purpose

Unlike unit tests that test the source code directly, integration tests:
- Test the installed package (via `pip install`)
- Verify the package can be imported correctly
- Ensure metadata is correct
- Test real-world usage scenarios

## Running Integration Tests

### 1. Install the package locally
```bash
pip install -e .
```

### 2. Run integration tests
```bash
pytest tests_integration/ -v
```

### 3. Test with installed package from PyPI
```bash
# Create a fresh virtual environment
python -m venv test_env
source test_env/bin/activate

# Install from PyPI
pip install simple-adder

# Run integration tests
pip install pytest
pytest tests_integration/
```

## Test Coverage

- ✅ Package installation verification
- ✅ Version checking
- ✅ Function availability and exports
- ✅ Functionality testing
- ✅ Subprocess import testing
- ✅ Package metadata validation
- ✅ Real-world usage scenarios
