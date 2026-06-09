from tools.tavily_search import search_topic

def research_agent(topic : str) :

    result=search_topic(topic)
    
    print("\nSearching the web...\n")

    return result 