from dotenv import load_dotenv
from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.report_agent import report_agent

load_dotenv()

topic = input("ENTER YOUR TOPIC : ")

results = research_agent(topic)

print("\n[1] SEARCH RESULTS\n")

for index, result in enumerate(results["results"], start=1):
    print(f"{index}. {result['title']}")
    print(result['url'])
    print()

analysis = analysis_agent(results)

print("\n[2] ANALYSIS REPORT\n")
print(analysis) 

report = report_agent(analysis)

print("\n[3] FINAL REPORT\n")
print(report)