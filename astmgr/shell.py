#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
astmgr.py

Usage: astmgr.py --config [options]

Options:
  -c --config=STRING        assistant manager configuration file [default: astmgr.yaml]


"""
from docopt import docopt
import os
from os.path import expanduser, join, exists, basename
from jira import JIRA, __version__
import subprocess
from IPython.terminal.prompts import Prompts, Token
from magics import JiraMagics
import IPython
from IPython.terminal.embed import InteractiveShellEmbed
from astmgr.utils import get_jira, get_config


class JiraPrompt(Prompts):
    jira_url = None

    def __init__(self, shell, jira_url):
        self.jira_url = jira_url
        shell.prompts = self
        super().__init__(shell)

    def in_prompt_tokens(self, cli=None):
        return [
            (Token, self.jira_url),
            (Token.Prompt, " >>> "),
        ]


def main():
    jira = get_jira()
    config = get_config()

    ip_shell = InteractiveShellEmbed(
        banner1="<Jira Shell " + __version__ + " (" + jira.server_url + ")>"
    )
    JiraPrompt(ip_shell, config.jira.api.server)
    JiraMagics(ip_shell, jira, config)

    ip_shell(
        "*** Jira shell active; client is in 'jira'. Press Ctrl-D to exit."
    )


if __name__ == "__main__":
    main()
