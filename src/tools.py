from crewai_tools import SerperDevTool, ScrapeWebsiteTool

def get_search_tool():
    """
    Returns a SerperDevTool for web searching.
    Requires SERPER_API_KEY in environment.
    """
    return SerperDevTool()

def get_scrape_tool():
    """
    Returns a ScrapeWebsiteTool for content extraction.
    """
    return ScrapeWebsiteTool()
