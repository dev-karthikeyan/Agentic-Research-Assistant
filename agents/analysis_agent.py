from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from prompts.analysis_prompt import analysis_prompt

load_dotenv()

model=ChatMistralAI(model="mistral-small-2603")

def analysis_agent(search_results : str) :

    content = ""

    for result in search_results["results"]:
        content += result["content"] + "\n\n"

    prompt= analysis_prompt(content=content)

    response = model.invoke(prompt)

    return response.content
