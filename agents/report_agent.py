from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from prompts.report_prompt import REPORT_PROMPT

load_dotenv()

model = ChatMistralAI(model="mistral-small-2603")

def report_agent(analysis: str):

    prompt = REPORT_PROMPT.format(
        analysis=analysis
    )

    response = model.invoke(prompt)

    return response.content