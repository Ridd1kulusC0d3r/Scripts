import requests
from bs4 import BeautifulSoup

def search_cpf_data(cpf):
    url = f"https://example.com/?cpf={cpf}"  # Substitua pelo URL apropriado de pesquisa
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        nome = soup.find("span", class_="nome").text
        telefone = soup.find("span", class_="telefone").text
        rg = soup.find("span", class_="rg").text
        
        return {
            "Nome": nome,
            "Telefone": telefone,
            "RG": rg
        }
    else:
        return None

cpf = "123.456.789-00"  # Substitua pelo CPF desejado
cpf_data = search_cpf_data(cpf)

if cpf_data:
    print("Informações encontradas:")
    for key, value in cpf_data.items():
        print(f"{key}: {value}")
else:
    print("Informações não encontradas.")
