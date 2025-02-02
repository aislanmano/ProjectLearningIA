import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:

    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.3-70b-versatile')
    
    def invoke(self, question):
        prompt = PromptTemplate(
            input_variables=['pergunta'],
            template='''
            Você é um especialsiat em marcas e modelos de de carros.
            Responda a pergunta do usuário sempre com dados detalhados dos carros e também curiosidades e também sobre os carros.
            Use emoji sempre que possível.
            <pergunta>
            {pergunta}
            </pergunta>
            '''
        )
        chain = prompt | self.__chat | StrOutputParser()
        response = chain.invoke({
            'pergunta': question,
        })
        return response