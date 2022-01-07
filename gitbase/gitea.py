import gitea

class gitea:
    def __init__(self, token, url):
        self.gitea = gitea.Gitea(token, url)
        self.user = self.gitea.get_user()

    @property
    def server_version(self):
        return self.gitea.get_version()

    def create_user(self, name, email, password):
        return self.gitea.create_user(name, email, password)

    def get_user(self, name):
        return gitea.User.request(self.gitea, name)

    def get_org(self, name):
        # org.description = 'new descrption'
        # org.location = 'new location'
        # org.commit()
        # teams = org.get_teams()
        # team_repos = team.get_repos()
        # repo_name = repo.name
        return gitea.Organization.request(self.gitea, name)
