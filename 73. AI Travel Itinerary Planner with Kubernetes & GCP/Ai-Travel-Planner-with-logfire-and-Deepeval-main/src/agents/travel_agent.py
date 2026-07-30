import logfire
import time
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware
from src.tools.tavily_tool import tavily_search_tool
from src.tools.serper_tool import google_serper_search_tool
from src.models.travel_models import TravelPlan
from src.utils.logger import get_logger

# Ensure Pydantic models are captured by Logfire for observability
logfire.instrument_pydantic()

logger = get_logger(__name__)

# Primary reasoning model (High-stability 70B for tool calling)
model = init_chat_model(
    model="groq:llama-3.3-70b-versatile",
    temperature=0.3,
    max_retries=3
)

tools = [tavily_search_tool, google_serper_search_tool]

# Custom Middleware for LangChain v1.x (Observability & Rate Limiting)
class TravelAgentMiddleware(AgentMiddleware):
    def before_agent(self, state, runtime):
        logger.info(f"🎬 Agent Turn Started (History: {len(state.get('messages', []))} msgs)")
        return None
    
    def after_model(self, state, runtime):
        # 🛡️ TPM PROTECTION: Pause slightly after every model reasoning step
        # This prevents the LLM from blasting multiple tool calls in 1 second
        logger.info("⏳ Catching breath (2s) for TPM refill...")
        time.sleep(2)
        return None
    
    def after_agent(self, state, runtime):
        logger.info("🏁 Agent Turn Completed. Cooling down (5s)...")
        time.sleep(5)
        return None

SYSTEM_PROMPT = """
You are an expert AI travel planner.

Rules:
1. Always give results as of the current date for accuracy.
2. Always use web search tools for latest info, events, and pricing.
3. Include food suggestions, local tips, and travel advice.
""".strip()

# Modern LangChain 1.x Agent with Built-in Loop (via LangGraph)
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    middleware=[TravelAgentMiddleware()]
)

# Model wrapper for structured output validation
structured_model = model.with_structured_output(TravelPlan)

logger.info("Modern LangChain v1.x Travel Agent with Middleware initialized.")