from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from prompts.presentation_prompt import PRESENTATION_PROMPT

model=ChatMistralAI(model="mistral-small-2603")

def presentation_agent(report : str ) :

    prompt=PRESENTATION_PROMPT.format(

        report=report
    )

    response=model.invoke(prompt)

    return response.content