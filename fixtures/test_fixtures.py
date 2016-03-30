import smtplib

import pytest
import mock


@pytest.fixture
def mocked_foo  ():
     """ Mocked smtp connection
     """
     return mock.Mock(spec_set=smtplib.SMTP)


def test_smtp(mocked_smtp):
    assert True


