
from openai import OpenAI
import os
from tools import get_career_roadmap, GET_CAREER_ROADMAP_TOOL_SCHEMA

class OpenAIChatCompletionsModel:
    """Model class for OpenAI Chat Completions"""
    
    def __init__(self, model_name: str = "gpt-4o"):
        self.model_name = model_name
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def create_completion(self, messages: list, tools: list = None):
        """Create a chat completion"""
        return self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            tools=tools,
            tool_choice="auto" if tools else None
        )

class Agent:
    """Base Agent class using OpenAI Chat Completions"""
    
    def __init__(self, name: str, model: str = "gpt-4o", instructions: str = "", tools: list = None, **kwargs):
        self.name = name
        self.model = model
        self.instructions = instructions
        self.tools = tools or []
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    async def run(self, message: str) -> str:
        """Run the agent with a given message"""
        try:
            # Prepare messages
            messages = [
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": message}
            ]
            
            # Prepare tools if available
            tools = None
            if self.tools:
                tools = [GET_CAREER_ROADMAP_TOOL_SCHEMA]
            
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto" if tools else None
            )
            
            # Handle tool calls if any
            if response.choices[0].message.tool_calls:
                tool_call = response.choices[0].message.tool_calls[0]
                if tool_call.function.name == "get_career_roadmap":
                    import json
                    args = json.loads(tool_call.function.arguments)
                    tool_result = get_career_roadmap(career_field=args.get("career_field"))
                    
                    # Make another call with tool result
                    messages.append(response.choices[0].message)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result
                    })
                    
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=messages
                    )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error running {self.name}: {str(e)}"

class Runner:
    """Base Runner class for orchestrating multiple agents"""
    
    def __init__(self, name: str, description: str = "", **kwargs):
        self.name = name
        self.description = description
    
    async def run_workflow(self, user_input: str):
        """Base workflow method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement run_workflow")

class CareerAgent(Agent):
    """Agent that suggests career fields based on user interests"""
    
    def __init__(self, **kwargs):
        super().__init__(
            name="CareerAgent",
            model="gpt-4o",
            instructions=(
                "You are an expert career counselor. Your job is to understand the user's interests "
                "(e.g., 'I like solving puzzles and math'). Based on their interests, you must suggest "
                "ONE suitable career field from the following options: 'Data Science', 'Software Development', "
                "or 'Cybersecurity'. Respond with a welcoming tone, suggest the career, and give a brief reason."
            ),
            **kwargs
        )

class SkillAgent(Agent):
    """Agent that generates skill-building roadmaps using tools"""
    
    def __init__(self, **kwargs):
        super().__init__(
            name="SkillAgent",
            model="gpt-4o",
            instructions=(
                "You are a skill development coach. The user has chosen a career field. "
                "Your only job is to use the 'get_career_roadmap' tool for that specific field. "
                "Do not add any extra text, just call the tool and present its output clearly."
            ),
            tools=[get_career_roadmap],
            **kwargs
        )

class JobAgent(Agent):
    """Agent that lists real-world job titles for career fields"""
    
    def __init__(self, **kwargs):
        super().__init__(
            name="JobAgent",
            model="gpt-4o",
            instructions=(
                "You are a recruitment expert. A user has been given a career path. "
                "Your task is to list 3-5 common, real-world job titles for that field. "
                "Keep your response concise and focused on the job titles."
            ),
            **kwargs
        )

class CareerMentorRunner(Runner):
    """Runner that orchestrates the career exploration workflow"""
    
    def __init__(self, **kwargs):
        super().__init__(
            name="CareerMentorRunner",
            description="Orchestrates career exploration using multiple specialized agents",
            **kwargs
        )
        
        # Initialize agents
        self.career_agent = CareerAgent()
        self.skill_agent = SkillAgent()
        self.job_agent = JobAgent()
        
        # Define the workflow
        self.workflow = [
            {
                "agent": self.career_agent,
                "description": "Analyze user interests and suggest career field"
            },
            {
                "agent": self.skill_agent,
                "description": "Generate skill-building roadmap for chosen career"
            },
            {
                "agent": self.job_agent,
                "description": "List real-world job titles for the career field"
            }
        ]
    
    async def run_workflow(self, user_input: str):
        """Run the complete career exploration workflow"""
        results = []
        current_context = user_input
        
        for step in self.workflow:
            agent = step["agent"]
            description = step["description"]
            
            # Run the agent with current context
            response = await agent.run(current_context)
            results.append({
                "agent": agent.name,
                "description": description,
                "response": response,
                "context": current_context
            })
            
            # Update context for next agent
            current_context = f"Career field: {self._extract_career_field(response)}\nPrevious response: {response}"
        
        return results
    
    def _extract_career_field(self, response: str) -> str:
        """Extract career field from agent response"""
        career_fields = ["Data Science", "Software Development", "Cybersecurity"]
        for field in career_fields:
            if field.lower() in response.lower():
                return field
        return "Software Development"  # Default fallback
