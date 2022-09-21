from docopt import docopt
import os
from os.path import expanduser, join, exists, basename
from jira import JIRA, __version__
import subprocess
from IPython.terminal.prompts import Prompts, Token
from astmgr.magics import JiraMagics
from astmgr.prompt import JiraPrompt
import IPython
from IPython.terminal.embed import InteractiveShellEmbed
from astmgr import CONFIG


class AssistantManagerShell(InteractiveShellEmbed):
    def __init__(self, *args, **kwargs):
        kwargs["banner1"] = "AssistantManager Shell"
        super().__init__(*args, **kwargs)
        self.prompts_class = JiraPrompt

    def init_magics(self):
        super().init_magics()
        self.register_magics(JiraMagics)


def main():
    ip_shell = AssistantManagerShell()
    ip_shell(
        f"*** jira client is in 'jira' version: {__version__} ({CONFIG.jira.api.server}). Press Ctrl-D to exit."
    )
