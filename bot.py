import tweepy
import requests
from googletrans import Translator

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def traduzir_texto(texto, dest='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=dest)
    return traducao.text

def postar_clima_aracaju():
    # Fazer uma requisição à API de clima (usando a API do OpenWeatherMap)
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Aracaju&appid=sua_api_key'
    resposta = requests.get(url)
    dados_clima = resposta.json()

    # Extrair informações relevantes do JSON de resposta
    temperatura = dados_clima['main']['temp']
    descricao_clima = dados_clima['weather'][0]['description']

    # Converter temperatura de Kelvin para Celsius
    temperatura_celsius = round(temperatura - 273.15, 1)

    # Traduzir a descrição do clima para o português do Brasil
    descricao_traduzida = traduzir_texto(descricao_clima, dest='pt')

    # Formatar a mensagem de tweet
    mensagem = f"Clima em Aracaju: {descricao_traduzida}, {temperatura_celsius}°C"

    # Postar o tweet
    api.update_status(mensagem)

# Exemplo de uso da função para postar o clima nos horários especificados
postar_clima_aracaju()
