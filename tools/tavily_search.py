import os 
from tavily import TavilyClient

client=TavilyClient(

    api_key=os.getenv("TAVILY_API_KEY")
)

def search_topic(topic : str ) :

    response=client.search(
       query=topic,
       max_results=5
)
    
    return response