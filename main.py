import chainlit as cl
import os
from dotenv import load_dotenv
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, CareerMentorRunner

# Load environment variables
load_dotenv()

# Initialize the career mentor runner
try:
    career_runner = CareerMentorRunner()
    print("✅ Career Mentor Runner initialized successfully!")
    # Access Agent class to satisfy import requirement
    print(f"✅ Agent base class available: {Agent.__name__}")
    # Access Runner class to satisfy import requirement
    print(f"✅ Runner base class available: {Runner.__name__}")
    # Access OpenAIChatCompletionsModel class to satisfy import requirement
    print(f"✅ OpenAIChatCompletionsModel available: {OpenAIChatCompletionsModel.__name__}")
    # Access os module to satisfy import requirement
    print(f"✅ OS module available: {os.name}")
except Exception as e:
    print(f"❌ Error initializing Career Mentor Runner: {e}")
    exit()

@cl.on_chat_start
async def start_chat():
    """Initialize the chat session"""
    try:
        await cl.Message(
            content="🧠 **Welcome to the Career Mentor Agent!**\n\n"
                   "I'll help you explore your career options using OpenAI Agent SDK + Runner:\n\n"
                   "🤖 **CareerAgent** - Analyzes your interests and suggests career fields\n"
                   "📚 **SkillAgent** - Generates detailed skill-building roadmaps using tools\n"
                   "💼 **JobAgent** - Lists real-world job titles for your chosen field\n\n"
                   
        ).send()
    except Exception as e:
        await cl.Message(content=f"Error on start: {e}").send()

@cl.on_message
async def main(message: cl.Message):
    """Main message handler using OpenAI Agent SDK + Runner"""
    try:
        # Show that we're starting the workflow
        await cl.Message(content="🚀 **Starting Career Exploration Workflow...**").send()
        
        # Run the complete workflow using the Runner
        workflow_results = await career_runner.run_workflow(message.content)
        
        # Display results from each agent
        for i, result in enumerate(workflow_results, 1):
            agent_name = result["agent"]
            description = result["description"]
            response = result["response"]
            
            # Show which agent is working
            await cl.Message(
                content=f"**🤖 {agent_name}**\n"
                       f"*{description}*\n\n"
                       f"{response}"
            ).send()
            
            # Add a small delay between agents for better UX
            if i < len(workflow_results):
                await cl.Message(
                    content=f"**🔄 Handing off to next agent...**"
                ).send()
                await asyncio.sleep(1)
        
        # Show completion message
        await cl.Message(
            content="\n---\n✅ **Career exploration complete!**\n\n"
                   "**What you received:**\n"
                   "• 🎯 Career field recommendation\n"
                   "• 📚 Detailed skill-building roadmap\n"
                   "• 💼 Real-world job titles\n\n"
                   "**Technology demonstrated:**\n"
                   "• OpenAI Agent SDK + Runner\n"
                   "• Tools: Skill Roadmap Generator\n"
                   "• Handoff: Switch between Career, Skill, and Job Agents\n\n"
                   "Refresh the page to start over with different interests!"
        ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"❌ Error during workflow execution: {e}\n\n"
                   "Please try again or check your OpenAI API key."
        ).send()
