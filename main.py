from dotenv import load_dotenv
from agents.research_agent import research_agent

load_dotenv()

topic = input("ENTER YOUR TOPIC :")

results=research_agent(topic)

print("\nSEARCH RESULTS\n")

for index,result in enumerate(results["results"],start=1) :

    print(f"{index}. {result['title']}")
    print(result['url'])
    print()