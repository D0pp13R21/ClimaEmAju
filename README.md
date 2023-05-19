Em pt-br logo abaixo do texto em en-us.
# Weather Bot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

Weather Bot is a Twitter bot that posts the weather in the city of Aracaju three times a day - at 6 AM, 12 PM, and 6 PM. It uses the OpenWeatherMap API to fetch the weather data and the Google Translate API to translate the weather description to Brazilian Portuguese.

The bot is designed to help followers stay informed about weather changes, particularly concerning flooding and heavy rainfall, in Aracaju. The bot is created as a hobby project by a Municipal Civil Defense employee to assist and raise awareness among the local community.

## Features

- Posts weather updates three times a day on Twitter.
- Retrieves weather data from the OpenWeatherMap API.
- Translates weather descriptions to Brazilian Portuguese using the Google Translate API.

## Requirements

- Python 3.x
- tweepy library
- requests library
- googletrans library

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/weather-bot.git
```

2. Navigate to the project directory:

```
cd weather-bot
```

3. Install the required libraries:

```
pip install -r requirements.txt
```

4. Set up Twitter API credentials and OpenWeatherMap API key (see Configuration section).

## Configuration

Before running the bot, you need to set up the necessary API credentials and keys. Follow the steps below:

### Twitter API

1. Create a Twitter Developer account at https://developer.twitter.com/.

2. Create a new app and generate the following credentials:
   - Consumer Key (API Key)
   - Consumer Secret (API Secret Key)
   - Access Token
   - Access Token Secret

3. Open the `config.py` file and update the following variables with your Twitter API credentials:

```python
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
```

### OpenWeatherMap API

1. Sign up for an OpenWeatherMap account at https://home.openweathermap.org/users/sign_up.

2. After signing in, go to the API Keys section.

3. Generate an API key.

4. Open the `config.py` file and replace `'your_api_key'` with your OpenWeatherMap API key:

```python
API_KEY = 'your_api_key'
```

## Usage

To start the Weather Bot, run the following command in the terminal:

```
python bot.py
```

The bot will automatically post weather updates on Twitter three times a day for the city of Aracaju.

## License

This project is licensed under the [MIT License](LICENSE).

---

# Bot do Clima

[![Licença](https://img.shields.io/badge/licença-MIT-blue.svg)](LICENSE_PT)

## Descrição

O Bot do Clima é um bot do Twitter que publica informações sobre o clima na cidade de Aracaju três vezes ao dia - às 6h, 12h e 18h. Ele utiliza a API do OpenWeatherMap para obter os dados do clima e a API do Google Translate para traduzir a descrição do clima para o português brasileiro.

O bot foi criado como um projeto de hobby por um funcionário da Defesa Civil Municipal com o objetivo de ajudar e conscientizar a comunidade local sobre as mudanças climáticas, especialmente em relação a enchentes e fortes chuvas, em Aracaju.

## Recursos

- Publica atualizações sobre o clima três vezes ao dia no Twitter.
- Obtém

 os dados do clima da API do OpenWeatherMap.
- Traduz a descrição do clima para o português brasileiro usando a API do Google Translate.

## Requisitos

- Python 3.x
- Biblioteca tweepy
- Biblioteca requests
- Biblioteca googletrans

## Instalação

1. Clone o repositório:

```
git clone https://github.com/your-username/weather-bot.git
```

2. Navegue até o diretório do projeto:

```
cd weather-bot
```

3. Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

4. Configure as credenciais da API do Twitter e a chave da API do OpenWeatherMap (consulte a seção de Configuração).

## Configuração

Antes de executar o bot, você precisa configurar as credenciais e chaves da API necessárias. Siga as etapas abaixo:

### API do Twitter

1. Crie uma conta de desenvolvedor no Twitter em https://developer.twitter.com/.

2. Crie um novo aplicativo e gere as seguintes credenciais:
   - Consumer Key (API Key)
   - Consumer Secret (API Secret Key)
   - Access Token
   - Access Token Secret

3. Abra o arquivo `config.py` e atualize as seguintes variáveis com as suas credenciais da API do Twitter:

```python
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
```

### API do OpenWeatherMap

1. Cadastre-se em uma conta do OpenWeatherMap em https://home.openweathermap.org/users/sign_up.

2. Após fazer o login, acesse a seção de Chaves da API.

3. Gere uma chave da API.

4. Abra o arquivo `config.py` e substitua `'your_api_key'` pela sua chave da API do OpenWeatherMap:

```python
API_KEY = 'your_api_key'
```

## Uso

Para iniciar o Bot do Clima, execute o seguinte comando no terminal:

```
python bot.py
```

O bot irá publicar automaticamente atualizações sobre o clima no Twitter três vezes ao dia para a cidade de Aracaju.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE_PT).