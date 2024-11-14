import os

class Config:
    def __init__(self):
        self.WS_GH_REPOS = os.getenv("WS_GH_REPOS")
        self.WS_GH_ACTIONS = os.getenv("WS_GH_ACTIONS")
        self.WS_AZ_REPOS = os.getenv("WS_AZ_REPOS")
        self.WS_AZ_ACTIONS = os.getenv("WS_AZ_ACTIONS")
        self.AVG_TIME_BETWEEN_EVENTS_MS = int(os.getenv("AVG_TIME_BETWEEN_EVENTS_MS"))
        self.STD_DV_TIME_BETWEEN_EVENTS_MS = int(os.getenv("STD_DV_TIME_BETWEEN_EVENTS_MS"))
        self.GITHUB_REPOS_ENABLED = os.getenv("GITHUB_REPOS_ENABLED").lower() == "true"
        self.GITHUB_ACTIONS_ENABLED = os.getenv("GITHUB_ACTIONS_ENABLED").lower() == "true"
        self.AZURE_REPOS_ENABLED = os.getenv("AZURE_REPOS_ENABLED").lower() == "true"
        self.AZURE_ACTIONS_ENABLED = os.getenv("AZURE_ACTIONS_ENABLED").lower() == "true"

    def __str__(self):
        return (
            f"Config("
            f"WS_GH_REPOS={self.WS_GH_REPOS}, "
            f"WS_GH_ACTIONS={self.WS_GH_ACTIONS}, "
            f"WS_AZ_REPOS={self.WS_AZ_REPOS}, "
            f"WS_AZ_ACTIONS={self.WS_AZ_ACTIONS}, "
            f"AVG_TIME_BETWEEN_EVENTS_MS={self.AVG_TIME_BETWEEN_EVENTS_MS}, "
            f"STD_DV_TIME_BETWEEN_EVENTS_MS={self.STD_DV_TIME_BETWEEN_EVENTS_MS}, "
            f"GITHUB_REPOS_ENABLED={self.GITHUB_REPOS_ENABLED}, "
            f"GITHUB_ACTIONS_ENABLED={self.GITHUB_ACTIONS_ENABLED}, "
            f"AZURE_REPOS_ENABLED={self.AZURE_REPOS_ENABLED}, "
            f"AZURE_ACTIONS_ENABLED={self.AZURE_ACTIONS_ENABLED})"
        )