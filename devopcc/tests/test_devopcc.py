"""
Unit and regression test for the devopcc package.
"""

# Import package, test suite, and other packages as needed
import devopcc
import pytest
import sys

def test_devopcc_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "devopcc" in sys.modules
