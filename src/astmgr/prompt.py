from IPython.terminal.prompts import Prompts, Token


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
