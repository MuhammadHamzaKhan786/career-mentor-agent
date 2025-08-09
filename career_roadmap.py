def get_career_roadmap(career_field: str) -> str:
    """Provides a skill-building roadmap for a given career field."""
    print(f"Tool 'get_career_roadmap' called with career: {career_field}")
    
    roadmaps = {
        "Data Science": "**Phase 1: Foundations**\n- Learn Python (Pandas, NumPy)\n- Master Statistics & SQL.\n**Phase 2: Core ML**\n- Learn Supervised & Unsupervised Learning.\n**Phase 3: Specialization**\n- Learn Deep Learning (TensorFlow/PyTorch).",
        "Software Development": "**Phase 1: Fundamentals**\n- Learn a language (Python/JavaScript).\n- Master Data Structures & Algorithms.\n- Learn Git.\n**Phase 2: Stacks**\n- Learn Frontend (React) & Backend (Django/Node.js).\n**Phase 3: Deployment**\n- Learn databases & cloud (AWS/Azure).",
        "Cybersecurity": "**Phase 1: IT Basics**\n- Earn CompTIA A+ & Network+.\n- Learn Linux.\n**Phase 2: Security Foundations**\n- Study for CompTIA Security+.\n- Learn OWASP Top 10.\n**Phase 3: Specialization**\n- Choose Penetration Testing or Security Analysis."
    }
    
    return roadmaps.get(career_field, f"Sorry, a roadmap for '{career_field}' is not available.")

# This is the schema that describes the tool for the OpenAI Assistant
GET_CAREER_ROADMAP_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_career_roadmap",
        "description": "Provides a detailed skill-building roadmap for a given career field. Use this when a user has chosen a specific career and needs a learning plan.",
        "parameters": {
            "type": "object",
            "properties": {
                "career_field": {
                    "type": "string",
                    "description": "The career field chosen by the user, e.g., 'Data Science', 'Software Development'."
                }
            },
            "required": ["career_field"]
        }
    }
}
