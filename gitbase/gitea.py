import gitea

class gitea:
    def __init__(self, token, url):
        self.gitea = gitea.Gitea(token, url)
