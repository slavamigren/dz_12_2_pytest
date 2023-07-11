from utils.dicts import get_val
import pytest

@pytest.fixture
def get_dict():
    return {"vcs": "mercurial"}


def test_get_val(get_dict):
    assert get_val(get_dict, "vcs") == "mercurial"
    assert get_val(get_dict, "vcs", "git") == "mercurial"
    assert get_val({}, "vcs", "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"
