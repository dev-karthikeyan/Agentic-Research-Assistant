from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model=ChatMistralAI(model="mistral-small-2603")

def analysis_agent(search_results : str) :

    content = ""

    for result in search_results["results"]:
        content += result["content"] + "\n\n"

    prompt= f"""

     You are an expert Research Analyst.

Your task is to analyze the provided research data and generate a structured research report.

Research Data:
{content}

Instructions:

- Read and analyze all available information.
- Identify the main topic and overall context.
- Extract the most important findings.
- Highlight significant insights and trends.
- Mention opportunities, risks, and challenges if present.
- Ignore duplicate information.
- Focus on factual and evidence-based observations.
- Keep the analysis concise but informative.

Generate the response in the following format:

# Research Topic

# Executive Summary
A short overview of the research.

# Key Findings
- Finding 1
- Finding 2
- Finding 3

# Important Insights
- Insight 1
- Insight 2
- Insight 3

# Trends and Patterns
- Trend 1
- Trend 2

# Opportunities
- Opportunity 1
- Opportunity 2

# Risks / Challenges
- Risk 1
- Risk 2

# Conclusion
Provide a clear final conclusion based on the research.
"""
    response = model.invoke(prompt)

    return response.content
