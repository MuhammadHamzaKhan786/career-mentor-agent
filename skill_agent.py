from tools.roadmap_tool import get_career_roadmap

class SkillAgent:
    def get_roadmap(self, field: str) -> str:
        return get_career_roadmap(field)
