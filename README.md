## lista_api_py é um exemplo de uma Api em Python  com algumas funções de teste e um arquivo para conteinerização (Dockerfile).

🦸‍♂️ Projeto que visa exemplificar a implementação de uma API web, onde é possível enviar uma lista de valores, recuperar essa lista e também aplicar funções de média, valor máximo e valor mínimo. As listas ficam salvas em memória e serão perdidas ao encerrar a aplicação.

🦸‍♂️ O diretório "tests" contem dois arquivos com exemplos de testes implementados com o pytest.

🦸‍♂️ O arquivo Dockerfile é um exemplo de como fazer um build de uma imagem da aplicação e criar um contêiner docker a partir dela. 

Projeto desenvolvido durante a **Data Science Codenation** 

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python3.7]
- [Flask]
- [Loguru]
- [Pytest]
- [UUID]
- [Docker]

# 🚀 Como rodar este projeto

## Sem Docker:
**Vá para a pasta do projeto**

$ cd lista_api_py

**Instalar Python e dependências**

$ pip install python=3.7

$ pip install -r requirements.txt

**Execute a aplicação**

$ python app.py

**Execute os testes**

$ pytest -v tests/ 

## Com Docker:
**Utilizando o Docker CLI vá para a pasta do projeto**

$ cd lista_api_py

**Criando Imagem Docker**

$ docker build -t lista_api_py:0.0.1 .

**Criando e executando o contêiner Docker**

$ docker run -p 5000:5000 lista_api_py:0.0.1

*Nota: a imagem está em meu diretório público do docker hub, podendo também ser importada diretamente com o comando abaixo*

$ docker pull mcaldeiragoes/lista_api_py:0.0.1  

# 🚀 Como interagir com a API

Basicamente devemos fazer as chamadas nas rotas da API. Eu utilizei a ferramenta Postman, porém existem muitas outras opções desse tipo. Outro exemplo seria o Insomnia.

Por padrão o serviço é executado em http://0.0.0.0:5000/

*Nota: Quando utilizar Docker, verificar qual é o IP publicado pelo host do contêiner.*

## Existem 5 rotas definidas para essa aplicação:

*/data* - Método POST para criar uma lista de valores e retornar seu UUID. A lista é enviada no corpo da requisição: 
{
    "data":[1, 2, 3, 4, 10, 15, 25]
}

*/data/UUID* - Método GET para retornar uma lista a partir de seu UUID

*/data/UUID/min* - Método get para retornar o valor mínimo dos dados de uma lista a partir de seu UUID

*/data/UUID/mean* - Método get para retornar o valor médio dos dados de uma lista a partir de seu UUID

*/data/UUID/max* - Método get para retornar o valor máximo dos dados de uma lista a partir de seu UUID