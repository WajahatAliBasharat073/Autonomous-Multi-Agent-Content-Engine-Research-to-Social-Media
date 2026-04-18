from crewai import Task

def get_planning_task(agent):
    return Task(
        description=(
            "1. Prioritize the latest trends, key players, "
            "and noteworthy news on {topic}.\n"
            "2. Identify the target audience, considering "
            "their interests and pain points.\n"
            "3. Develop a detailed content outline including "
            "an introduction, key points, and a call to action.\n"
            "4. Include SEO keywords and relevant data or sources."
        ),
        expected_output="A comprehensive content plan document "
                        "with an outline, audience analysis, "
                        "SEO keywords, and resources.",
        agent=agent,
    )

def get_writing_task(agent):
    return Task(
        description=(
            "1. Use the content plan to craft a compelling "
            "blog post on {topic}.\n"
            "2. Incorporate SEO keywords naturally.\n"
            "3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
            "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
            "5. Proofread for grammatical errors and "
            "alignment with the brand's voice."
        ),
        expected_output="A well-written blog post "
                        "in markdown format, ready for publication, "
                        "each section should have 2 or 3 paragraphs.",
        agent=agent,
    )

def get_editing_task(agent):
    return Task(
        description=("Proofread the given blog post for "
                     "grammatical errors and "
                     "alignment with the brand's voice."),
        expected_output="A well-written blog post in markdown format, "
                        "ready for publication, "
                        "each section should have 2 or 3 paragraphs.",
        agent=agent
    )

def get_linkedin_post_task(agent):
    return Task(
        description=(
            "1. Read the final edited blog post created by the Editor.\n"
            "2. Summarize the most impactful insight from the post.\n"
            "3. Craft a concise (max 200 words) LinkedIn summary.\n"
            "4. Include 3-5 relevant hashtags and a polite 'call to action' "
            "(e.g., 'Read the full insights in our latest article')."
        ),
        expected_output="A polished, engaging LinkedIn post summary in markdown format, "
                        "ready for scheduling.",
        agent=agent,
    )
