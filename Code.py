#--Install ADK--
!pip install -U google-adk google-genai

#--IMPORTS--
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, google_search
from google.genai import types

print("✅ ADK components imported successfully.")

#--API Key--
import os
os.environ["GOOGLE_API_KEY"] = "Your API KEY"

#--Retry Config--

retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

#--SUB AGENTS--
claim_extractor = Agent(
    name="ClaimExtractor",
    instruction="Extract key factual claims from the input text and present them as a clean list of bullet points.",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    tools=[google_search],
    # ADDED: Output key for storing results in session state, mirroring ResearchAgent's structure.
    output_key="claim_extraction_results", 
)

print("✅ claim_extractor created with output_key.")

#Fact checker Agent

fact_checker = Agent(
    name="FactChecker",
    description="Fact-check claims",
    instruction="Fact-check the provided claims using reasoning and internet search.",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
    tools=[google_search],
    output_key="fact_check_report", # ADDED: Output key for session state
)
print("✅ fact_checker created with output_keys.")

# News Summary Agent: Fetch and summarize technology/startup news.

news_agent = Agent(
    name="NewsSummaryAgent",
    description="Fetch and summarize technology/startup news",
    instruction="Search and summarize technology & startup news for the given period.",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
    tools=[google_search],
    output_key="news_summary_results", # ADDED: Output key for session state
)

print("✅ News_agent created with output_keys.")

#Root Agent

root_agent = Agent(
    name="StartupIntelligenceRoot",
    description="Master agent coordinating claim extraction, fact-checking, and news summary.",
    instruction="""
You will coordinate all the sub-agents in the following sequence:

1. Send the user text to ClaimExtractor to extract claims.
2. Send extracted claims to FactChecker.
3. Ask NewsSummaryAgent for news for the requested period.
4. Combine responses into a detailed final report.
""",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
   tools=[AgentTool(claim_extractor), AgentTool(fact_checker), AgentTool(news_agent)],
)

print("✅ root_agent created with output_key.")


#Runner
runner = InMemoryRunner(agent=root_agent)
response = await runner.run_debug(
    "I want to start a toy business .. what will be it's status by 2030..."
)
