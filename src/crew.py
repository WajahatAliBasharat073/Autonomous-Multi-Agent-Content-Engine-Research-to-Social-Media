from crewai import Crew
from src.agents import (
    get_planner_agent, 
    get_writer_agent, 
    get_editor_agent, 
    get_social_media_agent
)
from src.tasks import (
    get_planning_task, 
    get_writing_task, 
    get_editing_task, 
    get_linkedin_post_task
)

def build_content_engine_crew():
    """
    Assembles the 4-agent crew for content research and social media distribution.
    """
    # 1. Initialize Agents
    planner = get_planner_agent()
    writer = get_writer_agent()
    editor = get_editor_agent()
    social_media_poster = get_social_media_agent()

    # 2. Initialize Tasks
    plan_task = get_planning_task(planner)
    write_task = get_writing_task(writer)
    edit_task = get_editing_task(editor)
    post_summary_task = get_linkedin_post_task(social_media_poster)

    # 3. Assemble the Crew
    crew = Crew(
        agents=[planner, writer, editor, social_media_poster],
        tasks=[plan_task, write_task, edit_task, post_summary_task],
        verbose=2
    )
    
    return crew
