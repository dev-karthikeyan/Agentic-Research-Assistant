from tools.tavily_search import search_topic

def research_agent(topic: str):

    print("\n[1] Searching web...\n")

    results = search_topic(topic)

    return results