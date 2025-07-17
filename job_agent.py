class JobAgent:
    def get_roles(self, field: str) -> str:
        jobs = {
            "data science": "- Data Analyst\n- Machine Learning Engineer\n- Research Scientist",
            "information security": "- Security Analyst\n- Penetration Tester\n- SOC Engineer",
            "nurse practitioner": "- Family Nurse Practitioner\n- Acute Care Nurse Practitioner\n- Pediatric Nurse Practitioner",
            "health services management": "- Healthcare Administrator\n- Medical Office Manager\n- Health Information Manager",
            "software development": "- Frontend Developer\n- Backend Developer\n- Full Stack Developer",
            "digital marketing": "- SEO Specialist\n- Social Media Manager\n- PPC Campaign Manager",
            "ui/ux design": "- UI Designer\n- UX Researcher\n- Product Designer",
            "video editing": "- Video Editor\n- Motion Graphics Designer\n- YouTube Content Creator"
        }
        return jobs.get(field.lower(), "No roles found.")
