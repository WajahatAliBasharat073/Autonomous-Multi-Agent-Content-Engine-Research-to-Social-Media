from crewai import Agent
from src.tools import get_search_tool

def get_planner_agent():
    return Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory="You're working on planning a blog article "
                  "about the topic: {topic}. "
                  "You collect information that helps the "
                  "audience learn something and make informed decisions. "
                  "Your work is the basis for the Content Writer to write an article on this topic.",
        allow_delegation=False,
        verbose=True,
        tools=[get_search_tool()]
    )

def get_writer_agent():
    return Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
        backstory="You're working on a writing a new opinion piece about the topic: {topic}. "
                  "You base your writing on the work of the Content Planner, who provides an outline "
                  "and relevant context about the topic. You follow the main objectives and "
                  "direction of the outline, as provide by the Content Planner.",
        allow_delegation=False,
        verbose=True
    )

def get_editor_agent():
    return Agent(
        role="Editor",
        goal="Edit a given blog post to align with the writing style of the organization.",
        backstory="You are an editor who receives a blog post from the Content Writer. "
                  "Your goal is to review the blog post to ensure that it follows journalistic best practices, "
                  "provides balanced viewpoints, and avoids major controversial topics.",
        allow_delegation=False,
        verbose=True
    )

def get_social_media_agent():
    return Agent(
        role="Social Media Manager",
        goal="Summarize the key insights from the finalized {topic} article "
             "into a compelling and concise LinkedIn post.",
        backstory="You are a social media expert specializing in professional "
                  "platforms like LinkedIn. Your goal is to take high-quality, "
                  "technical content and adapt it for social media engagement, "
                  "generating curiosity and driving traffic to the main article.",
        allow_delegation=False,
        verbose=True
    )
