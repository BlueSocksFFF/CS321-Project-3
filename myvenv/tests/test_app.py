from app import index
import pytest

def test_index():
    
    assert index() == "hello, World!"