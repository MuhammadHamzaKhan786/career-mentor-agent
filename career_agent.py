# agents/career_agent.py

class CareerAgent:
    def suggest_fields(self):
        return (
            "❓ To get started, please type one of the suggested career fields below:\n"
            "- Software Development\n"
            "- Data Science\n"
            "- Information Security\n"
            "- Health Services Management\n"
            "- Digital Marketing\n"
            "- UI/UX Design\n"
            "- Video Editing\n\n"
            "👉 Just reply with a field name (e.g. 'data science') to begin!"
        )

    def valid_fields(self):
        return [
            "software development",
            "data science",
            "information security",
            "nurse practitioner",
            "health services management",
            "digital marketing",
            "ui/ux design",
            "video editing"
        ]
