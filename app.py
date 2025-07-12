from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

from dotenv import load_dotenv

load_dotenv()

topic = "Medical industry using Generative AI"

llm= LLM(model="gpt-4")

#search tool

serch_tool = SerperDevTool(n=10)

#Agent 1
senior_research_analyst = Agent(
    role = "Senior Research Analyst",
    goal= f"Research, analyze, and synthesize comprehensive information on {topic} from reliable web sources",#topic is writen above 
    backstory= "your an expert research analyst with advanced web research skills,"
               "You excel at finding, analyzing and synthesizing information from"
               "across the internet using search tools. you're at"
               "distinguishing reliable source from unreliable ones"
               "fack-checking, cross-referencing information, and identifying key patterns and insight"
               "You provide well-organized research briefs with proper citations"
               "and source verification Your analysis includes both raw data and interpreted insights, making complex information accessible and actionable."
    allow_delegation=False,
    verbose=True,
    tools=           
)