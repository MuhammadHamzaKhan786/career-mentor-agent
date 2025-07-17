import chainlit as cl
import os
from dotenv import load_dotenv
from difflib import get_close_matches
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

# 🔐 Load .env API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Agent instances
career_agent = CareerAgent()
skill_agent = SkillAgent()
job_agent = JobAgent()

# State tracker
state = {"stage": "start", "field": ""}

# Fuzzy match helper
def get_closest_field(user_input, valid_fields):
    matches = get_close_matches(user_input.lower(), valid_fields, n=1, cutoff=0.7)
    return matches[0] if matches else None


@cl.on_chat_start
async def start():
    state["stage"] = "career"
    await cl.Message(content="💼 Welcome to the Career Mentor Agent!\nType `explore careers` to begin your journey!").send()


@cl.on_message
async def main(message: cl.Message):
    msg = message.content.lower()

    if state["stage"] == "career":
        if "explore" in msg and "career" in msg:
            state["stage"] = "skill"
            await cl.Message(content=career_agent.suggest_fields()).send()
        else:
            await cl.Message(content="❓ Please type `explore careers` to begin.").send()

    elif state["stage"] == "skill":
        valid_fields = career_agent.valid_fields()
        matched_field = get_closest_field(msg, valid_fields)

        if matched_field:
            state["field"] = matched_field
            state["stage"] = "job"
            roadmap = skill_agent.get_roadmap(matched_field)
            await cl.Message(content=f"📚 Skill Roadmap for **{matched_field.title()}**:\n{roadmap}").send()
        else:
            await cl.Message(content="❓ Please choose a valid field (e.g. software development, data science, digital marketing, etc.).").send()

    elif state["stage"] == "job":
        field = state["field"]
        roles = job_agent.get_roles(field)
        await cl.Message(content=f"💼 Real-world roles in **{field.title()}** include:\n{roles}").send()
        await cl.Message(content="🎯 Type `explore careers` to explore more fields.").send()
        state["stage"] = "career"

    else:
        await cl.Message(content="✅ You're done! Type `explore careers` to restart.").send()
        state["stage"] = "career"
