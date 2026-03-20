# tests/test_member_manager.py

import pytest

def test_get_nonexist_member(empty_manager):
    with pytest.raises(KeyError):
        empty_manager.get_member("user")