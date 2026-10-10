import requests

def search_data(url, data_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            if data_name in content:
                print(f"O dado '{data_name}' foi encontrado na URL: {url}")
            else:
                print(f"O dado '{data_name}' não foi encontrado na URL: {url}")
        else:
            print(f"Falha ao acessar a URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Erro durante a requisição: {e}")

# Insira a URL e o nome do dado que deseja buscar
url_to_search = "https://www.exemplo.com"
data_to_search = "exemplo_desejado"

search_data(url_to_search, data_to_search)
