import requests
from bs4 import BeautifulSoup

def search_web_data(url, search_term):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = []

        # Encontrar todos os elementos que contenham o termo de busca
        for element in soup.find_all(text=lambda text: search_term in text):
            data.append(element)

        return data

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []

# Insira a URL do site e o termo de busca desejado
url_to_search = 'https://www.exemplo.com'
search_term = 'CPF'

# Realizar a busca e imprimir os resultados
search_results = search_web_data(url_to_search, search_term)
for result in search_results:
    print(result)
