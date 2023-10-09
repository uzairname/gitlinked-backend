from content_recommender import RecommendableItem




class User(RecommendableItem):
    def __init__(self, user_data: object):
        self.id = user_data["id"]
        self.description = user_data.get("description") or ""
        self.interest = user_data.get("interest") or ""
        self.skills = user_data.get("skills") or ""
        self.availability = user_data.get("availability") or ""

        text = " ".join([self.description, self.interest, self.skills])

        super().__init__(self.id, text, "user")


    def __repr__(self):
        return f"User {self.id} with description \"{self.description}\""



class Repository(RecommendableItem):
    def __init__(self, repo_data: object):
        self.id = repo_data["id"]
        self.description = repo_data.get("description") or ""
        self.languages = repo_data.get("languages") or ""
        
        text = " ".join([self.description, self.languages])

        super().__init__(self.id, text, "repository")


    def __repr__(self):
        return f"Repository {self.id} with description \"{self.description}\""

