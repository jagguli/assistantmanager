from __future__ import absolute_import
from box import Box
from unittest import TestCase
from jira import JIRA
from astmgr.magics import JiraMagics
from mock import Mock
import pytest
from astmgr.utils import get_jira, get_config


@pytest.fixture(scope="function", autouse=True)  # Automatically use in tests.
def jira():
    return get_jira()


def test_search(jira):
    magics = JiraMagics(None, jira, get_config())
    magics.search("sprint = 44")


def test_current_sprint(jira):
    magics = JiraMagics(None, jira, get_config())
    magics.current_sprint()


def test_show(jira):
    magics = JiraMagics(None, jira, get_config())
    magics.show("POINTZI-3364")


def test_mysprint(jira):
    magics = JiraMagics(None, jira, get_config())
    magics.mysprint("--all")


def test_releases(jira):
    magics = JiraMagics(None, jira, get_config())
    magics.releases("POINTZI")
    magics.release_issues("3.11.0")


def test_run_regression(jira):
    magics = JiraMagics(None, jira, get_config())
    magics.run_regression("3.11.0")
