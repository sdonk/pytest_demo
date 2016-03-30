from time import sleep

import pytest
import sys


@pytest.mark.skip(reason="Skip this test")
def test_skip():
    assert True


@pytest.mark.skipif(sys.version_info < (3,3),
                    reason="requires python3.3")
def test_skipif_python3():
    assert True


# custom markers

@pytest.mark.slow
def test_slow():
    sleep(5)
    assert True


@pytest.mark.whatever
def test_foo():
    assert True
