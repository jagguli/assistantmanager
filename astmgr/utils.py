import subprocess

from box import Box
from jira import JIRA
from gitlab import Gitlab


DEFAULT_SETTINGS_YML = "./astmgr.yaml"


def passstore(path):
    return subprocess.check_output(["pass", path]).strip().decode("utf8")


def pass_get(path):
    return passstore(path.split("pass:/")[-1])


def get_jira():
    config = Box.from_yaml(filename=DEFAULT_SETTINGS_YML)
    return JIRA(
        options=dict(server=config.jira.api.server, verify=True),
        basic_auth=(
            pass_get(config.jira.api.username),
            pass_get(config.jira.api.password),
        ),
    )


def get_config():
    return Box.from_yaml(filename=DEFAULT_SETTINGS_YML)


def get_gitlab():
    return Gitlab(
        private_token=pass_get(get_config().gitlab.api.personal_access_token)
    )
