import typing as t
from gitlinked_database import GitlinkedDatabase



class GitlinkedNetworkDatabase(GitlinkedDatabase):

    def __init__(self):
        super().__init__()
        self.all_users = []
        self.all_repositories = []
        self.all_tags = []


    def get_all_user_ids(self) -> t.List[str]:
        return [str(i["id"]) for i in self.get_all_users()]
    

    def get_all_repository_ids(self) -> t.List[str]:
        return [str(i["id"]) for i in self.get_all_repos()]
    

    def get_all_contributors(self) -> t.List[t.Dict]:
        return [i for i in self.client.table("contributors").select("*").execute().data]
    

    def get_all_tag_ids(self) -> t.List[str]:
        tags = []
        self.all_tags = tags
        return tags





