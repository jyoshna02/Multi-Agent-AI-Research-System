from tools.web_search import search_web

def research_agent(topic):
    topic = topic.strip()
    if not topic:
        raise ValueError("Please enter a research topic.")
    print("\nResearch Agent started!")
    print("Research Topic:",topic)
    search_results = search_web(topic)
    research_result = {
        "agent": "Research Agent",
        "topic": topic,
        "status": "Research completed",
        "sources": search_results
    }
    return research_result