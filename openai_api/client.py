import openai
import os
from dotenv import load_dotenv

load_dotenv()

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {}{}{} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro.
    '''
    openai.api_key = 'token-invalido' # os.getenv('OPENAI_API_KEY')
    prompt = prompt.format(brand, model, year)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
    )
    return response['choices'][0]['text']

