import os

from github import Github

from core.config import config


class GitHubClient:

    def __init__(self):

        token = os.getenv("GITHUB_TOKEN")

        if not token:
            raise RuntimeError("GITHUB_TOKEN secret not found.")

        self.github = Github(token)

        self.branch = config.get("github", "branch")

    def repository(self):

        repo_name = os.getenv("GITHUB_REPOSITORY")

        if not repo_name:
            raise RuntimeError("GITHUB_REPOSITORY not found.")

        return self.github.get_repo(repo_name)


github_client = GitHubClient()
