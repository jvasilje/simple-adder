"""
Integration tests for the installed simple_adder package.

These tests verify that the package works correctly after being
installed via pip install.

Run these tests after installing the package:
    pip install simple-adder
    pytest tests_integration/
"""

import subprocess
import sys


def test_package_is_installed():
    """Test that the package is installed and importable."""
    try:
        import simple_adder
        assert simple_adder is not None
    except ImportError:
        pytest.fail("simple_adder package is not installed")


def test_version_is_available():
    """Test that the package version is accessible."""
    import simple_adder
    assert hasattr(simple_adder, "__version__")
    assert simple_adder.__version__ == "0.1.0"


def test_add_function_is_exported():
    """Test that the add function is available at package level."""
    import simple_adder
    assert hasattr(simple_adder, "add")
    assert callable(simple_adder.add)


def test_add_function_works():
    """Test that the add function works correctly after installation."""
    from simple_adder import add

    # Test basic addition
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, -5) == 5
    assert add(2.5, 3.5) == 6.0


def test_package_can_be_imported_in_subprocess():
    """Test that the package can be imported in a subprocess."""
    code = "from simple_adder import add; print(add(10, 20))"
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "30"


def test_package_metadata():
    """Test that package metadata is correct."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "show", "simple-adder"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "simple-adder" in result.stdout.lower()
    assert "0.1.0" in result.stdout


def test_package_entry_point():
    """Test that the package can be used as expected."""
    # This tests the main use case from documentation
    code = """
from simple_adder import add
result = add(2, 3)
assert result == 5, f"Expected 5, got {result}"
print("SUCCESS")
"""
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "SUCCESS" in result.stdout
