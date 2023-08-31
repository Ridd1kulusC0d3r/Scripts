import requests

def search_web_data(url, data_type, file_type):
    response = requests.get(f"{url}?data_type={data_type}&file_type={file_type}")
    return response.text

url = input("Digite a URL: ")
data_type = input("Digite o tipo de dado: ")
file_type = input("Digite o tipo de arquivo: ")

result = search_web_data(url, data_type, file_type)
print(result)
