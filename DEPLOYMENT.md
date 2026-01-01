# Deployment Instructions

## Publishing to PyPI

### Prerequisites
1. Create accounts on:
   - TestPyPI: https://test.pypi.org/account/register/
   - PyPI: https://pypi.org/account/register/

2. Create API tokens:
   - TestPyPI: https://test.pypi.org/manage/account/token/
   - PyPI: https://pypi.org/manage/account/token/

### Upload to TestPyPI (for testing)
```bash
twine upload --repository testpypi dist/*
# Enter your TestPyPI API token when prompted
```

### Upload to PyPI (production)
```bash
twine upload dist/*
# Enter your PyPI API token when prompted
```

### Test Installation from TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ simple-adder
```

### Test Installation from PyPI
```bash
pip install simple-adder
```

## Current Status

✅ Package built successfully:
- `dist/simple_adder-0.1.0-py3-none-any.whl`
- `dist/simple_adder-0.1.0.tar.gz`

⏳ Waiting for PyPI credentials to upload

## Alternative: Using GitHub Actions for CI/CD

You can automate PyPI publishing using GitHub Actions. See `.github/workflows/publish.yml` for an example workflow.
